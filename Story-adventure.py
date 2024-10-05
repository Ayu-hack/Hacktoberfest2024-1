class QuizAdventure:
    def __init__(self):
        self.questions = [
            {
                "story": "You wake up in a dark forest. There's a path ahead, but you hear strange sounds behind you.",
                "question": "What do you do?",
                "options": ["Run forward", "Turn back", "Climb a tree", "Wait and observe"],
                "correct": 1
            },
            {
                "story": "You run forward and find a small village. There's an inn where you can rest, but the villagers seem unfriendly.",
                "question": "What do you do next?",
                "options": ["Enter the inn", "Talk to a villager", "Keep walking", "Hide in the shadows"],
                "correct": 2
            },
            {
                "story": "A villager tells you about a mysterious cave nearby. You decide to explore it.",
                "question": "Inside the cave, you see three tunnels. Which tunnel do you choose?",
                "options": ["Left", "Right", "Middle", "Turn back"],
                "correct": 3
            },
            {
                "story": "You enter the middle tunnel and come across a treasure chest. It's locked, but there's a puzzle on the chest.",
                "question": "How many sides does a hexagon have?",
                "options": ["4", "5", "6", "8"],
                "correct": 3
            },
            {
                "story": "After solving the puzzle, the chest opens, revealing a map to the Dragon's Lair.",
                "question": "Do you follow the map or explore the village first?",
                "options": ["Follow the map", "Explore the village", "Rest at the inn", "Talk to villagers again"],
                "correct": 1
            },
            {
                "story": "You arrive at the Dragon's Lair, but there are three guards blocking the entrance.",
                "question": "How do you proceed?",
                "options": ["Fight the guards", "Try to sneak past them", "Bribe them", "Ask for permission"],
                "correct": 2
            },
            {
                "story": "You successfully sneak past the guards and find the Dragon sleeping on a pile of gold.",
                "question": "What is your next move?",
                "options": ["Take the gold", "Try to talk to the Dragon", "Attack the Dragon", "Leave quietly"],
                "correct": 2
            },
            {
                "story": "The Dragon wakes up and listens to your story. It agrees to help you on your journey.",
                "question": "What do you ask the Dragon to do?",
                "options": ["Fly you to the next town", "Give you some gold", "Fight your enemies", "Guard the village"],
                "correct": 1
            }
        ]
        self.current_question = 0
        self.score = 0

    def ask_question(self):
        question_data = self.questions[self.current_question]
        print("\n" + question_data["story"])
        print(question_data["question"])
        for idx, option in enumerate(question_data["options"], start=1):
            print(f"{idx}. {option}")
        return question_data

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("Correct! The adventure continues...")
            self.score += 1
        else:
            print("Wrong choice! The story takes a dark turn...")

    def play(self):
        while self.current_question < len(self.questions):
            question_data = self.ask_question()
            try:
                answer = int(input("Choose an option (1-4): "))
                if 1 <= answer <= 4:
                    self.check_answer(answer, question_data["correct"])
                    self.current_question += 1
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        print(f"\nAdventure over! You scored {self.score}/{len(self.questions)}.")


if __name__ == "__main__":
    game = QuizAdventure()
    game.play()
