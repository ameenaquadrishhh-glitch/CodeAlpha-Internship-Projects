import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator")

text = st.text_area("Enter Text")

target = st.selectbox(
    "Target Language",
    ["english", "hindi", "french", "spanish", "german", "arabic"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source="auto",
        target=target
    ).translate(text)

    st.success(translated)