import speech_recognition as sr
from googletrans import Translator
import codecs

source_lang = "fr"
dest_lang = "en"

timeout = None
sample_rate = 16000

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Function to recognize speech and translate it
def recognize_and_translate():
    try:
        # Record audio from the microphone
        with sr.Microphone(sample_rate=sample_rate) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=timeout)

        # Recognize the speech using Google Web Speech API
        recognized_text = recognizer.recognize_google(audio, language=source_lang)  # Replace with your language code, e.g., "en-US" for English

        # Translate the recognized text to the desired language
        translated_text = translator.translate(recognized_text, dest=dest_lang)  # Replace with the target language code

        # Write the original and translated text to an output file
        with codecs.open("output.txt", "w", "utf-8") as file:
            file.write(translated_text.text + "\n")

        print("Original Text:", recognized_text)
        print("Translation:", translated_text.text)

    except sr.WaitTimeoutError:
        print("Audio timeout.")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    while True:
      recognize_and_translate()