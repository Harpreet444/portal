import streamlit as st

def app():
    st.title(":violet[BBSBC Gallary]")

    co1,co2,co3 = st.columns([1,1,1])
    col1, col2= st.columns([1,1])

    co1.image("tech.jpg")
    co2.image("tech.jpg")
    co3.image("tech.jpg")
    col1.image("1-min-1024x683.jpg")
    col2.image("1-min-1024x683.jpg")