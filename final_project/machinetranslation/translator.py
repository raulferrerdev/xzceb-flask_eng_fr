"""Module for language translation using IBM Watson."""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apiKey']
URL = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(version=VERSION, authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """Translates English text to French."""
    if not english_text:
        raise ValueError('Input text is empty')
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation

def french_to_english(french_text):
    """Translates French text to English."""
    if not french_text:
        raise ValueError('Input text is empty')
    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation = translation_response.get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation
