# pip install googletrans==4.0.0-rc1

from googletrans import Translator
import speech_recognition
import pyttsx3


sp = speech_recognition.Recognizer()
sp.pause_threshold = 0.5

def listen_voice():
    print('.' * 80)
    print('Скажіть щось, а я напишу те, що зрозумів...\n')
    try:
        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(source=mic, duration=0)
            audio = sp.listen(source=mic)
            # query = sp.recognize_google(audio_data=audio, language='uk-UA')
            query = sp.recognize_google(audio_data=audio, language='en-US')
            # query = sp.recognize_google(audio_data=audio, language='fr-FR').lower()
        print('=' * 80)
        print(query)
        print('.'*80)
        return query
    except speech_recognition.UnknownValueError:
        return 'Я не зрозумів. Повторіть, будь ласка.'



translator = Translator()
text_to_translate = listen_voice()

translated_text = translator.translate(text_to_translate, src='en', dest='ru')

print(translated_text.text)
print('='*80)
with open('my_translate.txt', 'a') as f:
    f.write(text_to_translate + '\n')
    f.write(translated_text.text + '\n\n')


# text_trg = input('text to tell : ')
text_trg = translated_text.text

engine = pyttsx3.init()
engine.setProperty('voice', 'en')
engine.say(text_trg)
engine.runAndWait()