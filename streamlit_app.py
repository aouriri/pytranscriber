# based on Fanilo Andrianasolo's "Convert a MIDI file to WAV" Streamlit app

import streamlit as st

app_formal_name = "Audio Conversion//Speech to Text//NER"

# EDIT config
st.set_page_config(
        page_title="pytranscriber",
        page_icon=":arrows_clockwise:",
        initial_sidebar_state="auto",
        menu_items={
          'Report a bug': "https://www.extremelycoolapp.com/bug",
          'About':  f"[{app_formal_name}](https://github.com/aouriri/pytranscriber) "
    f"converts mp3 files to wav (with the option to download), transcribes that audio file to text using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) Python library. "
    f"The text can the be copied to be used elsewhere **or** processed using [spaCy](https://github.com/explosion/spacy-streamlit). "
   
        }
)

st.sidebar.markdown("-----------------------------------")

# elseif statement?
page = st.sidebar.selectbox('Select page',
  ['Audio Conversion','Speech to Text Transcription', 'Named Entity Recognition'])
if page == 'Audio Conversion':
    # Display the conversion content here
    st.title("mp3 to wav converter")
    
    mp3 = st.file_uploader("Upload mp3 file.", type=["mp3"])
elif page == 'Speech to Text Transcription':
    # Display the transcription content here
    st.title("Speech to Text Transcription")
else:
    # Display the NER content here
    st.title("Named Entity Recognition")
    
    st run 'https://raw.githubusercontent.com/aouriri/pytranscriber/main/spacyNER_code.py'

st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown(
    "Made with 💜 by [@aouriri (she/her)](https://github.com/aouriri) as a [LEADING](https://cci.drexel.edu/mrc/leading/) fellow."    
)


st.sidebar.markdown(
    "**Fellowship site:** University of California - San Diego (UCSD) [Library](https://library.ucsd.edu/), **Project name:** [Transformation and Enhancement of the Farmworker Movement Collection](https://libraries.ucsd.edu/farmworkermovement/)"
)

