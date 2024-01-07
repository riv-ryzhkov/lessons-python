import speech_recognition
import requests
import pyttsx3
from myAPI import myAPI


# Speech recognition (French)
sp = speech_recognition.Recognizer()
sp.pause_threshold = 0.5

def listen_voice():
    print('.' * 80)
    print('Dites quelque chose que vous voulez traduire...\n')
    try:
        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(source=mic, duration=0)
            audio = sp.listen(source=mic)
            query = sp.recognize_google(audio_data=audio, language='fr-FR').lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Je suis désolé, je t'ai mal compris..."


text_fr = listen_voice()

# Translattion French to Russian
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
source = 'fr'
target = 'ru'
payload = 'q={}&target={}&source={}'.format(text_fr, target, source)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': myAPI
    }

response = requests.request("POST", url, data=payload, headers=headers)
translate_res = response.json()
print(translate_res)
# translated_text = translate_res["data"]["translations"][0]["translatedText"]
translated_text = translate_res["alternative"][0]["transcript"]
print(translated_text)

# Speaking translation in Russian

# text_ru = 'Слава Украине!'
text_ru = translated_text
engine = pyttsx3.init()
engine.setProperty('voice', 'ru')
with open('myfile.txt', 'a', encoding='utf-8') as file:
     file.write(text_fr + '\n')
     file.write(text_ru + '\n\n')
engine.say(text_ru)
engine.runAndWait()
