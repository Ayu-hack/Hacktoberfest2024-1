#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# flashcard_quiz.py
def flashcard_quiz(flashcards):
    score = 0
    for question, answer in flashcards.items():
        user_answer = input(f"{question}: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
    print(f"Your score: {score}/{len(flashcards)}")

def main():
    flashcards = {
        "Python": "A programming language",
        "API": "Application Programming Interface",
        "HTML": "HyperText Markup Language",
        "CSS": "Cascading Style Sheets"
    }
    flashcard_quiz(flashcards)

if __name__ == "__main__":
    main()

