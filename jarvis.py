    
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init

init(autoreset=True)

def translate_hindi_to_english(text):
    return translate(text, "en")

def speech_to_text():

    recognizer = sr.Recognizer()

    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 3000

    with sr.Microphone() as source:

        print(Fore.GREEN + "Listening...")

        recognizer.adjust_for_ambient_noise(source)

        try:

            audio = recognizer.listen(source)

            print(Fore.YELLOW + "Recognizing...")

            recognizer_text = recognizer.recognize_google(
                audio,
                language="hi-IN"
            ).lower()

            print("Hindi :", recognizer_text)

            trans_text = translate_hindi_to_english(
                recognizer_text
            )

            print(Fore.BLUE + "English :", trans_text)

            return trans_text

        except sr.UnknownValueError:

            print("Could not understand audio")

        except sr.RequestError as e:

            print("Request Error:", e)

speech_to_text()