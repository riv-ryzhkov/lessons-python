import speech_recognition
import pyttsx3
from googletrans import Translator

# Speech recognition (English)
sp = speech_recognition.Recognizer()
sp.pause_threshold = 0.5

def listen_voice():
    print('.' * 80)
    print('Скажіть українською те, що бажаєте перекласти...\n')
    try:
        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(source=mic, duration=0)
            audio = sp.listen(source=mic)
            # query = sp.recognize_google(audio_data=audio, language='uk-UA', show_all=True)
            query = sp.recognize_google(audio_data=audio, language='uk-UA')
            # query = sp.recognize_google(audio_data=audio, language='en-US')
            # query = sp.recognize_google(audio_data=audio, language='fr-FR').lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Нажаль, я плохо вас зрозумів..."

text_src = listen_voice()


# create an instance of the Translator class
translator = Translator()

# the text to be translated
text_to_translate = text_src

# use the translate method to translate the text
translated_text = translator.translate(text_to_translate, src='uk', dest='fr')

# print the translated text
print(translated_text.text)


# Speaking translation in Russian

# text_ru = 'Слава Украине!'
text_trg = translated_text.text
engine = pyttsx3.init()
engine.setProperty('voice', 'fr')
# with open('myfile.txt', 'a', encoding='utf-8') as file:
with open('myfile.txt', 'a') as file:
     file.write(text_src + '\n')
     file.write(text_trg + '\n\n')
engine.say(text_trg)
engine.runAndWait()
