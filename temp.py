import streamlit as st

import pandas as pd

import time 

import numpy as np



st.title("Predict MLB Batting Average!⚾️")

if st.checkbox('checkbox'):
    st.image("mike.png")

            
import pandas as pd 
df = pd.read_csv('savant_data (16).csv')

df = df[df['total_pitches'] > 10]
df = df.dropna()


if st.button('Predict Batting Average'):
    price = predict(hitter, hits, total_pitches)
    st.write(f"Predicted Batting Average for Bryce Harper against {hitter}")
    st.success( price)
