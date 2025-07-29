import random
def rock_Paper_Scissors():
    print("Welcome to rock 🪨  Paper 📃 Scissors ✂️")
    options = ["rock","paper","scissors"]
    userscore = 0
    computerscore = 0
    while True:
        userchoice = input("Choose rock paper or scissors(or 'quit' to stop)\n").lower()
        if userchoice == "quit":
            break
        if userchoice not in options:
            print("Invalid Choice Please Try again")
            continue
        computerchoice = random.choice(options)
        print(f"the computer chose: {computerchoice}")
        if userchoice == computerchoice:
            print("Its a tie👔")
        elif(userchoice == "rock" and computerchoice == "scissors") or \
            (userchoice == "paper" and computerchoice == "rock") or \
            (userchoice == "scissors" and computerchoice == "paper"):
            print("You win this round!🏆🥇")
            userscore += 1
        else:
            print("The computer wins this round")
            computerscore += 1
        print(f"score: You {userscore} | {computerscore} computer\n")

rock_Paper_Scissors()