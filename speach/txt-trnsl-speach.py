# pip install google-cloud-translate
# pip install google-cloud-texttospeech


import os
from google.cloud import texttospeech_v1beta1 as texttospeech
from google.cloud import translate_v2 as translate
import pyttsx3

# Set up the translation and text-to-speech clients
translate_client = translate.Client()
texttospeech_client = texttospeech.TextToSpeechClient()

# Set the input text in Russian
input_text = "Привет, как дела?"

# Translate the input text to English
translation = translate_client.translate(
    input_text, source_language='ru', target_language='en')['translatedText']

# Synthesize the translated text into speech
synthesis_input = texttospeech.types.SynthesisInput(text=translation)
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)
response = texttospeech_client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config)

# Save the audio to a file
with open('translation.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "translation.mp3"')

# Play the audio using the pyttsx3 library
engine = pyttsx3.init()
engine.setProperty('voice', 'english-us')
engine.say(translation)
engine.runAndWait()