import streamlit as st

st.set_page_config(
    page_title="Offshore Wind Farm Dashboard",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Navigation")
st.sidebar.write("Choose a page")

st.title("Machine learning")
st.write("Machine Learning Model")
