
from langchain.memory import ConversationBufferMemory
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from langchain.chains import ConversationalRetrievalChain
from langchain.schema import messages_from_dict, messages_to_dict
from openai import OpenAI
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load keys
load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LangChain model
chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)

# memory object
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def search_articles(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    data = {"q": query}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    results = response.json()

    return [
        {"title": result.get("title", ""), "url": result.get("link", "")}
        for result in results.get("organic", [])[:2]
    ]

def fetch_article_content(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = [
            tag.get_text().strip() for tag in soup.find_all(['h1', 'h2', 'h3', 'p'])
            if tag.get_text().strip()
        ]
        return "\n".join(content)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def concatenate_content(articles):
    full_text = ""
    for article in articles:
        content = fetch_article_content(article["url"])
        full_text += f"\n\nFrom: {article['title']}\n{content}"
    return full_text.strip()

def generate_answer_with_memory(content, query):
    # Load memory history 
    input_messages = memory.load_memory_variables({})["chat_history"]

    # new user query wrapped in HumanMessage
    input_messages.append(
        HumanMessage(content=f"You are a helpful assistant. Use the following content to answer the question:\n\n{content}\n\nNow, here is the user's question:\n{query}")
    )

    # using invoke()
    response = chat_model.invoke(input_messages)

    # current turn into memory
    memory.save_context({"input": query}, {"output": response.content})

    return response.content.strip()
