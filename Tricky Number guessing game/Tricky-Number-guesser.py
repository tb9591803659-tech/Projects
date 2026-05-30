from colorama import Fore, Style, init
import random
import threading
import time
import json
import os

init(autoreset=True)

# ---------------- GLOBAL VARIABLES ---------------- #

attempts = 0
timer = 0
hints_used = 0

time_out = False
game_over = False

mode = "None"

# ---------------- TIMER ---------------- #

def countdown():
    global timer, time_out, game_over

    while timer > 0 and not game_over:
        time.sleep(1)
        timer -= 1

    if timer <= 0 and not game_over:
        time_out = True
        print(Fore.RED + "\n⏰ TIME OVER!")


# ---------------- RESET GAME ---------------- #

def game_reset():
    global attempts, timer, hints_used
    global time_out, game_over, mode

    attempts = 0
    timer = 0
    hints_used = 0

    time_out = False
    game_over = False

    mode = "None"


# ---------------- MODES ---------------- #

def modes(choice):
    global mode, attempts, timer

    if choice == 1:
        mode = "Easy"
        attempts = 10
        timer = 300

    elif choice == 2:
        mode = "Medium"
        attempts = 7
        timer = 180

    elif choice == 3:
        mode = "Hard"
        attempts = 5
        timer = 60

    else:
        return False

    print(Fore.GREEN + f"{mode} Mode Selected!")
    return True


# ---------------- HINT SYSTEM ---------------- #

def hint(target, guess):
    global hints_used

    if hints_used >= 4:
        print(Fore.RED + "❌ No Hints Left!")
        return

    choice = input("Want Hint? (y/n): ").lower()

    if choice != "y":
        return

    hints_used += 1

    difference = abs(target - guess)

    if difference == 0:
        print(Fore.GREEN + "🎯 Exact!")
    elif difference <= 3:
        print(Fore.GREEN + "🔥 Very Close")
    elif difference <= 10:
        print(Fore.YELLOW + "⚡ Close")
    else:
        print(Fore.RED + "❄ Far")


# ---------------- SAVE SCORE ---------------- #

def save_score(player_name):
    global attempts, timer, hints_used, mode

    multiplier = {
        "Easy": 1,
        "Medium": 1.5,
        "Hard": 2
    }

    score = int((attempts * 10 + timer) * multiplier[mode] - (hints_used * 5))

    game_data = {
        "name": player_name,
        "mode": mode,
        "score": score,
        "time_left": timer,
        "attempts_left": attempts,
        "hints_used": hints_used
    }

    players = []

    if os.path.exists("Game_records.json"):
        try:
            with open("Game_records.json", "r") as file:
                players = json.load(file)
        except json.JSONDecodeError:
            players = []

    players.append(game_data)

    with open("Game_records.json", "w") as file:
        json.dump(players, file, indent=4)

    return score


# ---------------- LEADERBOARD ---------------- #

def leaderboard():

    if not os.path.exists("Game_records.json"):
        print(Fore.RED + "❌ No Records Found")
        return

    try:
        with open("Game_records.json", "r") as file:
            players = json.load(file)

    except:
        print(Fore.RED + "❌ Error Reading File")
        return

    if not players:
        print(Fore.RED + "❌ No Records Found")
        return

    # SORT BY SCORE
    players.sort(key=lambda x: x["score"], reverse=True)

    print(Fore.CYAN + Style.BRIGHT + "\n🏆 LEADERBOARD 🏆\n")

    for index, player in enumerate(players, start=1):

        print(Fore.YELLOW + f"Rank #{index}")
        print(Fore.GREEN + f"Player : {player['name']}")
        print(Fore.CYAN + f"Mode : {player['mode']}")
        print(Fore.MAGENTA + f"Score : {player['score']}")
        print(Fore.BLUE + f"Time Left : {player['time_left']} sec")
        print(Fore.RED + f"Attempts Left : {player['attempts_left']}")
        print(Fore.WHITE + f"Hints Used : {player['hints_used']}")
        print("-" * 35)


# ---------------- MAIN GAME ---------------- #

while True:

    print(Fore.MAGENTA + Style.BRIGHT + "\n🎮 NUMBER GUESSING GAME")

    print(Fore.YELLOW + "(1) " + Fore.WHITE + "Start Game")
    print(Fore.YELLOW + "(2) " + Fore.WHITE + "View Leaderboard")
    print(Fore.YELLOW + "(3) " + Fore.WHITE + "Exit")

    try:
        option = int(input(Fore.CYAN + "Select Option: "))

    except ValueError:
        print(Fore.RED + "❌ Enter Valid Number")
        continue

    # ---------------- START GAME ---------------- #

    if option == 1:

        game_reset()

        player_name = input(Fore.CYAN + "Enter Your Name: ")

        print(Fore.YELLOW + "\nSelect Difficulty")
        print("[1] Easy")
        print("[2] Medium")
        print("[3] Hard")

        try:
            mode_choice = int(input("Select Mode: "))
        except ValueError:
            print(Fore.RED + "❌ Invalid Input")
            continue

        if not modes(mode_choice):
            print(Fore.RED + "❌ Invalid Mode")
            continue

        # TARGET RANGE

        if mode_choice == 1:
            target = random.randint(1, 10)

        elif mode_choice == 2:
            target = random.randint(1, 50)

        else:
            target = random.randint(1, 100)

        # START TIMER THREAD

        timer_thread = threading.Thread(target=countdown, daemon=True)
        timer_thread.start()

        # ---------------- GAME LOOP ---------------- #

        while attempts > 0 and not time_out:

            try:

                print(Fore.CYAN + f"\n⏰ Time Left : {timer} sec")
                print(Fore.YELLOW + f"🎯 Attempts Left : {attempts}")

                guess = int(input("Guess Number: "))

            except ValueError:
                print(Fore.RED + "❌ Enter Valid Number")
                continue

            # CORRECT GUESS

            if guess == target:

                game_over = True

                print(Fore.GREEN + "\n🎉 CORRECT GUESS!")

                score = save_score(player_name)

                print(Fore.MAGENTA + f"🏆 Your Score : {score}")

                break

            # WRONG GUESS

            elif guess < target:
                print(Fore.YELLOW + "⬆ Higher")

            else:
                print(Fore.YELLOW + "⬇ Lower")

            attempts -= 1

            hint(target, guess)

        # ---------------- LOSE CONDITIONS ---------------- #

        game_over = True

        if time_out:
            print(Fore.RED + f"\n💀 You Lost! Number Was : {target}")

        elif attempts == 0:
            print(Fore.RED + "\n💀 No Attempts Left!")
            print(Fore.CYAN + f"Secret Number Was : {target}")

    # ---------------- LEADERBOARD ---------------- #

    elif option == 2:
        leaderboard()

    # ---------------- EXIT ---------------- #

    elif option == 3:

        print(Fore.YELLOW + "Exiting Game...")
        print(Fore.GREEN + "Exited Successfully!")

        break

    else:
        print(Fore.RED + "❌ Invalid Option")