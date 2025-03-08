import streamlit as st

st.title("Personal Data Form")

name = st.text_input("Enter your Name")
surname = st.text_input("Enter your Surname")
age = st.number_input("Enter your Age", min_value=0, step=1)
height = st.number_input("Enter your Height ", min_value=0, step=1)

if st.button("Send"):
    if name and surname and age and height:
        st.write("### Your Personal Data:")
        st.write(f"**Name**: {name}")
        st.write(f"**Surname**: {surname}")
        st.write(f"**Age**: {age} years old")
        st.write(f"**Height**: {height} cm")
    else:
        st.error("Please fill in all fields.")

