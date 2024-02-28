import streamlit as st
from googletrans import Translator

def translate(text, dest_lang) -> str:
    """
    Translates text to the specified destination language using Google Translate API.
    """
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest=dest_lang)
    return translated_text.text

def main():
    st.title("Text Translator")
    
    text_input = st.text_area("Enter text to translate", "Hi, how are you?")
    
    dest_lang = st.selectbox("Select destination language", ["Hindi", "Malayalam", "Kannada", "Tamil", "Telugu"])
    lang_dict = {"Hindi": "hi", "Malayalam": "ml", "Kannada": "kn", "Tamil": "ta","Telugu":"te"}
    selected_lang = lang_dict.get(dest_lang, "en")
    
    if st.button("Translate"):
        translated_text = translate(text_input, selected_lang)
        st.write("Translated Text:", translated_text)

if __name__ == "__main__":
    main()
