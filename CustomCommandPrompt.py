import time
import sys
import keyboard
import winsound
import pyttsx3
import os
import traceback
from itertools import cycle
from datetime import datetime
from os import *
from keyboard import *
from sys import *

Running = True
CommandTotal = "9"

engine = pyttsx3.init()
engine.runAndWait()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

    

def sys(command):
    syscmd  = system(command)

sys("color 9")
sys("cls")

def cls():
    
    if name == 'nt':
        _ = system('cls')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def beep():
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)



print("Welcome to custom CMD user type help to see all the command type quit to exit")
sys("pause")
cls()
while Running:
#   INPUT
    try:
        command = ''    
        cmd = input(">")
    except KeyboardInterrupt:
        sys("color 0F")
        sys("cls")
        break
    except EOFError:
        sys("color 0f")
        sys("cls")
        break
    
#   COMMAND

    if cmd == "status":
        test = "Hi"
        print("|--------------------------------------")
        print(f"|Running: [{Running}]")
        print(f"|Command: [{CommandTotal}]")
        print("|--------------------------------------")

    if cmd == "time":
        print(f"Current time is [{current_time}]")

    if cmd == "say":
        word = input("Word? ")
        speak(word)


    if cmd == "beep":
        print("Beep!")
        beep()
        
    if cmd == "sysc":
        syscm = input("Command? ")
        sys(syscm)
    if cmd == "cls":
        cls()
    if cmd == "help":
        print(command)

        
#   CONFIGURATION   

    if cmd == 'quit':
        print("Closed")
        cls()
        sys("color 0F")
        Running = False
        
