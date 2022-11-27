import streamlit as st

import pandas as pd

import time 

import numpy as np



st.title("Predict MLB Batting Average!⚾️")

if st.checkbox('checkbox'):
    st.image("mike.png")

            
import pandas as pd 
df = pd.read_csv('/Users/austinpullar/Downloads/savant_data (16).csv')

df = df[df['total_pitches'] > 10]
df = df.dropna()

import numpy as np
from sklearn.linear_model import LinearRegression

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

import streamlit as st
import pickle

pickle.dump(model, open('model.pkl', 'wb'))

pickled_model = pickle.load(open('model.pkl', 'rb'))


pickled_model.predict(x)

def predict(playerid, hits, total_pitches):
    #Predicting the price of the carat
    #if playerid == 593423:
        #"Mike Trout"
    #if hits == 3:
        #hits == 3
        
    #if total_pitches == 17:
       # total_pitches == 17
    prediction = model.predict(pd.DataFrame([[playerid, hits, total_pitches]], columns = ['playerid', 'hits', 'total_pitches']))
    return prediction

col, col2, col3 = st.columns(3)

st.header('Enter the characteristics: ')


hitter = st.selectbox(
    'Select a pitcher: ', ['593423', '541640'])
if hitter == '593423':
    st.write(f"You selected Frankie Montas")
    with col:
        st.header("Frankie Montas")
        st.image(image3)
    with col2:
        st.header(" ")
        st.write(" ")
        st.image(image5)
    with col3:
        st.header("Bryce Harper")
        st.image(image4)

elif hitter == '541640':
    st.write(f"You selected Erasmo Ramierz")
    
st.write("Hitter: Bryce Harper")


#playerid = st.number_input('playerid', min_value=1, max_value=10000000, value=1)
#if playerid == 593423:
    #'You selected: Mike Trout'
 
hits = st.number_input('hits:', min_value=1, max_value=50, value=1)
total_pitches = st.number_input('total_pitches:', min_value=1, max_value=50, value=1)



if st.button('Predict Batting Average'):
    price = predict(hitter, hits, total_pitches)
    st.write(f"Predicted Batting Average for Bryce Harper against {hitter}")
    st.success( price)
