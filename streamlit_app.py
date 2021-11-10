# based on Fanilo Andrianasolo's "Convert a MIDI file to WAV" Streamlit app

import streamlit as st
import spacy_streamlit

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
    
    
    st.text("Example using the components provided by spacy-streamlit in an existing app.")
    
    python -m spacy download en_core_web_sm
    
        
    DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""
    spacy_model = "en_core_web_sm"

    st.title("My cool app")
    text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
    doc = spacy_streamlit.process_text(spacy_model, text)
    
    spacy_streamlit.visualize_ner(
    doc,
    labels=["PERSON", "DATE", "GPE"],
    show_table=False,
    title="Persons, dates and locations",
 )
    st.markdown(f"Analyzed using spaCy model {spacy_model}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown(
    "Made with 💜 by [@aouriri (she/her)](https://github.com/aouriri) as a [LEADING](https://cci.drexel.edu/mrc/leading/) fellow."    
)


st.sidebar.markdown(
    "**Fellowship site:** University of California - San Diego (UCSD) [Library](https://library.ucsd.edu/), **Project name:** [Transformation and Enhancement of the Farmworker Movement Collection](https://libraries.ucsd.edu/farmworkermovement/)"
)

