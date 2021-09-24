#!/usr/bin/env python3
# Author : Nitesh Singh
"""
translate between english and french
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))
def english_to_french(english_text):
    """
    translate english to french
    """
    if english_text is None:
        return None
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
def french_to_english(french_text):
    """
    translate french to english
    """
    if french_text is None:
        return None
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
#print("English-to-french : "+english_to_french("Hello, how are you today?"))
#print("French-to-English : "+french_to_english("Bonjour, comment vous êtes aujourd'hui?"))


#ibmcloud target --cf-api https://api.eu-gb.cf.cloud.ibm.com -r eu-gb -o theniteshsingh@gmail.com