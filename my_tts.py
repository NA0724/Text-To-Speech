from gtts import gTTS

import os

fn=open("text.txt","r")
text=fn.read().replace("\n"," ")
speech=gTTS(text, lang='en-US')
speech.save("TTS.mp3")

os.system("start TTS.mp3")