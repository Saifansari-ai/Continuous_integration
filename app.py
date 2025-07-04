import streamlit as st

# Stream lit UI
st.title("Power calculator")
st.write("Enter a number to calculate its square,cube and fifth power")

# Input
n = st.number_input("Enter a input number",value=1,step=1)

# calculate result

square = n**2
cube = n**3
fifth_power = n**5

st.write(f"The Square of {n} is : {square}")
st.write(f"the Cube of the {n} is : {cube}")
st.write(f"The Fifth power of {n} is : {fifth_power}")
