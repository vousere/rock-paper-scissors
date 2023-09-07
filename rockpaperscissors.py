import random

user_win = 0
computer_win = 0

while True:
    if user_win == 3:
        print(f"You won the game!\nYour score: {user_win}\nComputer's score: {computer_win}")
        break
    elif computer_win == 3:
        print(f"Computer has won the game!\nYour score: {user_win}\nComputer's score: {computer_win}")
        break
    choices = ["rock","paper","scissors"]
    user_choice = input("Rock, paper or scissors?: ").lower()
    computer_choice = random.choice(choices)
    if user_choice not in choices:
        user_choice = input("Please enter your choice again,rock-paper-scissors: ")
    if user_choice == choices[0] and computer_choice == choices[0]:
        print("\tYou both chose rock!")
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[1] and computer_choice == choices[1]:
        print("\tYou both chose paper!")
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[2] and computer_choice == choices[2]:
        print("\tYou both chose scissors!")
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[0] and computer_choice == choices[1]:
        print(f"\tYou have been defeated.\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        computer_win = computer_win+1
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[0] and computer_choice == choices[2]:
        print(f"\tYou won!\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        user_win = user_win+1
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[1] and computer_choice == choices[0]:
        print(f"\tYou won!\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        user_win = user_win+1
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[1] and computer_choice == choices[2]:
        print(f"\tYou have been defeated.\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        computer_win = computer_win+1
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[2] and computer_choice == choices[0]:
        print(f"\tYou have been defeated.\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        computer_win = computer_win+1
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
    elif user_choice == choices[2] and computer_choice == choices[1]:
        print(f"\tYou won!\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        user_win = user_win+1
        print(f"User's score: {user_win}\nComputer's score: {computer_win}")
