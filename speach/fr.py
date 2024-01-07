# import pyttsx3
#
# # Initialize the text-to-speech engine
# engine = pyttsx3.init()
#
# print(*dir(engine), sep='\n')
# # Set the French voice
# voices = engine.getProperty('voices')
# print(*voices, sep='\n')
# # french_voice = None
# # for voice in voices:
# #     if voice.languages[0] == 'fr-fr':
# #         french_voice = voice.id
# #         break
# # if french_voice is None:
# #     raise Exception('French voice not found')
# # engine.setProperty('voice', french_voice)
# #
# # # Set the speaking rate and volume
# # engine.setProperty('rate', 180) # adjust to change speaking rate
# # engine.setProperty('volume', 1.0) # adjust to change volume
# #
# # # Synthesize the speech
# # text = "Bonjour, comment ça va?"
# # engine.say(text)
# # engine.runAndWait()

import subprocess

# Set the speaking rate and volume
speaking_rate = 140 # adjust to change speaking rate
volume = 100 # adjust to change volume

# Synthesize the speech
text = "Bonjour, comment ça va?"
subprocess.call(['espeak', '-v', 'fr', '-s', str(speaking_rate), '-a', str(volume), text])
