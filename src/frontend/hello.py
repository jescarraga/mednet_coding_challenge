import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.markdown('''

# MedNet - Coding Challenge

This project is a user interface and an API that allows the user to converts a given number and his Unit of weight, height or distance to another unit of the same type.

Also allow to add or subtract two numbers on different units of weight, height or distance.

# Assumptions

* The API will only convert between the following units:
    - Weight: kg, g, lb, oz
    - Height: cm, m, in, ft
    - Distance: km, m, cm, mi

* The API will only add or subtract between the any of the previous units.

* The API will only accept positive numbers.

* The API was developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints and WSL2 as the development environment with docker.
  
# Author

Hi everyone, I am Jordan Escarraga and I am a backend developer, focused on data-driven solutions.
            
''')