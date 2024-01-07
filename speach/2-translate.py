# pip install googletrans==4.0.0-rc1



from googletrans import Translator


translator = Translator()
# print(type(translator))
# print(*dir(translator), sep='\n')
# breakpoint()
# text_to_translate = "Привіт, як справи?"
# text_to_translate = "Привет, как дела?"
# text_to_translate = "How are you!"
text_to_translate = input('text to translate : ')


translated_text = translator.translate(text_to_translate, src='en', dest='uk')

print(translated_text.text)