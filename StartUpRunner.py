import os
def poe():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Grinding Gear Games\Path of Exile")
def skill_tree():
    os.startfile("C:\Program Files (x86)\PoESkillTree - Ascendancy\PoESkillTree")
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
    if command == "poe":
        poe()
    elif command == "skill tree":
        skill_tree()
    elif command == "spotify":
        spotify()
    elif command == "media keys":
        media_keys()
    elif command == "skype":
        skype()
    elif command == "lol":
        lol()
