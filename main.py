# bsd

import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2) # returns n columns to us

# "with" statement used when opening files, it ensures that files are closed properly and catches errors
with col1:
    st.image("images/prof.jpg") #you can change the width of image here...

with col2:
    st.title("David Berger")
    content = """
    Hi! this is a block of text.
    """
    # the three quotations allows a multi line string
    # st.write(content)
    st.info(content) # this method gives a nice background





