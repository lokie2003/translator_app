import os
import ctranslate2
import streamlit as st
from huggingface_hub import snapshot_download
from sentencepiece import SentencePieceProcessor

# As per https://opennmt.net/CTranslate2/performance.html
# By default CTranslate2 is compiled with intel MKL.
# It is observed that this setting has a significant positive performance impact.
os.environ["CT2_USE_EXPERIMENTAL_PACKED_GEMM"] = "1"

model_name = "santhosh/madlad400-3b-ct2"
model_path = snapshot_download(model_name)

tokenizer = SentencePieceProcessor()
tokenizer.load(f"{model_path}/sentencepiece.model")
translator = ctranslate2.Translator(model_path)
tokens = [tokenizer.decode(i) for i in range(460)]
lang_codes = [token[2:-1] for token in tokens if token.startswith("<2")]

def translate(input_text, target_language):
    input_tokens = tokenizer.encode(f"<2{target_language}> {input_text}", out_type=str)
    results = translator.translate_batch(
        [input_tokens],
        batch_type="tokens",
        beam_size=1,
        no_repeat_ngram_size=1,
    )
    translated_sentence = tokenizer.decode(results[0].hypotheses[0])
    return translated_sentence

st.title("MADLAD-400 Translation Demo")
st.markdown("""

""", unsafe_allow_html=True)

input_text = st.text_area("Input Text", "Imagine a world in which every single person on the planet is given free access to the sum of all human knowledge.")
target_language = st.selectbox("Target Language", lang_codes)
translated_text = translate(input_text, target_language)
st.text_area("Translated Text", translated_text)
