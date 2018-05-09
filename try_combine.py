#!/usr/bin/env python2.7

# Requires PyAudio and PySpeech. time.sleep(100)

import time 
from gtts import gTTS
import os
import speech_recognition as sr

 

# Record Audio

r = sr.Recognizer()
localtime = time.localtime(time.time())

with sr.Microphone(device_index=3) as source:
    start = gTTS("Say something!",lang='en')
    start.save("start.mp3")
    
    while(1):
        os.system("mpg321 start.mp3")
        print("Say something!")

        audio = r.listen(source,phrase_time_limit=5)

 

# Speech recognition using Google Speech Recognition

        try:
    
    # for testing purposes, we're just using the default API key

    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

    # instead of `r.recognize_google(audio)`
    
            sentence = r.recognize_google(audio)
            print("You said: " + sentence)
            word1 ='hello'
            word2 ='hey'
            word3 ='hi'
            word4 ='name'
            word5 ='developer'
            word6 ='developed'
            hour = localtime.tm_hour + localtime.tm_min/60
            if hour < 12:
                wish = "Hello, Everyone. Good Morning"
            else:
                wish = "Hello, Everyone. Good Afternoon"
            
            tts= gTTS (wish, lang='en')

            tts.save("wish.mp3")

            tts1= gTTS ("My Name is Anex", lang='en')

            tts1.save("name.mp3")
            
            tts2= gTTS ("I have been developed by Anshu Bharti and Ayushi Jain under the guidance of Dr. Smita Naval. Currently I am in my beta version.", lang='en')

            tts2.save("developer.mp3")

            if word1 in sentence:
            
                os.system("mpg321 wish.mp3")
            elif word2 in sentence:
            
                os.system("mpg321 wish.mp3")
            elif word3 in sentence:
            
                os.system("mpg321 wish.mp3")
            elif word4 in sentence:
            
                os.system("mpg321 name.mp3")
            elif word5 in sentence:
            
                os.system("mpg321 developer.mp3")
            elif word6 in sentence:
            
                os.system("mpg321 developer.mp3")
            elif "exit" in sentence:
                break             
		
        except sr.UnknownValueError:

            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:

            print("Could not request results from Google Speech Recognition service; {0}".format(e))


