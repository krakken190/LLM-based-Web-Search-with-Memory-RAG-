# 🚀 LLM-Powered Web Search with RAG and Memory

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0-black?logo=flask)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25-ff4b4b?logo=streamlit)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-4cbfaf?logo=openai)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a sophisticated **Retrieval-Augmented Generation (RAG)** system that combines real-time web search with the conversational power of Large Language Models. It features a modern **Streamlit** frontend and a robust **Flask** backend, providing users with accurate, context-aware answers complete with source citations.

<br>

https://github.com/user-attachments/assets/4ae04087-ad7e-4d0d-874a-ca8bd80680c1

---

### Table of Contents
* [About The Project](#about-the-project)
* [How It Works](#how-it-works)
* [Key Features](#-key-features)
* [Tech Stack](#-tech-stack)
* [Folder Structure](#-folder-structure)
* [Getting Started](#-getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#-usage)
* [Contributing](#-contributing)
* [License](#-license)

---

## About The Project

This application enhances traditional LLM capabilities by grounding them in up-to-date information from the web. Instead of relying solely on its training data, the model can perform live web searches, scrape relevant content, and synthesize an answer based on the retrieved information. The integrated memory module allows for natural, human-like follow-up conversations.

![RAG Flowchart](https://github.com/user-attachments/assets/1cf76875-f0a3-4313-a965-92e2d2ad662a)


## How It Works

The application follows a simple yet powerful architectural pattern:

1.  **Frontend Interaction**: The user enters a query into the Streamlit interface.
2.  **Backend Request**: Streamlit sends the query and chat history to the Flask API.
3.  **Web Search**: The Flask backend uses the **Serper.dev API** to perform a real-time web search.
4.  **Content Scraping**: The system scrapes the top search results for relevant content using **BeautifulSoup**.
5.  **RAG Generation**: The scraped text, user query, and conversation history are passed to an **OpenAI GPT model** via **LangChain**.
6.  **Memory**: **`ConversationBufferMemory`** from LangChain is used to retain context for follow-up questions.
7.  **Response**: The generated answer and its sources are sent back to the Streamlit UI and displayed.


## ✨ Key Features

-   **Live Web Search**: Integrates with Serper.dev for real-time information retrieval.
-   **Retrieval-Augmented Generation**: Scrapes web content to provide answers based on current data.
-   **Conversational Memory**: Supports seamless follow-up questions using chat history.
-   **Source Citations**: Displays the URLs from which information was extracted, ensuring transparency.
-   **Persistent Chat History**: Saves conversation logs for each user session.
-   **Clean, Decoupled Architecture**: Separate Flask backend for logic and Streamlit frontend for UI.


## 💻 Tech Stack

This project is built with a modern, scalable tech stack:

-   **Backend**: Flask
-   **Frontend**: Streamlit
-   **LLM Integration**: LangChain, LangChain-OpenAI
-   **Web Scraping**: BeautifulSoup4
-   **API Communication**: Requests
-   **Environment Management**: python-dotenv


## 📁 Folder Structure

The project is organized with a clear separation of concerns between the frontend and backend services.

```
LLM-based-Web-Search-with-Memory-RAG-/
├── flask_app/
│ ├── app.py # Flask API endpoints
│ └── utils.py # Core logic for search, scraping, and generation
│
├── streamlit_app/
│ ├── app.py # Streamlit user interface
│ └── chat_history/ # Stores user conversation logs (e.g., user_1.json)
│
├── requirements.txt # Project dependencies
└── README.md # You are here!
```


## 🔧 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

Make sure you have Python 3.9+ installed on your system.

### Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/krakken190/LLM-based-Web-Search-with-Memory-RAG-.git
    cd LLM-based-Web-Search-with-Memory-RAG-
    ```

2.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the `flask_app` directory and add your API keys:
    ```
    SERPER_API_KEY="your_serper_api_key"
    OPENAI_API_KEY="your_openai_api_key"
    ```

4.  **Run the Flask backend:**
    Navigate to the backend directory and start the server.
    ```
    cd flask_app
    python app.py
    ```
    The backend will be running at `http://127.0.0.1:5000`.

5.  **Run the Streamlit frontend:**
    Open a new terminal, navigate to the frontend directory, and run the app.
    ```
    cd streamlit_app
    streamlit run app.py
    ```
    The application will be accessible at `http://localhost:8501`.


## 📋 Usage

1.  Open your browser and go to `http://localhost:8501`.
2.  Type your first question in the input box and press Enter.
3.  The app will display the answer along with the sources it used.
4.  Ask a follow-up question to see the memory feature in action!
5.  To start a new conversation, use the "Clear Chat" button.


## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
