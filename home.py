import streamlit as st
st.title("S-GPT STUDIO")
st.snow()
if st.button("TRAIN YOUR OWN GPT!"):
    st.switch_page("pages/2_Training.py")
if st.button("INFERNCE"):
    st.switch_page("pages/Inference.py")