import os
def poe():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Grinding Gear Games\Path of Exile")
def spotify():
    os.startfile("C:\Users\lwree\AppData\Roaming\Spotify\Spotify")
def media_keys():
    os.startfile("C:\Users\lwree\Desktop\Media Keys.ahk")
def skype():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Skype\Skype")
def lol():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\League of Legends\League Of Legends")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
running = True
while(running == True):
    command = raw_input("-->")
    if command == "path of exile" or "poe":
        poe()
    if command == "spotify":
        spotify()
    if command == "media keys":
        media_keys()
    if command == "skype":
        skype()
    if command == "league of legends" or "lol":
        lol()
