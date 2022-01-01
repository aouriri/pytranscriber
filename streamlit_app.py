# clean up unnecessary imports
import io
import requests
import os
import json
import pydub
import urllib.request as url
import streamlit as st
import spacy
import spacy_streamlit
import en_core_web_sm
from bs4 import BeautifulSoup
from spacy import displacy
from os import path
from os.path import join, dirname
from pydub import AudioSegment
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


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

st.sidebar.markdown("-----------------------------------")

st.sidebar.markdown(
	'Institute of Museum and Library Services (IMLS), LB21 LEADING project: RE-246450-OLS-20'
)

if page == 'Audio Conversion':
# Display the conversion content here

	st.title(":arrows_clockwise: mp3 to wav converter")

	uploaded_file = st.file_uploader("Upload mp3 file", type=["mp3"])
	mp3_link = st.text_input("or input mp3 URL")

	if len(mp3_link) >1:
		source = url.urlopen(mp3_link).read()

	st.markdown("---")

	st.text("Preview selected file.")

	if len(mp3_link) != 0:
		audio = st.audio(mp3_link)
	else:
		audio = st.audio(uploaded_file)

	st.markdown("mp3s *uploaded locally* can be downloaded as a wav file from the audio player **(vertical elipses > 'Download')**, "
		    "mp3s from a *URL* must be converted, then downloaded. Click the **'Convert!'** button below to download the converted mp3."
		   )
	st.markdown("**PLEASE NOTE:** The 'Convert!' button is *only* available when URL is used.")

	if len(mp3_link) != 0:
		r = requests.get(mp3_link, allow_redirects=True)
		open('convaudio.wav', 'wb').write(r.content)

		with open('convaudio.wav', 'rb') as file:
			btn = st.download_button(
				label="Convert!",
				data=file,
				file_name="newaudio.wav",
				mime="audio/wav"
			)
	else:
		pass

elif page == 'Speech to Text Transcription':
# Display the transcription content here
	import config
	from config import apikey, url

	authenticator = IAMAuthenticator(configapikey)
	stt = SpeechToTextV1(authenticator=authenticator)
	stt.set_service_url(url)

	st.title('Speech to Text Transcription')
	st.markdown("Speech to text using ```Python``` can be done 'out of the box' on shorter audio (limited to 50 requests per day) using Google's Web Speech API. "
		    "The code for that is included below (click to expand!). For larger audio files, an API must be used. "
		    "For this project, I am using [IBM's Speech to Text](https://www.ibm.com/cloud/watson-speech-to-text) and its cloud. "
		    "Its 'Lite' option includes 500 minutes of *free* speech recognition a month. "
		    "If you choose to use another recognition API, **please fork/update code to reflect that.** "
		    "**The attaching of my IBM Cloud account is for demonstrative purposes.**"
		   )

	fileObject = st.file_uploader("Please upload your file", type=["wav"])
	if uploaded_file is not None:
		     bytes_data = fileObject.getvalue()

	with open(join(dirname('__file__'), bytes_data),'rb') as audio_file:
	 	dic = json.loads(
	 		json.dumps(
	 			service.recognize(
	 				audio=audio_file,
	 				content_type='audio/wav',
	 				timestamps=False,
	 				word_confidence=False).get_result(),
	 			indent=2))

	# Stores the transcribed text
	str = ""

	while bool(dic.get('results')):
		str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]

	st.markdown("---")
	st.text_area('Transcribed text', str) # replace quotes with str
	st.markdown("---")

	with st.expander("Speech Recognition (Basic) Code"):
		code = ''' # Be sure to (pip) install SpeechRecognition before starting!
		import speech_recognition as sr
		r = sr.Recognizer()
		r.recognize_google()
		harvard = sr.AudioFile('harvard.wav') # Example local audio file
		with harvard as source:
			audio = r.record(source)
		r.recognize_google(audio)
		f = open("transcription.txt", "a")
		f.write(r.recognize_google(audio))
		f.write(" ")
		f.close()'''
		st.code(code, language='python')

else:
	# Display the NER content here
	# Example using the components provided by spacy-streamlit in an existing app.

	st.title('Named Entity Recognition')

	DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""

	nlp = en_core_web_sm.load()
	text = st.text_area("Text to analyze (Default text can be used, but I'm okay with change.)", DEFAULT_TEXT, height=200)
	doc = spacy_streamlit.process_text("en_core_web_sm", text)

	spacy_streamlit.visualize_ner(
		doc,
		labels=["PERSON", "DATE", "GPE", "ORG", "NORP", "LAW", "LOC"],
		show_table=False,
		title="Person, Places and Other Things",
		#displacy_options={
		#	"kb_url_template": "https://www.wikidata.org/wiki/{}"
		#},
		#key="Default Colors"
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

	st.text(f'Analyzed using spaCy model en_core_web_sm with opentapioca pipe.')
