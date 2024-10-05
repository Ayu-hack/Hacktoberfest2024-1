import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Capsule Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 32)
large_font = pygame.font.Font(None, 48)

# Extended quiz questions
questions = [
    {
        "decade": "1950s",
        "question": "Which vaccine, developed by Jonas Salk, was declared safe in 1955?",
        "options": ["Polio", "Smallpox", "Measles", "Tuberculosis"],
        "answer": "Polio",
        "fact": "The polio vaccine's success led to a worldwide effort to eradicate the disease."
    },
    {
        "decade": "1950s",
        "question": "What was the name of the first artificial satellite launched into space in 1957?",
        "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Telstar"],
        "answer": "Sputnik 1",
        "fact": "Sputnik 1's launch marked the beginning of the Space Age and the Space Race between the USA and USSR."
    },
    {
        "decade": "1960s",
        "question": "Which band released 'Abbey Road' in 1969?",
        "options": ["The Beatles", "The Rolling Stones", "The Who", "The Kinks"],
        "answer": "The Beatles",
        "fact": "The Beatles' 'Abbey Road' was their last recorded album, although 'Let It Be' was released later."
    },
    {
        "decade": "1960s",
        "question": "Who gave the famous 'I Have a Dream' speech in 1963?",
        "options": ["Martin Luther King Jr.", "John F. Kennedy", "Malcolm X", "Lyndon B. Johnson"],
        "answer": "Martin Luther King Jr.",
        "fact": "The speech was a defining moment of the American Civil Rights Movement."
    },
    {
        "decade": "1970s",
        "question": "What was the name of the first widely successful personal computer?",
        "options": ["Apple II", "Commodore PET", "TRS-80", "Altair 8800"],
        "answer": "Apple II",
        "fact": "The Apple II, introduced in 1977, was one of the first successful mass-produced microcomputers."
    },
    {
        "decade": "1970s",
        "question": "Which film is often considered to have started the 'blockbuster' era in 1975?",
        "options": ["Jaws", "Star Wars", "The Godfather", "The Exorcist"],
        "answer": "Jaws",
        "fact": "Jaws was the first movie to earn $100 million in theatrical rentals."
    },
    {
        "decade": "1980s",
        "question": "Which toy, first sold in 1980, became a worldwide craze?",
        "options": ["Rubik's Cube", "Cabbage Patch Kids", "Transformers", "My Little Pony"],
        "answer": "Rubik's Cube",
        "fact": "The Rubik's Cube was invented in 1974 by Hungarian sculptor and professor Ernő Rubik."
    },
    {
        "decade": "1980s",
        "question": "What was the name of the nuclear accident that occurred in Ukraine in 1986?",
        "options": ["Chernobyl", "Three Mile Island", "Fukushima", "Kyshtym"],
        "answer": "Chernobyl",
        "fact": "The Chernobyl disaster is considered the worst nuclear accident in history both in cost and casualties."
    },
    {
        "decade": "1990s",
        "question": "What was the name of the sheep, the first mammal cloned from an adult cell?",
        "options": ["Dolly", "Molly", "Polly", "Holly"],
        "answer": "Dolly",
        "fact": "Dolly the sheep was born in 1996 and lived until 2003, proving that cloning was possible using adult animal cells."
    },
    {
        "decade": "1990s",
        "question": "Which operating system did Microsoft release in 1995?",
        "options": ["Windows 95", "Windows 3.1", "Windows 98", "Windows NT"],
        "answer": "Windows 95",
        "fact": "Windows 95 introduced the Start menu, taskbar, and minimize/maximize buttons, which are still used in modern Windows versions."
    },
    {
        "decade": "2000s",
        "question": "Which social media platform was founded by Mark Zuckerberg in 2004?",
        "options": ["Facebook", "MySpace", "Twitter", "LinkedIn"],
        "answer": "Facebook",
        "fact": "Facebook was initially limited to college students before opening to everyone over 13 in 2006."
    },
    {
        "decade": "2000s",
        "question": "What was the name of the ocean tsunami that devastated parts of Asia in 2004?",
        "options": ["Indian Ocean Tsunami", "Pacific Tsunami", "Atlantic Tsunami", "Mediterranean Tsunami"],
        "answer": "Indian Ocean Tsunami",
        "fact": "The 2004 Indian Ocean tsunami was one of the deadliest natural disasters in recorded history, killing over 230,000 people across 14 countries."
    },
    {
        "decade": "2010s",
        "question": "Which app, launched in 2010, allowed users to share photos that disappeared after a short time?",
        "options": ["Snapchat", "Instagram", "TikTok", "Vine"],
        "answer": "Snapchat",
        "fact": "Snapchat's disappearing messages feature was revolutionary in social media, leading to many imitators."
    },
    {
        "decade": "2010s",
        "question": "What was the name of the massive leak of financial documents in 2016 that exposed offshore accounts?",
        "options": ["Panama Papers", "WikiLeaks", "Edward Snowden Files", "Cambridge Analytica Scandal"],
        "answer": "Panama Papers",
        "fact": "The Panama Papers comprised 11.5 million leaked documents detailing financial information for more than 214,000 offshore entities."
    }
]

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Quiz:
    def __init__(self):
        self.questions = questions.copy()
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.state = "question"  # Can be "question", "answer", or "end"

    def next_question(self):
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]
        return None

    def check_answer(self, selected_answer):
        current_q = self.questions[self.current_question]
        if selected_answer == current_q["answer"]:
            self.score += 1
            return True
        return False

    def advance(self):
        self.current_question += 1
        if self.current_question >= len(self.questions):
            self.state = "end"
        else:
            self.state = "question"

# Create quiz instance
quiz = Quiz()

# Create buttons
button_width, button_height = 300, 50
button_margin = 20
buttons = []

for i in range(4):
    x = (WIDTH - button_width) // 2
    y = 250 + i * (button_height + button_margin)
    buttons.append(Button(x, y, button_width, button_height, "", GRAY))

next_button = Button((WIDTH - button_width) // 2, 500, button_width, button_height, "Next", BLUE)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quiz.state == "question":
                for i, button in enumerate(buttons):
                    if button.is_clicked(event.pos):
                        current_q = quiz.questions[quiz.current_question]
                        if quiz.check_answer(current_q["options"][i]):
                            button.color = GREEN
                        else:
                            button.color = RED
                            for j, opt in enumerate(current_q["options"]):
                                if opt == current_q["answer"]:
                                    buttons[j].color = GREEN
                        quiz.state = "answer"
            elif quiz.state == "answer":
                if next_button.is_clicked(event.pos):
                    quiz.advance()
                    for button in buttons:
                        button.color = GRAY

    screen.fill(WHITE)

    if quiz.state != "end":
        current_q = quiz.questions[quiz.current_question]
        
        # Draw decade
        decade_text = large_font.render(current_q["decade"], True, BLUE)
        decade_rect = decade_text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(decade_text, decade_rect)

        # Draw question
        question_text = font.render(current_q["question"], True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH // 2, 150))
        screen.blit(question_text, question_rect)

        # Draw buttons
        for i, button in enumerate(buttons):
            button.text = current_q["options"][i]
            button.draw()

        if quiz.state == "answer":
            # Draw fact
            fact_text = font.render(current_q["fact"], True, BLACK)
            fact_rect = fact_text.get_rect(center=(WIDTH // 2, 450))
            screen.blit(fact_text, fact_rect)
            
            next_button.draw()
    else:
        # Display final score
        score_text = large_font.render(f"Final Score: {quiz.score}/{len(quiz.questions)}", True, BLUE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(score_text, score_rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
