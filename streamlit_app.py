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
    st.title("mp3 to wav converter")
    
    @st.cache(allow_output_mutation=True)
    def load_session():
        return requests.Session()
    
    def has_download_attr(tag):
        return tag.has_attr("download")

    @st.cache(
        hash_funcs={requests.Session: id},
        allow_output_mutation=True,
        suppress_st_warning=True,
    )
    def download_from_site(url: str, sess: requests.Session) -> bytes:
        user_agent = {"User-agent": "bot"}
        r_page = sess.get(url, headers=user_agent)
        soup = BeautifulSoup(r_page.content, "html.parser")
        link = soup.find(lambda tag: tag.name == "a" and tag.has_attr("download"))
        if link is None:
            st.error(f"No mp3 file found on page '{url}'")
            raise ValueError(f"No mp3 file found on page '{url}'")

        url_mp3_file = "http.*\.mp3"
        r_mp3_file = sess.get(url_mp3_file, headers=user_agent)
        return r_mp3_file.content
        
    def main():
        st.title(":arrows_clockwise: mp3 to wav converter")
        sess = load_session()
        
        uploaded_mp3 = st.file_uploader("Upload mp3 file.", type=["mp3"])
        mp3_link = st.text_input(
            "Or input URL", "https://libraries.ucsd.edu/farmworkermovement/media/oral_history/music/Huelga%203%20Cesar%20Chavez.mp3"
        )
        
        mp3_file = None
        
        if uploaded_file is None:
            if "http.*\.mp3" not in mp3_link:
                st.error("Make sure your URL is of type 'http.*\.mp3'")
                st.stop()
            with st.spinner(f"Downloading mp3 file from {mp3_link}"):
                mp3_file = io.BytesIO(download_from_bitmidi(mp3_link, sess))
        else:
            mp3_file = uploaded_mp3
            
        st.markdown("---")
        
        with st.spinner(f"Transcribing to wav"): # update to mp3 to wav code
            midi_data = pretty_midi.PrettyMIDI(midi_file)
            audio_data = midi_data.fluidsynth()
            audio_data = np.int16(
                audio_data / np.max(np.abs(audio_data)) * 32767 * 0.9
            )  # -- Normalize for 16 bit audio https://github.com/jkanner/streamlit-audio/blob/main/helper.py
            
            virtualfile = io.BytesIO()
            wavfile.write(virtualfile, 44100, audio_data)
            
        st.audio(virtualfile)
        st.markdown("Download the audio by selecting the vertical ellipsis and selecting 'Download' or by right-clicking on the media player")
        
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

