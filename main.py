
# Voice Assistant
# Take in a voice command
# Proceed with the action
# 1. Function for a timer
# 2. open music (Spotify, YouTube Music)
# 3. open google (search)
# 4. open youtube
# 5. check if word is palindrome

import time
import winsound
import pygame
import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser

# initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# 1 for female voice 0 for male voice
engine.setProperty('voice', voices[1].id)

# Mini project #1: Building a timer
def countdown_timer(t):
    # initialize and load music file
    pygame.mixer.init()
    pygame.mixer.music.load("ring.mp3")
    # timer starts here
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #             5:45
        print(timer)
        time.sleep(1)
        t -= 1
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # #             Hz,   msec
    # winsound.Beep(1000, 5000)

# countdown_timer(10)

# Mini Project #2:

# Compare two strings to see if equal

# Create a program to check if a word is a palindrome
def check_palidrome(word):
    for x in range(int(len(word)/2)):
        if word[x] == word[len(word)-1-x]:
            palindrome = True
        else:
            palindrome = False
            break
    print(palindrome)

# check_palidrome("regerg")


# Mini project #3
# Convert speech to text and return text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("Hello World")
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(query)
    except:
        print("error")
        speak("Error try again")

# speech_to_text()

# Mini project #4
# Navigate/Go-to a certain website

def web(website):
    webbrowser.open(website)

web("google.com")

