import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sowjanya")
    content = """
    Upon completing her formal education, 
    Sowjanya Pamulapati set out to make her mark in the software engineering realm. She embarked on her professional 
    journey with unwavering determination and a desire to push the boundaries of what technology can achieve.
    """
    st.write(content)