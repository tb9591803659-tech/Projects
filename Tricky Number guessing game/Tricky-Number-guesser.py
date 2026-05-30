#Targets : 1.Modes 2.Scoring system based on hints & attempmts
#  3.hints 4.timer 5.attempts 6.Menu system for mode and player entry 7.leaderboard
from colorama import Fore , Back ,Style , init
import random
import threading
import time
import json
attempts = None
timer = None
hints = 0
Time_out = False
mode = "ntg"
Game_over = False
init(autoreset=True)

def countdown():
    global timer,Time_out

    while timer > 0 and not Game_over :
        timer -= 1
        time.sleep(1)
    
    if timer == 0 :
        Time_out = True
        print(Fore.RED + "Time Over!")

    

def modes(num):
    global mode , timer , attempts 
    if num == 1 :
        mode = "Easy"
        attempts = 10
        timer = 300 #Time in seconds
        print(Fore.GREEN + "Easy mode Selected")
    elif num == 2 :
        mode = "Medium"
        attempts = 7
        timer = 180
        print(Fore.YELLOW + "Medium mode Selected")
    elif num == 3 :
        mode = "Hard"
        attempts = 5
        timer = 60
        print(Fore.RED + "Hard mode Selected")
    
    else :
        return False
    return True

def hint(target, guess):
    global hints

    hints += 1

    difference = abs(target - guess)

    if difference <= 3:
        print("Very Close")

    elif difference <= 10:
        print("Close")

    else:
        print("Far")
    

def won(Player_name,attempts,timer,hints) :
    score = 10*attempts + timer - 5*hints
    game_details = {"Player Name" : Player_name,"Attempts" : attempts,"Time taken" : timer,"hints taken": hints}
    # with open("Game_records.txt","a") as file:
    #     file.write(game_details)
    return score

def leaderboard():
    with open("Game_records.txt","r") as file:
        for line in file:
            print(line.strip()) 

while True:
    print(Fore.MAGENTA + Style.BRIGHT + "Welcome to number guessing game")
    print(Fore.YELLOW + "(1)" + Fore.WHITE + "Start Game")
    print(Fore.YELLOW + "(2)" + Fore.WHITE + "View Scoreboard")
    print(Fore.YELLOW + "(3)" + Fore.WHITE + "Exit Game")
    try:
        option = int(input(Fore.MAGENTA + Style.NORMAL + "Select Option:"))
        if option == 1 :
            Player_name = input(Fore.MAGENTA + "Enter name:")
            print(Fore.MAGENTA + Style.NORMAL + "Select Difficulty:")
            print("[1]" , Fore.GREEN + "Easy")
            print("[2]" , Fore.YELLOW + "Medium")
            print("[3]" , Fore.RED + "Hard") 
            try:
                Mode = int(input(Fore.MAGENTA + Style.DIM + "Select which mode:"))
                if not modes(Mode) :
                    print(Fore.RED + "Invalid Selection")
                    continue
                if Mode == 1:
                    target = random.randint(1,10)
                elif Mode == 2 :
                    target = random.randint(1,50)
                elif Mode == 3 :
                    target = random.randint(1,100)
                else:
                    print(Fore.RED + Style.BRIGHT +  "Invalid mode")
                    continue
                tries = 0

                time_thread = threading.Thread(target=countdown)
                time_thread.start()

                while attempts > 0 and not Time_out :
                    try:
                        guess = int(input("Guess the number: "))
                        
                        #logic
                        if guess == target:
                            print(Fore.GREEN + "Congrads,it is correct guess")
                            score = won(Player_name,attempts,timer,hints)
                            print(Fore.MAGENTA + f"Your Score = {score}")
                            break
                        elif guess < target:
                            print("Higher")
                        else :
                            print("Lower")
                        print(Fore.CYAN + f"Time Left = {timer}")
                        attempts -= 1
                        tries += 1

                    except Exception as e:
                        print(e)
                
                
            except Exception as e :
                print(e)
                    
        if option == 2 :
            leaderboard()

        if option == 3 :
            print(Fore.YELLOW + "Exiting Game...")
            print(Fore.GREEN + "Exited Game Succesfully.") 
            break      

            
    except Exception as e:
        print(e)