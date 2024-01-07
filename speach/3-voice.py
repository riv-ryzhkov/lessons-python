# pip install pyttsx3


import pyttsx3


# text_trg = input('text to tell : ')
text_trg = 'Слава Украине!'

engine = pyttsx3.init()
# print(type(engine))
# print(*dir(engine), sep='\n')
# breakpoint()
engine.setProperty('voice', 'ru')
engine.say(text_trg)
engine.runAndWait()