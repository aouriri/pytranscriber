import streamlit as st

app_formal_name = "Audio Conversion//Speech to Text//NER"

st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown(
    f"[{app_formal_name}](https://github.com/aouriri/pytranscriber) "
    f"converts mp3 files to wav (with the option to download), transcribes that audio file to text using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) Python library. "
    f"The text can the be copied to be used elsewhere **or** processed using [spaCy](https://github.com/explosion/spacy-streamlit). "
)

st.sidebar.markdown(
    "Made with 💜 by [@aouriri (she/her)](https://github.com/aouriri) as a [LEADING](https://cci.drexel.edu/mrc/leading/) fellow."    
)


st.sidebar.markdown(
        "Fellowship site: University of California - San Diego (UCSD) [Library](https://library.ucsd.edu/), Project name: [Transformation and Enhancement of the Farmworker Movement Collection](https://libraries.ucsd.edu/farmworkermovement/)"
)

st.write("mp3 to wav converter")

st.write("Speech to Text converter")

mp3 = st.file_uploader("Upload mp3 file.", type=["mp3"])
