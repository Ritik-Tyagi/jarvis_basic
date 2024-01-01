import pyttsx3
import random

import pyaudio
import speech_recognition 
import webbrowser
import datetime
import pyjokes
import os
import time
def sptext():
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source,0,4)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio,language="en-in")
            print(data)
            return data
        except speech_recognition.UnknownValueError:
            print("Not Understande") 
def speechtx(audio):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)

    engine.say(audio)
    engine.runAndWait()
if __name__ == '__main__':
    
    #if "hi jarvis" in sptext().lower():
    while True:
        query=sptext().lower() # type: ignore
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query = sptext().lower() # type: ignore
                if "go to sleep" in query:
                    speechtx("ok sir, You can call me anytime")
                    break
                elif "hello" in query:
                    speechtx("hello sir, how are you ?")
                elif "i am fine" in query:
                    speechtx("that's great sir")
                elif "how are you" in query:
                    speechtx("perfect sir")
                elif "thank you" in query:
                    speechtx("your welcome,sir")
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchwikipedia
                    searchwikipedia(query)
                    

    #         data1= sptext().lower()
    #         if "your name" in data1:
    #             name = "my name is jarvis"
    #             speechtx(name)
    #         elif "old are you" in data1:
    #             age="i am two years old"
    #             speechtx(age)
    #         elif "time" in data1:
    #             time = datetime.datetime.now().strftime("%I%M%p")
    #             speechtx(time)
    #         elif "youtube" in data1:
    #             webbrowser.open("https://www.youtube.com/")
    #         elif "who are you" in data1:
    #             intro="i am a artificial intelligence"  
    #             speechtx(intro) 
    #         elif "joke" in data1:
                
    #             joke_1=pyjokes.get_joke(language="en",category="neutral")
    #             print(joke_1)
    #             speechtx(joke_1) 
    #         elif "play song" in data1:     
    #             add="D:\punjabi video songs"
    #             listsong=os.listdir(add)
    #             print(listsong)
    #             os.startfile(os.path.join(add,random.choice(listsong)))
    #         elif "introduction" in data1 or "intro" in data1 :
    #             intro="my name is jarvis and i am an ai tool" 
    #             speechtx(intro)  
    #         elif  "exit" in data1:
    #             speechtx("thank you")
    #             break 
    #         time.sleep(5)
    # else:           
    #     print("thanks")