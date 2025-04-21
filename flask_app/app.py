from flask import Flask, request, jsonify
from utils import search_articles, concatenate_content, generate_answer_with_memory

app = Flask(__name__)

@app.route('/')
def index():
    return "LLM RAG Search API is running. Use POST requests to /query with a JSON payload containing the 'query' field."

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        user_query = data.get("query", "")
        print("🔍 Received query:", user_query)

        articles = search_articles(user_query)
        content = concatenate_content(articles)
        answer = generate_answer_with_memory(content, user_query)

        return jsonify({
            "answer": answer,
            "sources": articles if articles else []
        })

    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Flask backend is running. Use POST /query to send a query.")
    app.run(host='localhost', port=5001)
