import streamlit as st
import json
import requests

st.title("Predict App")
st.write("")
st.write("Enter the X value in the textbox below")
X = st.number_input("X:", format="%0.00001f")

inputs = {"X":X}

if st.button('Predict'):
    res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(inputs))

    # way-3
    #dict_res = json.loads(res.text)
    #st.subheader(f"Response from API, y={dict_res['y']}")
    
    # way-2
    st.json(res.text)
    #yres = st.json(res.text)
    #st.subheader(f"Response from API {type(yres)}, {yres['y']}")
    
    # way-1
    #st.subheader(f"Response from API {res.text}")
    
    #{yres['y']}, 
    
    
