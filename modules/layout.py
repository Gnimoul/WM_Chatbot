import streamlit as st

class Layout:
    
    def show_header(self):
        """
        Displays the header of the app
        """
        st.markdown(
            """
            <h1 style='text-align: center;'> 欢迎来到王勉知识库 ! 😁</h1>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        """
        Displays the prompt form
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="请向我提问吧",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Send")
            
            is_ready = submit_button and user_input
        return is_ready, user_input
    
    def reset_chat_button(self):
        if st.button("重新开启对话（清空聊天历史）"):
            st.session_state["reset_chat"] = True
        st.session_state.setdefault("reset_chat", False)