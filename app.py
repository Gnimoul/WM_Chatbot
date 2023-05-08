import streamlit as st

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

import os

from modules.layout import Layout
from modules.history import ChatHistory
from modules.chatbot import Chatbot

def init():
    os.environ["OPENAI_API_KEY"] = st.secrets['path']
    st.set_page_config(layout="centered", page_icon="💬", page_title="Wang Mian | Chat-Bot 🤖")
    st.title("王勉GPT")
    st.text('Powered by GPT-3.5 Turbo @OpenAI ; Version Date: 2023.5.8')

def main():
    # Initialize the app
    init()
    embeddings = OpenAIEmbeddings()
    vectors = FAISS.load_local("./data/csv_index", embeddings)

    # Instantiate the main components
    layout = Layout()

    #layout.show_header()
    layout.reset_chat_button()

    # Initialize chat history
    history = ChatHistory()

    try:
        chatbot = Chatbot('gpt-3.5-turbo', 0.0, vectors)
        st.session_state["ready"] = True
        st.session_state["chatbot"] = chatbot
        # Create containers for chat responses and user prompts
        response_container, prompt_container = st.container(), st.container()
        with prompt_container:
            # Display the prompt form
            is_ready, user_input = layout.prompt_form()
            # Initialize the chat history
            history.initialize()
            # Reset the chat history if button clicked
            if st.session_state["reset_chat"]:
                history.reset()
            if is_ready:
                # Update the chat history and display the chat messages
                history.append("user", user_input)
                output = st.session_state["chatbot"].conversational_chat(user_input)
                history.append("assistant", output)
        history.generate_messages(response_container)
    except Exception as e:
        st.error(f"Error: {str(e)}")

    st.markdown("""
    注意：

    1. 回答仅供参考，请以**王勉作品数据库**为准，[使用说明](https://weibo.com/3182148054/M02BazHQC)、[腾讯文档](https://docs.qq.com/sheet/DQmJLRU1jSVNGU1hI)、[Notion](https://band-science-345.notion.site/c5739e0796754870ae6faccf1fdc4ace?continueFlag=79ffd5fcb61f5a609d5f0e732d0f2e83)；
    2. 如果您有任何疑问或建议，可以在微博私信[@Gnimoul](https://weibo.com/u/3182148054)。
    
    """)

# streamlit run app.py
if __name__ == "__main__":
    main()