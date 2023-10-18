import time
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print(OPENAI_API_KEY)
# def translate(input_text, target_language, target_audience):
#     # Use a translation library to translate the input text
#     with st.spinner(text="Translating.."):
#         time.sleep(1)

#     translated_text = "This is JUST a demo"

#     # Return the translated text
#     return translated_text

# if __name__ == "__main__":

#     st.title("Localization Engine")

#     # Create a text input for the target language
#     target_language = st.text_input("Target Language:")

#     # Create a text input for the target audience
#     target_audience = st.text_input("Target Audience:")

#     col1, col2 = st.columns(2)
#     # Create a text input for the input text
#     input_text = col1.text_area("Input Text:", height=300)

#     # Create a text input for the output text
#     output_text = col2.text_area("Output Text:", height=300, key="output_text")

#     # Create a button to translate the text
#     translate_button = st.button("Translate")

#     if translate_button:
#         # Get the input text
#         input_text = input_text.strip()

#         # Get the target language
#         target_language = target_language.strip()

#         # Translate the text
#         translated_text = translate(input_text, target_language, target_audience)

#         # Set the output text
#         st.session_state["output_text"] = translated_text


        