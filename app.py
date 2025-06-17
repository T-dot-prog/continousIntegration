import streamlit as st


st.write("Power Calculator")
st.write("Enter a number to calculate the square , qube and fifth power")

user_input = st.number_input("Enter an Integar: ", value = 1, step = 1)


square = user_input **2

cube = user_input **3 

fifth = user_input ** 5

st.write(f"The square of {user_input} is : {square}")
st.write(f"The cube of {user_input} is : {cube}")
st.write(f"The fifth power of {user_input} is : {fifth}")