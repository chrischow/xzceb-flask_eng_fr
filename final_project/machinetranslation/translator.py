#!/usr/bin/env python3.6

"""
This module contains functions for translating English and French for
the Python Project for AI & Application Development Course.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create instance
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Translate english to french
def english_to_french(english_text):
    """
    Convert English text to French.
    """
    try:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
    except ValueError:
        return None

    return french_text.get('translations')[0].get('translation')

# Translate french to english
def french_to_english(french_text):
    """
    Convert French text to English.
    """
    try:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
    except ValueError:
        return None
    return english_text.get('translations')[0].get('translation')
