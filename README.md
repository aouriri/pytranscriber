# pytranscriber
**NOTE:** pytranscriber will be archived **May 16th** and no longer actively maintained. Feel free to go forth and fork (or copy certain parts)!

mp3 to WAV converter SLASH speech to text transcriber in Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/aouriri/pytranscriber/main)

## to do (later)
- [X] create logo
  - may rework it...
- [ ] update README or create Wiki to provide background/instructions
- [X] figure out how to merge spacy_streamlit NER with [OpenTapioca](https://github.com/UB-Mannheim/spacyopentapioca#vizualization) 
  - *mostly* figured out, QIDs not linked to Wikidata entry; ```displacy_options``` [(example)](https://github.com/explosion/spacy-streamlit/blob/dffa3fb6b1faa5ddf8098fea24132ad79f7f79e1/examples/04_visualize-ner-extra-options.py) enhancement may work once it's fully incorporated
  - **UPDATE [2022.04.04]**: ```displacy_options``` was updated to include extra options for NER visualizer and options are now live on app (WOO!).
- [X] add file upload option for speech-to-text
- [ ] [train Watson model](https://www.ibm.com/demos/live/content/watson/stt/lab/hands-on-lab-customization.pdf) using corpus?
- [X] try out STT "smart formatting" (currently in beta)
  - added!

-----------------
**Institute of Museum and Library Services (IMLS) acknowledgement statement:** Institute of Museum and Library Services (IMLS), LB21 LEADING project: RE-246450-OLS-20
