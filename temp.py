import streamlit as st

import pandas as pd

import time 

import numpy as np

from sklearn.linear_model import LinearRegression



st.title("Predict MLB Batting Average!⚾️")

if st.checkbox('checkbox'):
    st.image("mike.png")

            
import pandas as pd 
df = pd.read_csv('savant_data (16).csv')

df = df[df['total_pitches'] > 10]
df = df.dropna()

if st.checkbox("Show number of rows and columns"):
        st.write(f'Rows: {df.shape[0]}')
        st.write(f'Columns: {df.shape[1]}')

        
