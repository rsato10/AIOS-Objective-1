import streamlit as st
import pandas as pd
import numpy as np

import os
from apikey import apikey
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chains import SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apikey

#Framework
st.title('Afterflea aios Objective 1 Clothing store recommendation')
with st.form("my_form"):
    chain_list = []

    type_i = st.text_input('type:')
    color_i = st.text_input('color:')
    city_i = st.text_input('city:')
    extra_i = st.text_area('Fill in with more details, please.')

    prompt_template = PromptTemplate(
        input_variables=["type", "color", "city", "extra"],
        template="find a store that sells {type} in the color {color} in the city {city} {extra}."
    )   
    #llm
    llm = OpenAI(temperature = 0.9)

    chain = (LLMChain(llm=llm, prompt=prompt_template, verbose=True))
    submitted = st.form_submit_button("Submit")
    if((len(type_i) + len(color_i) + len(city_i) + len(extra_i)) > 0):
        response = chain.run(type = type_i, color = color_i, city = city_i, extra = extra_i)
        st.write(response)