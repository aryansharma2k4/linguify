from src.translator.translate import basic_translate
from src.translator.languages import printAllChoices
from src.translator.ai_enhancer import enhance_translation



if __name__ == "__main__":
    userChoice = int(input("Enter 1: To View all the language code \nEnter 2: To enter the text\n"))
    if(userChoice == 1):
        printAllChoices()
    elif(userChoice == 2):
        userInput = str(input("Enter the text you want to translate(auto-detect): \n"))
        languageCode = str(input("Enter the language you want to translate to: \n"))
        translatedText = basic_translate(userInput, languageCode)
        finalTranslatedText = enhance_translation(translatedText, userInput, "en", languageCode)
        print(finalTranslatedText)
