# this code allow us to create application

import streamlit as st
import pandas as pd


st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)# for adding the title for html code

st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""") # to add only the text


# Function for loading the data
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# define some styles rely to the box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# load the data
load_(pd.read_csv('data/motos_scooters1.csv'), 'Motocycles data 1', '1')
load_(pd.read_csv('data/motos_scooters2.csv'), 'Motocycles data 2', '2')
load_(pd.read_csv('data/motos_scooters3.csv'), 'Motocycles data 3', '3')
load_(pd.read_csv('data/motos_scooters4.csv'), 'Motocycles data 4', '4')
load_(pd.read_csv('data/motos_scooters5.csv'), 'Motocycles data 5', '5')




 


