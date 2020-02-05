#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from os import system as komut


buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

def lower(text:str):
    newText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)
            newText += kucukAlfabe[index]
        
        else:
            newText += i

    return newText




# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    komut("cls")
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
flag = False

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio,language = "tr")
    print("Algılanan: " + text)
    flag = True
    text = lower(text)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
if flag:
   if text == "program çalıştır":
       komut("atom")