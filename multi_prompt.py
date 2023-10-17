## Integrate our code openAI API 
## Chains: We need to send output of the first prompt to the next prompt as input.
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Steramlit framework
st.title('Search language model')
input_text = st.text_input('search the topic you want')

## openAI LLM
llm=OpenAI(temperature=0.8)

# prompt tempplate 
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name} model"
)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='language_model')

# prompt tempplate 
second_input_prompt = PromptTemplate(
    input_variables=['language_model'],
    template="When was released this {language_model}"
)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='year')

# prompt tempplate 
third_input_prompt = PromptTemplate(
    input_variables=['year'],
    template="Mention other 5 large language models released at {year}"
)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='other_LLMs')

# combine sequence
parent_chain= SequentialChain(chains=[chain,chain2,chain3], input_variables = ['name'], output_variables = ['language_model', 'year', 'other_LLMs'],verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))