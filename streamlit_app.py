import streamlit as st
import spacy
import spacy_streamlit
	
st.title('Named Entity Recognition')
	
DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""
	
spacy_model = "en_core_web_sm"
nlp = spacy.load(spacy_model)
nlp.add_pipe("opentapioca")
nlp.to_disk("/tmp/en_core_web_sm_ot")
	
text = st.text_area("Text to analyze (Default text can be used, but I'm okay with change.)", DEFAULT_TEXT, height=200)
doc = spacy_streamlit.process_text("/tmp/en_core_web_sm_ot", text)
	
spacy_streamlit.visualize_ner(
	doc,
	labels=["PERSON", "DATE", "GPE", "ORG", "NORP", "LAW", "LOC"],
	show_table=False,
	title="Person, Places and Other Things",
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
