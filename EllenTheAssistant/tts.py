import pip
pip.main(['install', 'requests'])

from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import mpg123
import pyaudio
import playsound
import random
import time
from weather import Weather, Unit


def talkToMe(audio):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = str(r2)+"randomtext"+str(r1) +".mp3"
    print(audio)
    tts = gTTS(text=audio, lang='en-AU') #gb
    tts.save(randfile)
    playsound.playsound(randfile, False)
    os.remove(randfile)

#Commands

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        #print("I am ready for your next command!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        r.sample_rate=48000
        r.chunk_size= 2048
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language = "en-us", show_all=False)
            print("You said: " + command + '/n')
        except sr.UnknownValueError:
            #command = r.recognize_google(audio, language = "en-us", show_all=False)
            return myCommand()
            
        return command

#ifs
def assistant(command):
    
    if 'Olivia open the python subreddit' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = 'https://new.reddit.com/r/Python/'
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        talkToMe('yes sir, Opening r slash python')
    
    if 'Olivia search' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = "https://www.google.com/search?q=" + command.replace("Olivia search", " ")
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        talkToMe('yes sir, searching ' + command.replace("Olivia search", " "))

    if "what's up Olivia" in command:
        talkToMe('Just chillin in the cold depths of a command promt')
        
    if "Olivia what's up" in command:
        talkToMe('Just chillin in the cold depths of a command promt')

    if 'Olivia terminate' in command:
        talkToMe('Terminating')        
        time.sleep(1)
        exit()

    if "Olivia what's the weather" in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = "https://www.yahoo.com/news/weather/"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        talkToMe('Opening Yahoo weather')

while True:
    assistant(myCommand())
            



