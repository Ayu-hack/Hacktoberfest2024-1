#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

HANGMAN_PICS = [
    """
     ------
     |    |
     |
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """,
]

WORDS = ['python', 'javascript', 'hangman', 'development', 'terminal', 'project']

def get_random_word(word_list):
    return random.choice(word_list).lower()

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print("\nMissed letters:", ' '.join(missed_letters))
    
    blanks = ['_' if letter not in correct_letters else letter for letter in secret_word]
    print(" ".join(blanks))

def is_valid_guess(guess, missed_letters, correct_letters):
    # Check if the input is a single alphabetic character
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        return False
    # Check if the letter has already been guessed
    if guess in missed_letters or guess in correct_letters:
        print("You've already guessed that letter! Try again.")
        return False
    return True

def play_hangman():
    secret_word = get_random_word(WORDS)
    missed_letters = []
    correct_letters = []

    while len(missed_letters) < len(HANGMAN_PICS) - 1:
        display_board(missed_letters, correct_letters, secret_word)
        
        guess = input("Guess a letter: ").lower()

        if is_valid_guess(guess, missed_letters, correct_letters):
            if guess in secret_word:
                correct_letters.append(guess)
                if all(letter in correct_letters for letter in secret_word):
                    print(f"Congratulations! You've guessed the word '{secret_word}'.")
                    break
            else:
                missed_letters.append(guess)
        
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print(f"Sorry, you've been hanged! The word was '{secret_word}'.")
            break

if __name__ == "__main__":
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


# In[ ]:




