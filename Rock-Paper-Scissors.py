import random


def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    return choice


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    return "Computer wins!"


while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break
