import io
import numpy as np
import requests
import streamlit as st
import spacy
import spacy_streamlit
from bs4 import BeautifulSoup
from spacy.kb import KnowledgeBase
from os import path
from pydub import AudioSegment

app_formal_name = 'Audio Conversion//Speech to Text//NER'

st.set_page_config(
        page_title="pytranscriber",
        page_icon=":arrows_clockwise:",
        initial_sidebar_state="auto",
        menu_items={
          'Report a bug': "https://github.com/aouriri/pytranscriber/issues",
          'About':  f"[{app_formal_name}](https://github.com/aouriri/pytranscriber) "
    f"converts mp3 files to wav (with the option to download), transcribes that audio file to text using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) Python library. "
    f"The text can the be copied to be used elsewhere **or** processed using [spaCy](https://github.com/explosion/spacy-streamlit). "
   
        }
)

st.sidebar.markdown("-----------------------------------")

page = st.sidebar.selectbox('Select page',
  ['Audio Conversion','Speech to Text Transcription', 'Named Entity Recognition'])
st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown(
    'Made with 💜 by [@aouriri (she/her)](https://github.com/aouriri) as a [LEADING](https://cci.drexel.edu/mrc/leading/) fellow.'    
)
st.sidebar.markdown(
    '**Fellowship site:** University of California - San Diego (UCSD) [Library](https://library.ucsd.edu/), **Project name:** [Transformation and Enhancement of the Farmworker Movement Collection](https://libraries.ucsd.edu/farmworkermovement/)'
)

if page == 'Audio Conversion':
# Display the conversion content here
# based on Fanilo Andrianasolo's "Convert a MIDI file to WAV" Streamlit app

# NOTE: adjust requests/URL sections to point toward page(s) of interest

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

	def download_from_website(url: str, sess: requests.Session) -> bytes:
		user_agent = {"User-agent": "bot"}
		r_page = sess.get(url, headers=user_agent)
		soup = BeautifulSoup(r_page.content, "html.parser")
		link = soup.find(lambda tag: tag.name == "a" and tag.has_attr("download"))
		if link is None:
			st.error(f"No mp3 file found on page '{url}'")
			raise ValueError(f"No mp3 file found on page '{url}'")

		url_mp3_file = "https://library.ucsd.edu/" + link["href"] # change URL to request/query other sites, using UCSD FW website as example
		r_mp3_file = sess.get(url_mp3_file, headers=user_agent)
		return r_mp3_file.content

	def main():
		st.title(":arrows_clockwise: mp3 to wav converter")
		sess = load_session()
		
		uploaded_file = st.file_uploader("Upload mp3 file", type=["mp3"])
		audio_link = st.text_input(
			"Or input URL"
		)
		
	mp3_file = None
	
	uploaded_file = st.file_uploader("Upload mp3 file", type=["mp3"])
	audio_link = st.text_input(
			"Or input URL"
		)
	sess = load_session()

	if uploaded_file is None:
        	if "https://library.ucsd.edu/farmworkermovement/media/oral_history/music/" not in audio_link:
            		st.error("Make sure your URL is of type 'https://library.ucsd.edu/farmworkermovement/media/oral_history/music/<mp3_name>'")
            		st.stop()
        	with st.spinner(f"Downloading mp3 file from {audio_link}"):
            		mp3_file = io.BytesIO(download_from_website(audio_link, sess))
	else:
		mp3_file = uploaded_file
			
	st.markdown("---")
	
	with st.spinner(f"Transcribing to wav"):
        	# files
		src = mp3_file

		# convert wav to mp3                                                            
		audSeg = AudioSegment.from_mp3(mp3_file)
		
		virtualfile = io.BytesIO()
		wavfile.write(virtualfile, 44100, audSeg)
	
	st.audio(virtualfile)
	st.markdown("Download the audio by right-clicking on the media player")
        
elif page == 'Speech to Text Transcription':
# Display the transcription content here
    st.title('Speech to Text Transcription')
        
else:
    # Display the NER content here
    # Example using the components provided by spacy-streamlit in an existing app.
    st.title('Named Entity Recognition')
           
    DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""
    
    spacy_model = "en_core_web_sm"
    text = st.text_area("Text to analyze (Default text can be used but, I'm okay with change.)", DEFAULT_TEXT, height=200)
    doc = spacy_streamlit.process_text(spacy_model, text)

    spacy_streamlit.visualize_ner(
            doc,
            labels=["PERSON", "DATE", "GPE", "ORG", "NORP", "LAW", "LOC"],
            show_table=False,
            title="Person, Places and Other Things"
    )
    with st.expander("Entity label explanation"):
            st.write("""
                **PERSON:**      People, including fictional.
                
**NORP:**        Nationalities or religious or political groups.

**ORG:**         Companies, agencies, institutions, etc.

**GPE:**         Countries, cities, states.

**LOC:**         Non-GPE locations, mountain ranges, bodies of water.

**LAW:**         Named documents made into laws.

**DATE:**        Absolute or relative dates or periods.
     """)
    
    st.text(f'Analyzed using spaCy model {spacy_model}.')
