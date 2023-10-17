## Integrate our code openAI API 

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Steramlit framework
st.title('Search language model')
input_text = st.text_input('search the topic you want')

# prompt tempplate # using one prompt template
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name} model"
)

## openAI LLM
llm=OpenAI(temperature=0.8)

chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True )

if input_text:
    st.write(chain.run(input_text))