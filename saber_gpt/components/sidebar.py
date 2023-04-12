import streamlit as st
from saber_gpt.components import config
from saber_gpt.components.faq import faq
from saber_gpt.components import UIelements


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown(
            "1. Select an API Key\n"
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )

        dropdown_options = config.options_data["dropdown_options"]
        api_key_input = st.sidebar.selectbox("Select and API Key: ", dropdown_options) 

        if api_key_input:
            set_openai_api_key(api_key_input)

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "This is a fork of KnowledgeGPT"
        )
        st.markdown(
            "This tool is a work in progress. "
        )
        st.markdown("Originally Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("Forked by [snmendoza] (https://github.com/snmendoza)")
        st.markdown("---")

        faq()
