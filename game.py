import random
import time
import os
import sys

# Initialize global variables
HP = 100
score = 0
hammer = True
Gangmembers = 4
drinks = ['D1', 'D2', 'D3']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    """Introduction to the game"""
    print("Hello, player")
    time.sleep(0.5)
    print("Enter your national ID here:")
    input("> ")
    print("I'm kidding!!")
    time.sleep(1)
    print("You are 3 years old...")
    time.sleep(1)
    print("You are dreaming of being a warrior")
    time.sleep(1)
    print("But you can't be one... That's right!")
    time.sleep(1)
    print("You are a child! But you can when you are 18.")
    time.sleep(1)
    print("Enter 18!")
    time.sleep(1)
    if input("> ") == "18":
        print("Hooray! You are 18")
    else:
        print("Nah, that's not 18")
    time.sleep(1)

def weapon_pick():
    """Let player pick a weapon"""
    global hammer
    print("Now you are in the Weapons shop.")
    time.sleep(1)
    print("You are ordered to choose a weapon.")
    print("1. Sledgehammer")
    print("2. Suppressed M4 Carbine with attachments.")
    print("3. A banana")
    while True:
        cmd = input("> ")
        if cmd == "1":
            print("Great choice for an adventure game.")
            hammer = True
            break
        elif cmd == "2":
            print("Not today, this isn't Call of Duty.")
        elif cmd == "3":
            print("Healthy choice, but not a weapon.")
        else:
            print("Invalid option.")

def fight():
    """Combat with gang members"""
    global HP, hammer, Gangmembers, score
    print("You face 4 gang members!")
    time.sleep(2)
    clear_screen()
    print(f"Your Health: {HP}")
    print("Choose an action:")
    print("1. Run away")
    print("2. Use a broken bottle")
    print("3. Use your hammer")
    print("4. Call for help")
    print("5. Fight one by one")

    while Gangmembers > 0 and HP > 0:
        cmd = input("> ")
        if cmd == "1":
            print("You ran, but got stabbed!")
            HP -= 80
            print(f"HP: {HP}")
        elif cmd == "2":
            print("You tried using a broken bottle.")
            HP -= 20
            print(f"You cut yourself. HP: {HP}")
        elif cmd == "3":
            if hammer:
                print("You smashed a gang member!")
                hammer = False
                Gangmembers -= 1
                score += 100
                print(f"Enemies left: {Gangmembers}")
            else:
                print("Hammer can't be used again.")
        elif cmd == "4":
            print("No one heard you...")
        elif cmd == "5":
            print("Fighting with skill!")
            Gangmembers -= 3
            score += 300
            print("You defeated 3 enemies!")
        else:
            print("Invalid action.")

    if HP <= 0:
        game_over()
    elif Gangmembers <= 0:
        print("You won the fight!")
        print(f"Score: {score}")
        time.sleep(1)

def finale():
    """Final challenge with poisoned drinks"""
    global score
    print("You’re at a bar. Plot twist: the bartender is an enemy!")
    time.sleep(2)
    clear_screen()
    print("Pick one drink (2 are poisoned):")
    random.shuffle(drinks)
    safe_drink = random.choice(drinks)
    print("1. Drink 1\n2. Drink 2\n3. Drink 3")
    while True:
        choice = input("> ")
        if choice in ['1', '2', '3']:
            if drinks[int(choice) - 1] == safe_drink:
                print("You survived!")
                score += 200
                break
            else:
                print("Poisoned! You died.")
                game_over()
        else:
            print("Invalid input.")

    print("Final choice:")
    print("1. Destroy the bar")
    print("2. Forgive and leave")

    while True:
        cmd = input("> ")
        if cmd == "1" or cmd == "2":
            print("You unleash your wrath and become a WARRIOR!")
            score += 200
            print(f"Final Score: {score}")
            break
        else:
            print("Invalid choice.")
    end_game()

def game_over():
    """Handle game over and restart prompt"""
    print("GAME OVER!")
    print(f"Final Score: {score}")
    if input("Play again? (y/n) > ").lower() == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        sys.exit()

def end_game():
    """Handle end of game with exit or restart"""
    if input("Do you want to play again? (y/n) > ").lower() == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Thanks for playing!")
        sys.exit()

# === Game Start ===
if __name__ == "__main__":
    while True:
        HP = 100
        score = 0
        hammer = True
        Gangmembers = 4
        intro()
        weapon_pick()
        fight()
        finale()
        break
