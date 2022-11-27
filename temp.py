import streamlit as st

import pandas as pd

import time 

import numpy as np

st.button('Streamlit Button', help = "Click me!")


st.title("Predict MLB Batting Average!⚾️")

df = 'savant_data (16).csv'

st.write(df)

if st.checkbox('checkbox'):
    st.image("mike.png")


