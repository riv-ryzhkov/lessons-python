# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio

import speech_recognition
import random


words = 'Adresse,chef,hôtel,monsieur,restaurant,Arbitre,couloir,jury,merci beaucoup,' \
        'surprise,Bar,diplomate,kiosque,métro,taxi,Bistrot,ensemble,kilo,naїf,' \
        'téléphone,Bureau,festival,luxe,opéra,uniforme,Chantage,film,madame,' \
        'passeport,université,Charme,girafe,mademoiselle,radio,visa'
words = words.split(',')

count_of_phrases = 0
count_of_errors = 0

sp = speech_recognition.Recognizer()
sp.pause_threshold = 0.5

def listen_voice():
    try:
        print('.' * 80)
        phrase = random.choice(words)
        print('Почитайте виразно фразу:       ' + phrase)
        print('.' * 80)
        print('і чітко її промовте.')
        phrase = phrase.lower()
        print()
        print('Якщо готові, введіть "Y", натисніть <ENTER> і через паузу промовляйте...')
        a = input('Якщо хочете завершити работу з програмою, введіть "N" :')
        if a.lower() != 'y' and a.lower() != 'н':
            return 'finir'
        global count_of_phrases
        global count_of_errors
        count_of_phrases += 1

        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(source=mic, duration=0)
            audio = sp.listen(source=mic)
            # query = sp.recognize_google(audio_data=audio, language='uk-UA').lower()
            query = sp.recognize_google(audio_data=audio, language='fr-FR').lower()
        print('='*80)
        if query == phrase:
            print('Дуже добре! Я Вас зрозумів вірно! Ви промовили:\t\t', query.upper())
            print('.' * 80)
            print('Давайте перейдемо до наступної фрази. Ваш поточний результат:')
            print('Кількість використаних фраз =', count_of_phrases)
            print('Кількість помилок =', count_of_errors)
        else:
            count_of_errors += 1
            print("Нажаль НЕ ВІРНО. Це дуже схоже на \t\t\t", query.upper())
            print('.' * 80)
            print("Давайте продовжим заняття. Ваш поточний результат:")
            print('Кількість використаних фраз =', count_of_phrases)
            print('Кількість помилок =', count_of_errors)
        print('=' * 80)
        return query
    except speech_recognition.UnknownValueError:
        count_of_phrases -= 1
        print('Нажаль я Вас зовсім не зрозумів. Давайте ще спробуємо...')
        return 'Нажаль я Вас зовсім не зрозумів.((('


def run():
    voice = listen_voice()
    # print(voice)
    return voice


if __name__ == "__main__":
    answer = ' '
    while answer != 'finir':
        answer = run()
    print('=' * 80)
    print('Ваш остаточний результат:')
    print('Кількість використаних фраз =', count_of_phrases)
    print('Кількість помилок =', count_of_errors)
    print('=' * 80)
    print('Работу з програмою закінчено!')

