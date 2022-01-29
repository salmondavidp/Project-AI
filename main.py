#import Component/libreary/model
from asyncore import read
from cgitb import text
from cmath import inf
from distutils.log import info
from pickle import TRUE
import pywhatkit
from pyexpat import model
import queue
import string
import webbrowser
from unittest import result
import pywhatkit
from vosk import Model, KaldiRecognizer
import wikipedia
import json
import os
import pyaudio
import pyttsx3
from selenium import webdriver 
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
voices = engine.getProperty('voices')

#open mic 
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000, input=True, frames_per_buffer=8000 )
stream.chunk=1024 #this will break in chunks
stream.start_stream()

def Hello():
     speak("hello sir I am your desktop assistant. Tell me how may I help you")

def Take():
     Hello()
if __name__ == '__main__':
     Take()

while TRUE:

    data = stream.read(stream.chunk,exception_on_overflow=False) 
 
    if rec.AcceptWaveform(data):
       result = rec.Result()
       result = json.loads(result)
     
       text= result['text'] 
       print(result)
       
       

       #Commands
       if text == 'what is the date' or text == 'tell me the' :
            speak(SystemInfo.get_date())
          
       if text == 'what is the time' or text == 'tell me' :
            speak(SystemInfo.get_time()) 
            
       if text == 'open google chrome' or text == 'run chrome'  :
            speak('Openng google chrome') 
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
   
       if text == 'what is your name' or text == 'tell me your name':
            speak('My name is Mads')           

       if 'mad play' in text:
            song = text.replace('mad play','')
            speak('playing'+ song) 
            print(song)
            pywhatkit.playonyt(song)   

       if 'what is' in text:
          ask = text.replace('what is','')
          info= wikipedia.summary(ask,1)
          speak(info)              