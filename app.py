import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(
    page_title="Language Translation Tool",
    layout="centered"
)

st.title("Language Translation Tool")

st.write("Translate text between multiple languages.")

languages = {
    "English": "en",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru"
}

text = st.text_area("Enter text to translate")

if text:
    st.write("Word Count:", len(text.split()))
    st.write("Character Count:", len(text))

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

translate_btn = st.button("Translate")

if translate_btn:

    if text.strip() == "":
        st.warning("Please enter text.")
    else:

        try:

            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translated Text")

            st.text_area(
                "Result",
                translated,
                height=150
            )

            st.download_button(
                label="Download Translation",
                data=translated,
                file_name="translation.txt",
                mime="text/plain"
            )

            try:
                tts = gTTS(
                    text=translated,
                    lang=languages[target_lang]
                )

                temp_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp3"
                )

                tts.save(temp_file.name)

                audio_file = open(
                    temp_file.name,
                    "rb"
                )

                st.audio(
                    audio_file.read(),
                    format="audio/mp3"
                )

            except:
                st.info(
                    "Audio not available for this language."
                )

        except Exception as e:
            st.error(f"Error: {e}")

if st.button("Clear"):
    st.rerun()