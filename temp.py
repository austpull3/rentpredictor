import streamlit as st

import pandas as pd

import time 

import numpy as np

#conn = sqlite3.connect('rentpredictor')


st.title("Predict MLB Batting Average!⚾️")


from PIL import Image 
image = Image.open('rentpredictor/mike.png')
#image2 = Image.open('/Users/austinpullar/Desktop/julio.png')
#image3 = Image.open('/Users/austinpullar/Desktop/Frankie.png')
#image4 = Image.open('/Users/austinpullar/Desktop/Bryce.png')
#image5 = Image.open('/Users/austinpullar/Desktop/vs.jpeg')




import base64

"""## Home Run Bryce Harper!!!🎆"""
file_ = open("/Users/austinpullar/Desktop/giphy.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
            
            
            
            
