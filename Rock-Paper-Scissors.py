#rock paper scissor game in python
import random

def get_choice(prompt):
    choice = input(prompt).strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Choose Rock, Paper, or Scissors: ").strip().lower()
    return choice

def determine_winner(user, computer):
    outcomes = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "It's a tie!" if user == computer else "You win!" if outcomes[user] == computer else "Computer wins!"

while input("Play Rock, Paper, Scissors? (yes/no): ").strip().lower() == "yes":
    user_choice, computer_choice = get_choice("Choose Rock, Paper, or Scissors: "), random.choice(["rock", "paper", "scissors"])
    print(f"You chose {user_choice}, Computer chose {computer_choice}. {determine_winner(user_choice, computer_choice)}")
