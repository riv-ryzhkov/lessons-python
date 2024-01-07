# pip install googletrans==4.0.0-rc1



from googletrans import Translator

# create an instance of the Translator class
translator = Translator()

# the text to be translated
text_to_translate = "Привет, как дела?"

# use the translate method to translate the text
translated_text = translator.translate(text_to_translate, src='ru', dest='en')

# print the translated text
print(translated_text.text)




# from googletrans import Translator
#
# translator = Translator()
# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
#
# print(result.src)
# print(result.dest)
# print(result.text)


# import googletrans

# print(*googletrans.LANGUAGES, sep='\n')

# from googletrans import Translator
#
# translator = Translator()
# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
#
# print(result.src)
# print(result.dest)
# print(result.text)