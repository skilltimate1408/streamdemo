import streamlit as st

st.title("Demo")
user = st.text_input("Username")
pwd = st.text_input("Password", type="password")
st.button("Login")
