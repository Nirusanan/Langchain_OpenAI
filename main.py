## Integrate our code openAI API 

import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key
# Steramlit framework
st.title('langchain demo with openai')
input_text = st.text_input('search the topic you want')

## openAI LLM
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))