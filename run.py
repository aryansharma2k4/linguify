from src.translator.translate import basic_translate

def printAllChoices():
    print("🌐 Supported Languages:")
    languages = [
        ["en", "English"],
        ["hi", "Hindi"],
        ["es", "Spanish"],
        ["fr", "French"],
        ["de", "German"],
        ["zh-cn", "Chinese (Simplified)"],
        ["zh-tw", "Chinese (Traditional)"],
        ["ja", "Japanese"],
        ["ko", "Korean"],
        ["ru", "Russian"],
        ["ar", "Arabic"],
        ["pt", "Portuguese"],
        ["it", "Italian"],
        ["nl", "Dutch"],
        ["tr", "Turkish"],
        ["bn", "Bengali"],
        ["ur", "Urdu"],
        ["ta", "Tamil"],
        ["te", "Telugu"],
        ["gu", "Gujarati"],
        ["mr", "Marathi"],
        ["pa", "Punjabi"],
        ["ml", "Malayalam"],
        ["kn", "Kannada"],
        ["as", "Assamese"],
        ["ne", "Nepali"],
        ["si", "Sinhala"],
        ["th", "Thai"],
        ["vi", "Vietnamese"],
        ["id", "Indonesian"],
        ["ms", "Malay"],
        ["sw", "Swahili"],
        ["af", "Afrikaans"],
        ["pl", "Polish"],
        ["uk", "Ukrainian"],
        ["he", "Hebrew"],
        ["fa", "Persian (Farsi)"],
        ["ps", "Pashto"],
        ["so", "Somali"],
        ["yo", "Yoruba"],
        ["zu", "Zulu"]
    ]
    for it in languages:
        print(it[0]+ " : " + it[1])


if __name__ == "__main__":
    userChoice = int(input("Enter 1: To View all the language code \nEnter 2: To enter the text"))
    if(userChoice == 1):
        printAllChoices()
    elif(userChoice == 2):
        userInput = str(input("Enter the text you want to translate: \n"))
        languageCode = str(input("Enter the language you want to translate to: \n"))
        translatedText = basic_translate(userInput, languageCode)
        print(translatedText)


