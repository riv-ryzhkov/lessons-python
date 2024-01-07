import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the language to Ukrainian
engine.setProperty('voice', 'ru')

# Open the file in read mode with encoding set to UTF-8
# with open('data/myfile.txt', 'r', encoding='utf-8') as file:
with open('data/myfile.txt', 'r') as file:

    # Read the contents of the file into a variable
    text = file.read()

# Read out the text using the text-to-speech engine
engine.say(text)
engine.runAndWait()




