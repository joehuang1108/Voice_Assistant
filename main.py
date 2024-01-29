
# Voice Assistant
# Take in a voice command
# Proceed with the action
# 1. Function for a timer
# 2. open music (Spotify)
# 3. open google (search)
# 4. open youtube, wikipedia, canvas
# 5. check if word is palindrome

import time
import winsound
import pygame
import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import urllib
import os

# initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# 1 for female voice 0 for male voice
engine.setProperty('voice', voices[1].id)

dict_num = {"one":1, "two":2, "three":3, "four":4, "five":5}



# Mini project #1: Building a timer
def countdown_timer(t):
    # initialize and load music file
    pygame.mixer.init()
    pygame.mixer.music.load("ring.mp3")
    # timer starts here

    if t in dict_num:
        int_t = dict_num[t]
    else:
        int_t = int(t)

    while int_t > 0:
        mins, secs = divmod(int_t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #             5:45
        print(timer)
        time.sleep(1)
        int_t -= 1
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # #             Hz,   msec
    # winsound.Beep(1000, 5000)

# countdown_timer(10)

# Mini Project #2:

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
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(query)
        return query
        # speak(query)
    except:
        print("error")
        speak("Error try again")
        return None

# speech_to_text()

# Mini project #4
# Navigate/Go-to a certain website

def web(website):
    webbrowser.open(website)

# web("spotify.com")

def google_search():
    url = "google.com/search?q="
    speak("Would you like to google search anything, please say yes or no")
    answer = speech_to_text()

    if answer == "yes":
        speak("What would you like to search? ")
        search = speech_to_text()
        search = search.replace(" ", "+")
        final_url = url + search
        webbrowser.open(final_url)
    else:
        webbrowser.open(url)

# google_search()

# Mini project #5
# Access/open a local application

def open_local_applications(application):
    if application == "Spotify":
        speak("Opening Spotify")
        loc = "Spotify location.exe"
    elif application == "Zoom":
        speak("Opening zoom")
        loc = "zoom location"

    # run file at location
    os.startfile(loc)


# Integration of functions

# 1. Listen for "Python" and activates listening for commands
# 2. Speak and prompt what the user wants to do
# 3. Take in speech command and proceed with execution accordingly

activated = False
answer = None

while True:
    while(answer != "Python"):
        answer = speech_to_text() # either returns what we said OR None

    if(answer == 'Python'):
        activated = True

    if(activated == True):
        speak("What do you want to do")
        action = speech_to_text() # either returns what we said OR None
        if action == "Youtube":
            web("youtube.com")
        elif action == "Canvas":
            web("canvas.com")
        elif action == "stop":
            activated = False
            print("stop")
        elif action == "timer":
            countdown_timer(10)





# Classes
# class Robot():
#     def __init__(self, motor1, motor2):
#         self.motor1 = motor1
#         self.motor2 = motor2
#
#     def __int__(self, motor1, motor2, motor3, motor4):
#         self.motor1 = motor1
#         self.motor2 = motor2
#         self.motor3 = motor3
#         self.motor4 = motor4
#
#     def four_motor_drive(self):
#         self.motor1.drive()
#         self.motor2.drive()
#         self.motor3.drive()
#         self.motor4.drive()
#
# robot = Robot(m1, m2) # robot is an object of class Robot
# robot.four_motor_drive()












