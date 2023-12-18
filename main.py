
# Voice Assistant
# Take in a voice command
# Proceed with the action
# 1. Function for a timer
# 2. open music (Spotify, YouTube Music)
# 3. open google (search)
# 4. open youtube

import time
import winsound
import pygame

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
# countdown_timer(5)

# Mini Project #2:

# Compare two strings to see if equal

word1 = "racecar"
word2 = "anna"
word3 = "moon"

print(word1[0])
print(len(word1))


for x in range(len(word3)):
    if word3[x] == word3[len(word3)-1-x]:
        palidrome = True
    else:
        palidrome = False
        break

print(palidrome)