#importing all required libraries
from time import sleep
import os
import json
SAVE_PATH = "save.json"
#startup logo
def startup_logo():
    print("""
  ____             _       _               _     
 |  _ \           | |     | |             (_)    
 | |_) | __ _ _ __| |_ ___| | __ __      ___ ___ 
 |  _ < / _` | '__| __/ _ \ |/ / \ \ /\ / / / __|
 | |_) | (_| | |  | ||  __/   <   \ V  V /| \__ |
 |____/_\__,_|_|__ \__\___|_|\_\   \_/\_/ |_|___/
  / ____|      / _| |                            
 | (___   ___ | |_| |___      ____ _ _ __ ___    
  \___ \ / _ \|  _| __\ \ /\ / / _` | '__/ _ \   
  ____) | (_) | | | |_ \ V  V / (_| | | |  __/   
 |_____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|   
                                                                                 
    """)
#startup
def startup():
    startup_logo()
    print("Please wait.\nLoading")
    sleep(0.25)
    console_clear()
    startup_logo()
    print("Please wait.\nLoading.")
    sleep(0.25)
    console_clear()
    startup_logo()
    print("Please wait.\nLoading..")
    sleep(0.25)
    console_clear()
    startup_logo()
    print("Please wait.\nLoading...")
    sleep(0.25)
    console_clear()
    main_menu()

#used to quickly clear the console
def console_clear():
    if os.name == "nt": #windows
        os.system("cls")
    else: #macOS and linux
        os.system("clear")

def first_time():
    print("Hi!")
    sleep(0.1)
    print("\nIt looks like it's your first time playing.")
    sleep(0.25)
    print("\nDon't worry, the game is very easy.")
    sleep(0.25)
    print("\nBefore you start playing, please choose your language:")
    print("1. English\n2. Polish")
    wybor = str(input("Please input the language of your choice: "))
    if wybor.lower == "english" or "angielski" or "1":
        pass
    if wybor.lowr == "polish" or "polski" or "2":
        pass
def main_menu():
    pass
    
    
def game():
    pass

startup() #starting animation