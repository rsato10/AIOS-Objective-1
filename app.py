import streamlit as st
import pandas as pd
import numpy as np

import os
from apikey import apikey
from langchain.llms import OpenAI
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey

#Framework
st.title('Afterflea aios Objective 1')
prompt = st.text_input('Enter prompt')

#LLM
llm = OpenAI(temperature = 0.9)

if(prompt):
    response = llm(prompt)
    st.write(response)