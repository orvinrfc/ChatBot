from googletrans import Translator

# return the string of the translated text
def translate_text(text,target):
    translator = Translator()
    translated = translator.translate(text,src="en",dest=str(target))
    return translated.text

# print(translate_text("my name is orvin", "de"))
# print('IMDBot: ' + translate_text("Here\'s the link to the full Wikipedia page: ","ja") + "Test")