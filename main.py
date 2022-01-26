#import Component/libreary/model
from asyncore import read
from cgitb import text
from cmath import inf
from pickle import TRUE
from pyexpat import model
import queue
import string
import webbrowser
from unittest import result
from vosk import Model, KaldiRecognizer
import json
import os
import pyaudio
import pyttsx3
from core import SystemInfo
from threading import Event
import time

#speech Recg
model = Model('model')
rec = KaldiRecognizer(model, 16000)
#speech Synt

#listener
def speak(text):
    engine.say(text)
    engine.runAndWait()
engine = pyttsx3.init()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000, input=True, frames_per_buffer=8000 )
stream.chunk=1024 #this will break in chunks
stream.start_stream()

while TRUE:
    data = stream.read(stream.chunk,exception_on_overflow=False) #infinity aya ba 
    ##if  len(data) == 0 :
      ##break
    
    if rec.AcceptWaveform(data):
       result = rec.Result()
       result = json.loads(result)
       print(result)
       text= result['text']
       
       

       

       #Commands


       if text == 'what is the date' or text == 'tell me the' :
            speak(SystemInfo.get_date())
          
       if text == 'what is the time' or text == 'tell me' :
            speak(SystemInfo.get_time()) 
            
       if text == 'open chrome' or text == 'run chrome'  :
            speak('Openng google chrome') 
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            
       if text == 'what is your name' or text == 'tell me your name':
            speak('My name is __')
            