import streamlit as st
from transformers import pipeline

# Load the translation pipeline
@st.cache_resource
def load_translation_pipeline():
    return pipeline("translation", model="facebook/nllb-200-distilled-600M")

pipe = load_translation_pipeline()

# Available target languages
languages = {
    "French": "fra_Latn",
    "Spanish": "spa_Latn",
    "German": "deu_Latn",
}

# Main Streamlit app
def main():
    st.title("✨ Multilingual Translator")
    
    # Creating two columns for the form and the translation result
    
    st.write("##")
        # Text input for translation
    text_to_translate = st.text_area("Enter text to translate...")
        
        # Dropdown for selecting the target language
    target_lang = st.selectbox("Select target language:", list(languages.keys()))

        # Translate button
    if st.button("Translate"):
        if text_to_translate:
                # Perform translation
            target_lang_code = languages[target_lang]
            translation = pipe(text_to_translate, src_lang="eng_Latn", tgt_lang=target_lang_code)
            st.session_state['translation'] = translation[0]['translation_text']

  
    st.write("Translated To:", target_lang )
        # Display the translated text if available
    if 'translation' in st.session_state:
        st.write(st.session_state['translation'])

if __name__ == "__main__":
    main()
