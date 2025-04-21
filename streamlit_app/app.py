import streamlit as st
import requests
import os
import json

st.set_page_config(page_title="LLM RAG Search", page_icon="🔍")
st.title("LLM-based RAG Search")
st.caption("Note: Memory-enabled chat. Ask follow-ups!")

# folder to store chat
os.makedirs("chat_history", exist_ok=True)
HISTORY_FILE = "chat_history/user_1.json"

# Initialize chat history
if "chat_history" not in st.session_state:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            st.session_state.chat_history = json.load(f)
    else:
        st.session_state.chat_history = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    st.rerun()  

# full chat history
st.markdown("### Chat")
for msg in st.session_state.chat_history:
    st.markdown(f"**You:** {msg['query']}")
    st.markdown(f"**AI:** {msg['answer']}")

st.markdown("---")

query = st.text_input("Ask something (initial or follow-up):", key="input_query")

if st.button("Send") and query.strip():
    with st.spinner("💬 Thinking..."):
        try:
            response = requests.post("http://localhost:5001/query", json={"query": query})
            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "No answer.")
                sources = data.get("sources", [])

                # Save interaction
                new_entry = {"query": query, "answer": answer}
                st.session_state.chat_history.append(new_entry)

                with open(HISTORY_FILE, "w") as f:
                    json.dump(st.session_state.chat_history, f, indent=2)

                # Show latest result
                st.success("### Answer")
                st.write(answer)

                if sources:
                    st.info("### Sources")
                    for s in sources:
                        st.markdown(f"- [{s['title']}]({s['url']})")
            else:
                st.error(f" Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f" Backend error: {e}")