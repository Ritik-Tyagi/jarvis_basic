# Jarvis - A Voice-Activated AI Assistant

Jarvis is a Python-based AI assistant that leverages speech recognition and text-to-speech technologies to perform tasks such as web searches, responding to user queries, telling jokes, and more.

## Features
- **Voice Activation**: Wake up the assistant with the command "wake up".
- **Speech Recognition**: Understands and processes voice commands using Google's Speech Recognition API.
- **Text-to-Speech**: Responds to user queries with a natural-sounding voice using the `pyttsx3` library.
- **Task Execution**:
  - Opens websites like Google, YouTube, and Wikipedia.
  - Provides time updates and tells jokes.
  - Plays random songs from a specified directory.
  - Introduces itself and provides basic conversational responses.

## Requirements
To run this project, ensure you have the following Python libraries installed:
- `pyttsx3`
- `speech_recognition`
- `pyaudio`
- `pyjokes`
- `webbrowser`
- `os`
- `datetime`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jarvis-assistant.git
   cd jarvis-assistant
2. pip install pyttsx3 speechrecognition pyaudio pyjokes
3. python jarvis.py



## Say "wake up" to activate Jarvis. You can use commands like:

"Hello"
"Google <search query>"
"YouTube <search query>"
"Wikipedia <search query>"
"Tell me a joke"
"Play a song"
"Go to sleep"
