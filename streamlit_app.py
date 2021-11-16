# based on Fanilo Andrianasolo's "Convert a MIDI file to WAV" Streamlit app

import io
import numpy as np
import requests
import streamlit as st
import spacy
import spacy_streamlit
from bs4 import BeautifulSoup

app_formal_name = 'Audio Conversion//Speech to Text//NER'

# EDIT config
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
    st.title(":arrows_clockwise: mp3 to wav converter")
        
    uploaded_mp3 = st.file_uploader('Upload mp3 file', type=["mp3"])
    mp3_link = st.text_input('Or input URL')
        
    run_button = st.button('Convert!')

elif page == 'Speech to Text Transcription':
# Display the transcription content here
    st.title('Speech to Text Transcription')
        
else:
# Display the NER content here
    # Example using the components provided by spacy-streamlit in an existing app.
    st.title('Named Entity Recognition')
           
    DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""
    
    spacy_model = "en_core_web_sm"
    nlp.add_pipe('opentapioca')
    text = st.text_area("Text to analyze (Default text can be used but, I'm okay with change.)", DEFAULT_TEXT, height=200)
    doc = spacy_streamlit.process_text(spacy_model, text)

    spacy_streamlit.visualize_ner(
            #doc,
            #labels=["PERSON", "DATE", "GPE", "ORG", "NORP", "LAW", "LOC"],
            show_table=False,
            params={"text": doc.text,
                    "ents": [{"start": ent.start_char,
                    "end": ent.end_char,
                    "label": ent.label_,
                    "kb_id": ent.kb_id_,
                    "kb_url": "https://www.wikidata.org/entity/" + ent.kb_id_} 
                   for ent in doc.ents],
            title: "Persons, Places and Other Things"}
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
