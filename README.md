# 🔍 LLM-based Web Search with Memory (RAG)  
### you can also check simple streamlit version of this, without flask here: https://github.com/krakken190/Web-Search-with-Memory-RAG-and-LLM

This project implements a **Retrieval-Augmented Generation (RAG)** system with a **Streamlit frontend** and a **Flask backend**. It uses **Serper.dev** for web search and **OpenAI's GPT** models (via LangChain) to generate responses based on real-time web content.

https://github.com/user-attachments/assets/4ae04087-ad7e-4d0d-874a-ca8bd80680c1

---

## ✨ Features

- ✅ Search the web using the Serper.dev API.
- ✅ Scrape and extract meaningful content from the top 2 search results.
- ✅ Generate context-aware answers using OpenAI’s GPT model.
- ✅ **Supports follow-up questions** with memory (like ChatGPT).
- ✅ Displays sources for every answer.
- ✅ Stores chat history per user in a folder (`chat_history/`).

---

## Memory + Follow-Up Support

- It uses **LangChain’s `ConversationBufferMemory`** to preserve past messages.
- The Streamlit UI allows users to enter follow-up questions without resetting the chat.
- Chat history is displayed in the interface and persisted to disk (`chat_history/user_1.json`).

---

## 📁 Folder Structure
project-root/

├── app.py             # Flask backend

├── utils.py           # Search, scraping, and answer generation logic

├── streamlit_app.py   # Frontend Streamlit app

├── .env               # API keys for Serper and OpenAI

├── chat_history/      # Stores user chat logs

└── requirements.txt   # All dependencies

---

## 🔧 Setup Instructions

### 1. Clone the repository

```
git clone [https://github.com/your-username/rag-search-app.git](https://github.com/your-username/rag-search-app.git)
cd rag-search-app
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add .env file
```
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the Flask backend
```
python app.py
```

### 5. Run the Streamlit frontend
```
streamlit run streamlit_app.py
```

📋 Usage

Enter your first query in the input box.

Wait for the answer and the sources.

Enter follow-up questions in the same box — the chat history will be preserved.

Check chat_history/user_1.json for the conversation logs.

Also you can clear the chat, which will remove chat_history too
