import streamlit as st
from llm_helper import get_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A ChatBot")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)