import streamlit as st
import requests


st.set_page_config(
    page_title="Convert Number",
    page_icon="⚖",
)

st.title("Convert Number to Another Unit of Weight, Height or Distance")

st.subheader("Select the type of the unit to convert")

# Select the type of the unit to convert
type_of_conversion = st.selectbox(
    label="Select the type to convert",
    options=["weight", "height", "distance"],
    index=0,
)

st.subheader("Enter the number to convert")
# Enter the number to convert
number = st.number_input(
    label="Enter the number to convert",
    value=0.0,
    step=0.1,
    format="%.5f",
    key=None,
    min_value=0.0,
)

options = {
    "weight": ["kg", "g", "lb", "oz"],
    "height": ["cm", "m", "in", "ft"],
    "distance": ["km", "m", "cm", "mi"],
}

st.subheader("Select the unit to convert")

unit = st.selectbox(
    label="Select the unit to convert",
    options=options[type_of_conversion],
    index=0,
)

st.subheader("Select the desired unit")

unit_target = st.selectbox(
    label="Select the desired unit",
    options=options[type_of_conversion],
    index=0,
)

data_request = {
    "number": str(number),
    "unit": unit,
}

if st.button("Convert"):

    url = f"http://backend/convert/{str(type_of_conversion)}"

    api_call = requests.post(
        url,
        params={
            "unit_target": unit_target,
        }, json=data_request
    )

    st.subheader("Result")

    st.write(api_call.json()["number"] + " " + api_call.json()["unit"])

