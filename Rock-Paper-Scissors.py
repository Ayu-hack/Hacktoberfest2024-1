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
        print("It's a tie")
        return 0
    
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win! Congratulations!")
        return 1
    
    else:
        print("Computer wins! Better luck next time!")
        return -1

print("\nWelcome to\n") 
print(r"  ___         _               ")
print(r" | _ \___  __| |__            ")
print(r" |   / _ \/ _| / /            ")
print(r" |_|_\___/\__|_\_\            ")
print(r" | _ \__ _ _ __  ___ _ _      ")
print(r" |  _/ _` | '_ \/ -_) '_|     ")
print(r" |_| \__,_| .__/\___|_|       ")
print(r"  ___     |_|                 ")
print(r" / __| __(_)______ ___ _ _ ___")
print(r" \__ \/ _| (_-<_-</ _ \ '_(_-<")
print(r" |___/\__|_/__/__/\___/_| /__/")
print("\n")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        result = determine_winner(user_choice, computer_choice)

        if result == 1:
            user_score += 1
        
        elif result == -1:
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again in ["yes", "y"]:
            continue

        elif play_again in ["no", "n"]:
            print(f"Score - You: {user_score}, Computer: {computer_score}")
            print("Thank you for playing!")
            break

        else:
            print("Error - Invalid input!")

if __name__ == "__main__":
    main()