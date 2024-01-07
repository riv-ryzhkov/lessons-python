# pip install SpeechRecognition
######################################################### pip install pipwin         No
######################################################### pipwin install pyaudio

import speech_recognition


sp = speech_recognition.Recognizer()
sp.pause_threshold = 0.5

def listen_voice():
    print('.' * 80)
    print('Скажіть щось, а я напишу те, що зрозумів...\n')
    try:
        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(source=mic, duration=0)
            audio = sp.listen(source=mic)
            # query = sp.recognize_google(audio_data=audio, language='uk-UA', show_all=True)
            query = sp.recognize_google(audio_data=audio, language='uk-UA')
            # query = sp.recognize_google(audio_data=audio, language='fr-FR').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Я не зрозумів. Повторіть, будь ласка.'


def run():
    voice = listen_voice()
    print(voice)
    return voice


if __name__ == "__main__":
    answer = ' '
    while answer != 'зупинись':
        answer = run()
    print('=' * 80)
    print('STOP PROGRAM!')

