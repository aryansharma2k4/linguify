import os
from google import genai
from dotenv import load_dotenv

def enhance_translation(machineTranslatedText: str, originalText: str, originalLang: str, targetLang: str):
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(
        api_key=gemini_api_key,
    )


    prompt = f"""
        You are a highly skilled translator with over 40 years of experience in {originalLang} and {targetLang}. You possess a deep understanding of both cultures and are adept at conveying not just the literal meaning, but also the nuances, intent, and emotional tone of the original text. You excel at identifying and adapting idioms, slang, and cultural references to ensure the translated text feels natural and authentic to a native speaker of {targetLang}.
        Your task is to improve the following translation from {originalLang} to {targetLang}:
        Original Text: {originalText}
        Machine Translation: {machineTranslatedText}
        Carefully analyze the original text and the existing translation. Identify any areas where the translation is awkward, unnatural, or fails to capture the true meaning or intent. Revise the translation to be as natural and authentic as possible, using appropriate idioms, slang, and cultural references where necessary. Consider the context and the intended audience when making your revisions.
        Your output should be ONLY the improved, more authentic translation. Do not include any introductory phrases, explanations, or conversational elements. Provide ONLY the final, translated text.
        """

    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=prompt
    )

    return response.text
