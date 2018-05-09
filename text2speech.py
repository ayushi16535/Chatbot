from gtts import gTTS

tts= gTTS (text='Hello everyone. Good Morning, Smita Mam. How are you today.', lang='en')

tts.save("Good2.mp3")
