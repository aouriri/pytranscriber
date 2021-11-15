# based on Fanilo Andrianasolo's "Convert a MIDI file to WAV" Streamlit app

import io
import numpy as np
import requests
import streamlit as st
import spacy
import spacy_streamlit
from bs4 import BeautifulSoup

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

page = st.sidebar.selectbox('Select page',
  ['Audio Conversion','Speech to Text Transcription', 'Named Entity Recognition'])
if page == 'Audio Conversion':
# Display the conversion content here
    st.title(":arrows_clockwise: mp3 to wav converter")
    sess = load_session()
	
    def download_from_URL(url: str, sess: requests.Session) -> bytes:
        user_agent = {"User-agent": "bot"}
        r_page = sess.get(url, headers=user_agent)
        soup = BeautifulSoup(r_page.content, "html.parser")
        link = soup.find(lambda tag: tag.name == "a" and tag.has_attr("download"))
    if link is None:
        st.error(f"No mp3 file found on page '{url}'")
        raise ValueError(f"No mp3 file found on page '{url}'")

    url_mp3_file = "http.*\.mp3"
    r_mp3_file = sess.get(url_midi_file, headers=user_agent)
    return r_mp3_file.content
        
    uploaded_mp3 = st.file_uploader("Upload mp3 file", type=["mp3"])
    mp3_link = st.text_input(
        "Or input URL", "https://libraries.ucsd.edu/farmworkermovement/media/oral_history/music/Huelga%203%20Cesar%20Chavez.mp3"
    )
        
    run_button = st.button('Convert!')

elif page == 'Speech to Text Transcription':
    # Display the transcription content here
    st.title("Speech to Text Transcription")
else:
    # Display the NER content here
    st.title("Named Entity Recognition")
    
    st.text("Example using the components provided by spacy-streamlit in an existing app.")    
       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown(
    "Made with 💜 by [@aouriri (she/her)](https://github.com/aouriri) as a [LEADING](https://cci.drexel.edu/mrc/leading/) fellow."    
)


st.sidebar.markdown(
    "**Fellowship site:** University of California - San Diego (UCSD) [Library](https://library.ucsd.edu/), **Project name:** [Transformation and Enhancement of the Farmworker Movement Collection](https://libraries.ucsd.edu/farmworkermovement/)"
)
