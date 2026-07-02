from translate import Translator


translator = Translator(to_lang="es")  # Spanish

text = "Hello, how are you?"

translation = translator.translate(text)

print("Translated Text:", translation)