import streamlit as st
import pandas as pd
import numpy as np

import os
from apikey import apikey
from langchain.llms import OpenAI
from langchain.chains import LLMChain

#LLM
os.environ['OPENAI_API_KEY'] = apikey
llm = OpenAI(temperature = 0.9)

#Framework
st.title('Afterflea aios Objective 1')
with st.form("my_form"):
    prompt_list = []

    prompt_list.append(st.text_input('situation:'))

    prompt_list.append(st.text_input('emotion:'))

    prompt_list.append(st.text_input('resolution:'))

    prompt_list.append(st.text_area('Fill in with more details, please.'))

    input = ' '.join(prompt_list)
    
    submit = st.form_submit_button()

    if(input != ' ' and submit):
        response = llm(input)
        st.write(response)