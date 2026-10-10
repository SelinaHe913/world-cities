import streamlit as st


st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
)

st.title("World Cities")
st.write("Welcome! Click the button below to explore the World Cities app.")

if st.button("Go to App", type="primary"):
    st.switch_page("pages/app.py")
