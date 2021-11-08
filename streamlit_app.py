import streamlit as st

st.sidebar.info('This is a purely informational message')

st.write("mp3 to wav converter")

st.write("Speech to Text converter")

mp3 = st.file_uploader("Upload mp3 file.")
