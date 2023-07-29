import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title('David Benitoe')
    content = """
    Hi, I am David! I am currently a benefits analyst who loves data. I hope to one day become a data anlayst at the
    mid-senior level.
    """
    st.info(content)