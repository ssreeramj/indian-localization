import time
import streamlit as st

import os
from dotenv import load_dotenv

import openai

load_dotenv()

st.set_page_config(layout="wide")

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def get_response(query, target_language, target_audience):
    system_message = """
    As an experienced and professional language translator, you specialize in translating Indian languages. 
    Please gather the following information from the user:

    1. SOURCE TEXT: The text you want to translate.
    2. TARGET LANGUAGE: The target language you want the text to be translated into.
    3. TARGET AUDIENCE: The intended target audience. Specify if the audience is around 10-15 years old or working
    professionals, or old people.

    You will adjust the choice of words and language usage based on the specified target audience and return 
    the translated text. Do not change any factual details from the source text.
    """

    final_prompt = f"""
    SOURCE TEXT:
    ```{query}```
    TARGET LANGUAGE:
    ```{target_language}```
    TARGET AUDIENCE:
    ```{target_audience}

    TRANSLATED TEXT:
    """
    model_name = "gpt-4" if st.session_state.get("use_gpt4") else "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "system", "content": system_message},
                {"role": "user", "content": final_prompt}
    ])
    
    try:
        translated_text = response.get("choices")[0].get("message").get("content")
    except Exception as e:
        st.error(body=e)

    return translated_text


def translate(inp_text, target_language, target_audience):
    if input_text.strip():
        with st.spinner(text="Translating.."):
            time.sleep(2)
            translated_text = get_response(inp_text, target_language, target_audience)
            # translated_text = "hello world"

            st.session_state.output_text = translated_text



if __name__ == "__main__":

    st.title("Localization Engine")

    is_gpt4 = st.checkbox("Use GPT-4", key="use_gpt4")

    col1, col2 = st.columns(2)
    # List of the most common languages in India
    common_languages = ["Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Kannada", "Odia", "Punjabi"]

    # Create a dropdown in Streamlit
    target_language = col1.selectbox("Select Target Language", common_languages, index=0)

    # Create a text input for the target audience
    target_audience = col2.text_input(
        "Target Audience:", 
        value="young children",
        placeholder="young, college going students | working professionals | old people")

    st.divider()

    col1, col2 = st.columns(2)
    # Create a text input for the input text
    sample_input_text = "Once upon a time, there lived a farmer in a village."
    input_text = col1.text_area("Input Text:", height=300, value=sample_input_text )

    # Create a text input for the output text
    output_text = col2.text_area("Output Text:", height=300, key="output_text")

    # Create a button to translate the text
    translate_button = st.button("Translate", on_click=translate, args=(input_text, target_language, target_audience,))
