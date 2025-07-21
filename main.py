import speech_recognition as sr
import pyttsx3
import musiclibrary
import webbrowser
import requests

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    print(f"[nova speaking]: {text}")
    engine.say(text)
    engine.runAndWait()

    # News function
def get_news():
    api_key = "7b781710553a4f20ab9164d56daaf63c"  
    url= requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=7b781710553a4f20ab9164d56daaf63c")

    try:
        response = requests.get(url)
        news_data = response.json()

        if news_data.get("status") != "ok":
            speak("Sorry, I couldn't fetch the news.")
            return

        articles = news_data.get("articles", [])[:5]  # Top 5 headlines
        if not articles:
            speak("No news found at the moment.")
            return

        speak("Here are the top headlines:")
        for i, article in enumerate(articles, 1):
            headline = article['title']
            print(f"{i}. {headline}")
            speak(headline)

    except Exception as e:
        print("Error fetching news:", e)
        speak("Something went wrong while fetching the news.")


# Command processor
def processcommand(c):
    print("Command received:", c)
    speak(f"You said: {c}")
    # Example action
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open Linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com")

    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "").strip()
    
        # Optional: print to check
        print(f"Song requested: {song}")
        link = musiclibrary.music.get(song)

        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song '{song}' in your music library.")

    elif "news" in c.lower() or "headlines" in c.lower():
        speak("Fetching the latest news for you.")
        get_news()

    else:
        speak("Sorry, I don't know how to do that yet.")

    


# MAIN PROGRAM
if __name__ == "__main__":
    speak("Initializing nova...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'nova'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)
            if (word.lower()== "nova"):
                speak("Yes sir...")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processcommand(command)

        except      sr.WaitTimeoutError:
                    print("Timeout — no voice input detected.")
                    speak("Timeout....")
        except      sr.UnknownValueError:
                    print("Could not understand audio.")
                    speak("Sorry, I didn't catch that...")
        except      sr.RequestError as e:
                    print("API Error:", e)
                    speak("There was a problem with the speech service.....")
        except      Exception as e:
                    print("Error:", e)
