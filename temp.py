import streamlit as st

if chck:
    primarycl = st.get_option("theme.primaryColor"

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

x = df[['player_id','hits', 'total_pitches']]
y = df['ba']
x = x.to_numpy()
y = y.to_numpy()

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
for i in range(10):
    print(x[i], y_pred[i])
    
# define input
new_input = [[593423, 3 ,17]]
# get prediction for new input
new_output = model.predict(new_input)
# summarize input and output
print(new_input, new_output) 

if st.checkbox("Show number of rows and columns"):
        st.write(f'Rows: {df.shape[0]}')
        st.write(f'Columns: {df.shape[1]}')

        
