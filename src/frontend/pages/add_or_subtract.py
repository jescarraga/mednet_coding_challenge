import streamlit as st
import requests

st.set_page_config(
    page_title="Add or Subtract",
    page_icon="➕",
)

st.title("Add or Subtract Two Numbers with different Units of Weight, Height or Distance")

st.subheader("Select the type of the unit to convert")

# Select the type of the unit to convert
type_of_conversion = st.selectbox(
    label="Select the type to convert",
    options=["weight", "height", "distance"],
    index=0,
)

# Enter the number to convert

st.subheader("Enter the numbers and their units")

options = {
    "weight": ["kg", "g", "lb", "oz"],
    "height": ["cm", "m", "in", "ft"],
    "distance": ["km", "m", "cm", "mi"],
}

col1, col2 = st.columns(2)

with col1:

    number_1 = st.number_input(
        label="Enter the first number",
        value=0.0,
        step=0.1,
        format="%.5f",
        min_value=0.0,
    )
    
    st.subheader("Select the unit of the first number")
    
    unit_1 = st.selectbox(
    label="Select the unit of the first number",
    options=options[type_of_conversion],
    index=0,
    )

with col2:

    number_2 = st.number_input(
        label="Enter the second number",
        value=0.0,
        step=0.1,
        format="%.5f",
        min_value=0.0,
    )
    
    st.subheader("Select the unit of the second number")
    
    unit_2 = st.selectbox(
    label="Select the unit of the second number",
    options=options[type_of_conversion],
    index=0,
    )

# Select the operation
    
st.subheader("Select the operation")

operation = st.selectbox(
    label="Select the operation",
    options=["add", "subtract"],
    index=0,
)

# Data request

data_req_1 = {
    "number": str(number_1),
    "unit": unit_1
}

data_req_2 = {
    "number": str(number_2),
    "unit": unit_2
}

data_req = {
    "entry_data_1": data_req_1,
    "entry_data_2": data_req_2,
}

if st.button("Calculate"):

    st.subheader("Result")

    url = f"http://backend/convert/{str(type_of_conversion)}/{str(operation)}"

    api_call = requests.post(
        url,
        json=data_req
    )

    if api_call.status_code != 200:
        st.write("Error")
    elif(api_call.json()[0] == api_call.json()[1]):
        st.write("The units of the numbers are the same, the result is")
        st.write(api_call.json()[0]["number"] + " " + api_call.json()[0]["unit"])
    elif(api_call.json()[0] != api_call.json()[1]):
        st.write("The result is")
        st.write(api_call.json()[0]["number"] + " " + api_call.json()[0]["unit"])
        st.write(api_call.json()[1]["number"] + " " + api_call.json()[1]["unit"])