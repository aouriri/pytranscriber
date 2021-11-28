import io
import numpy as np
import requests
import time
import speech_recognition as sr
import streamlit as st
import spacy
import spacy_streamlit
from bs4 import BeautifulSoup
from os import path

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
# Based on Fanilo Andrianasolo's Streamlit MIDI to WAV Converter.
# NOTE: adjust requests/URL sections to point toward page(s) of interest
	@st.cache(allow_output_mutation=True)
	def load_session():
		return requests.Session()

	@st.cache(
		hash_funcs={requests.Session: id},
		allow_output_mutation=True,
		suppress_st_warning=True,
		)
	def download_from_URL(url: str, sess: requests.Session) -> bytes:
		user_agent = {"User-agent": "bot"}
		r_page = sess.get(url, headers=user_agent)
		soup = BeautifulSoup(r_page.content, "html.parser", from_encoding = "iso-8859-1")
		link = soup.find_all(lambda tag: tag.name == "a")
		if link is None:
			st.error(f"No mp3 file found on page '{url}'")
			raise ValueError(f"No mp3 file found on page '{url}'")

		url_mp3_file = "https://audionautix.com/"
		r_mp3_file = sess.get(url_mp3_file, headers=user_agent)
		return r_mp3_file.content


	st.title(":arrows_clockwise: mp3 to wav converter")
	sess = load_session()
	
	uploaded_file = st.file_uploader("Upload mp3 file", type=["mp3"])
	mp3_link = st.text_input("or input mp3 URL", "https://audionautix.com/Music/AskRufus.mp3"
	)
	
	mp3_file = None

	if uploaded_file is None:
		with st.spinner(f"Downloading mp3 file from {mp3_link}"):
			mp3_file = io.BytesIO(download_from_URL(mp3_link, sess))
	else:
		mp3_file = uploaded_file
	
	st.markdown("---")
	
	st.audio(uploaded_file)
	st.text("Preview uploaded file. Audio file can be downloaded as wav file by clicking the vertical elipses on the player and selecting 'Download'.")
        
elif page == 'Speech to Text Transcription':
# Display the transcription content here
    	st.title('Speech to Text Transcription')
    	fileObject = st.file_uploader("Please upload your file")
    
    	#filename = fileObject
    	#r = sr.Recognizer()

    	#with sr.AudioFile(filename) as source:
	#	audio_data = r.record(source)
	#	text = r.recognize_google(audio_data)
    
    	#transcribedtxt = st.text_area("Transcribed text", text)
st.markdown("Speech to text using ```Python``` can be done 'out of the box' on short audio (less than/equal to a minute) using Google's Speech Recognition." 
		    "The code for that is included below. For larger audio files, an API must be used."
		    "For this project, I am using [IBM's Speech to Text](https://www.ibm.com/cloud/watson-speech-to-text) and its cloud." 
		    "Its 'Lite' option includes 500 minutes of *free* speech recognition a month." 
		    "If you choose to use another recognition API, **please fork/update code to reflect that.**" 
		    "**The attaching of my IBM Cloud account is for demostrative purposes.**"
		   )
	
code = ''' # Be sure to (pip) install SpeechRecognition before starting!
	import speech_recognition as sr
	
	r = sr.Recognizer()
	r.recognize_google()
	harvard = sr.AudioFile('harvard.wav') # Example local audio file
	with harvard as source:
		audio = r.record(source)'''
	st.code(code, language='python')
	
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
