import streamlit as st

st.write("# Welcome to Streamlit! 👋")
num1 = st.number_input('num 1')
num2 = st.number_input('num 2')
num3 = st.number_input('num 3')

max_num = max(num1, num2, num3)
st.write(f"max number is {max_num}")