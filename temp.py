import streamlit as st

import pandas as pd

import time 

import numpy as np

st.button('Streamlit Button', help = "Click me!")


st.title("Predict MLB Batting Average!⚾️")

df = 'savant_data (16).csv'

if st.checkbox("Show number of rows and columns"):
  st.write(f'Rows: {df.shape[0]}')
  st.write(f'Columns: {df.shape[1]}')

if st.checkbox('checkbox'):
    st.image("mike.png")


