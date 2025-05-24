from translate import Translator

def basic_translate(text: str, code: str) -> str:
    #the code goes here
    translator = Translator(to_lang=code)
    translation = translator.translate(text)
    return translation

