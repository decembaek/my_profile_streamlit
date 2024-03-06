import streamlit as st

st.title("Decembaek Library")
col1, col2 = st.columns(2)

col1.image(
    "images/circle_profile.png",
    caption="Profile",
    width=50,
    # use_column_width="always",
)
col2.write("Hellow my name is Seunggyu")
