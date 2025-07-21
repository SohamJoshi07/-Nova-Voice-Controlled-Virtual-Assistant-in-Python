🎙️ Nova: Voice-Controlled Virtual Assistant in Python
Nova is a simple yet effective voice-controlled personal assistant built in Python. It uses speech recognition and text-to-speech to interact with users, process commands, and perform actions like opening websites, playing music, and reading out the latest news.

🔧 Features
Wake Word Activation: Listens for the wake word "nova" to start interaction.
Speech Recognition: Converts your voice commands to text using Google's speech recognition.
Text-to-Speech (TTS): Responds back using a natural-sounding voice via pyttsx3.
News Reader: Fetches and reads top headlines using NewsAPI.
Music Playback: Plays predefined songs via YouTube links from the local musiclibrary.py.
Web Control: Opens commonly used websites like Google, YouTube, Facebook, etc.

📁 Files Overview
main.py – The core logic and infinite listening loop that powers Nova.
musiclibrary.py – A simple dictionary mapping song names to YouTube URLs.
test.py – A diagnostic/testing version of the main script for debugging and iterative development.

▶️ Getting Started
Requirements:
Python 3.x
speechrecognition, pyttsx3, requests, pyaudio (for mic input)

Install dependencies:
bash
Copy
Edit
pip install speechrecognition pyttsx3 requests pyaudio

Run the assistant:
bash
Copy
Edit
python main.py

📌 Note
Update the API key in main.py with your own NewsAPI key.
Make sure your microphone is enabled and accessible.


