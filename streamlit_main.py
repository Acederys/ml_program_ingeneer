import io
import streamlit as st
from io import StringIO
from transformers import pipeline
st.title('Text translator in the Streamlit')
uploaded_file = st.file_uploader("Select the file.txt you want to translate")
def load_file():
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

        return string_data
    else:
        return None

string = load_file()

result = st.button('TRANSLATE')

if result:
    with st.container():
        classifier = pipeline('translation', 'Helsinki-NLP/opus-mt-en-ru')
        Values_list = classifier(string)
        st.caption(Values_list[0]['translation_text'])

