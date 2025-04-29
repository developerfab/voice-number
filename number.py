from gtts import gTTS
from pygame import mixer

import os
import random
import sys

print(" ------------------------------")
print("| Welcome to guess the number  |")
print(" ------------------------------")
print("| The idea is that you will    |")
print("| listen a number and you      |")
print("| write it, if you guess you   |")
print("| can continue with the next.  |")
print("| You have 3 lives, if you lost|")
print("| these you lose. Good luck    |")
print(" ------------------------------")
print("| Now please selected you level|")
print("| 1 - Easy                     |")
print("| 2 - Middle                   |")
print("| 3 - Advance                  |")
print(" ------------------------------")
level = input()
print(" Press Enter to start")
input()

if (level=='1'):
    lives = 5
elif(level=='2'):
    lives = 3
elif(level=='3'):
    lives = 1
else:
    print("Upss, you have entered an invalid value")
    sys.exit()

while(lives > 0):

    if level == '1':
        number = str(random.randint(0, 100))
    elif level == '2':
        number = str(random.randint(0, 5000))
    else:
        number = str(random.randint(0, 100000))

    language = 'en'

    audio = gTTS(text=number, lang=language, slow=False)
    audio.save("number.mp3")

    mixer.init()
    mixer.music.load('./number.mp3')
    mixer.music.play()
    os.remove("number.mp3")
    i = input("what number did you listen?")
    if (i == number):
        print("Congratulations that was the number")
    else:
        print("Sorry :( It's wrong")
        lives = lives - 1
        print("Now you have " + str(lives) + " lives")
