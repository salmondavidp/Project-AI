#import Component/libreary/model
from cgitb import text
from pyexpat import model
from unittest import result
from vosk import Model, KaldiRecognizer
import json
import os
import pyaudio
import pyttsx3
from core._inher_ import SystemInfo

#speech Recg
model = Model('model')
rec = KaldiRecognizer(model, 16000)
#speech Synt
def speak(text):
    engine.say(text)
    engine.runAndWait()
engine = pyttsx3.init()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000, input=True, frames_per_buffer=8000 )
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
       result = rec.Result()
       result = json.loads(result)
       text = result['text']


       if text == 'what time is' or text == 'tell me the time':
            speak(SystemInfo.get_time())
       
    
       

    
    