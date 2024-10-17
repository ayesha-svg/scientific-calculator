import streamlit as st
import math

# Title
st.title("Scientific Calculator")

# User inputs
num1 = st.number_input("Enter first number:")
operation = st.selectbox("Select operation:", 
                          ["Addition", "Subtraction", "Multiplication", "Division", 
                           "Sine", "Cosine", "Tangent", "Logarithm"])

if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    num2 = st.number_input("Enter second number:")
    
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
else:
    if operation == "Sine":
        result = math.sin(math.radians(num1))
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
    elif operation == "Logarithm":
        if num1 > 0:
            result = math.log(num1)
        else:
            result = "Error: Logarithm of non-positive number!"

# Display result
st.write("Result: ", result)
