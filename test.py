import speech_recognition as sr
import pyttsx3
import musiclibrary
import webbrowser
import requests

if __name__ == "__main__":
    speak("Initializing nova...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'nova'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)
            print(f"[DEBUG] Heard word: '{word}'")

            if "nova" in word.lower():
                print("wake word detected") #dignostic
                speak("Yes sir...") #speak
                

                with sr.Microphone() as source:
                    print("Listening for your command...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                    command = recognizer.recognize_google(audio)
                    processcommand(command)

        except      sr.WaitTimeoutError:
                    print("Timeout — no voice input detected.")
        except      sr.UnknownValueError:
                    print("Could not understand audio.")
                    speak("Sorry, I didn't catch that...")
        except      sr.RequestError as e:
                    print("API Error:", e)
                    speak("There was a problem with the speech service.....")
        except      Exception as e:
                    print("Error:", e)


  