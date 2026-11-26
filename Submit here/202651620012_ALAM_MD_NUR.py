"""Name: ALAM MD NUR
SchoolID:202651620012
"""


"""Hangman - a word-guessing game built with Python's turtle module.

Rules:
    * A secret word is chosen at random and shown as underscores.
    * Guess one letter at a time through the pop-up dialog.
    * Each wrong guess draws one more part of the hangman.
    * Guess the word before 6 mistakes to win.
"""

import random
import turtle

# ------------------------------------------------------------------ #
# Settings
# ------------------------------------------------------------------ #
MAX_WRONG = 6
WORDS = [
    "ducks", "python", "turtle", "spiking", "neuron", "network",
    "vision", "signal", "keyboard", "science", "student", "university",
    "algorithm", "research", "computer", "machine", "program", "variable",
]

FONT_WORD = ("Courier", 32, "bold")
FONT_INFO = ("Arial", 18, "normal")
FONT_RESULT = ("Arial", 26, "bold")

# Gallows lines: (x1, y1, x2, y2)
GALLOWS = [
    (-150, -150, 0, -150),   # base
    (-75, -150, -75, 150),   # pole
    (-75, 150, 25, 150),     # beam
    (25, 150, 25, 120),      # rope
]

# Body lines drawn after the head: (x1, y1, x2, y2)
BODY_PARTS = [
    (25, 80, 25, -10),       # body
    (25, 60, -5, 30),        # left arm
    (25, 60, 55, 30),        # right arm
    (25, -10, 0, -60),       # left leg
    (25, -10, 50, -60),      # right leg
]

# ------------------------------------------------------------------ #
# Window and pens
# ------------------------------------------------------------------ #
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Hangman - My First Game")
screen.bgcolor("white")
screen.tracer(0)                 # we call screen.update() ourselves

pen = turtle.Turtle()            # draws the gallows and the hangman
pen.hideturtle()
pen.speed(0)
pen.pensize(4)
pen.penup()

writer = turtle.Turtle()         # writes the word and the messages
writer.hideturtle()
writer.penup()

# ------------------------------------------------------------------ #
# Game loop
# ------------------------------------------------------------------ #
playing = True

try:
    while playing:
        # ---- start a new round ----
        word = random.choice(WORDS)
        guessed = set()
        wrong = set()
        hint = ""

        pen.clear()
        pen.color("saddle brown")
        for x1, y1, x2, y2 in GALLOWS:
            pen.penup()
            pen.goto(x1, y1)
            pen.pendown()
            pen.goto(x2, y2)
        pen.penup()
        pen.color("black")

        # ---- one guess per pass ----
        while True:
            shown = " ".join(ch if ch in guessed else "_" for ch in word)
            wrong_text = ", ".join(sorted(wrong)) if wrong else "none"

            writer.clear()
            for y, text, font, color in [
                (-210, shown, FONT_WORD, "black"),
                (-260, "Wrong letters: " + wrong_text, FONT_INFO, "firebrick"),
                (-295, "Attempts left: " + str(MAX_WRONG - len(wrong)), FONT_INFO, "black"),
            ]:
                writer.color(color)
                writer.goto(0, y)
                writer.write(text, align="center", font=font)
            screen.update()

            # win / lose checks
            if all(ch in guessed for ch in word):
                writer.color("forest green")
                writer.goto(0, 200)
                writer.write("You win!", align="center", font=FONT_RESULT)
                screen.update()
                break
            if len(wrong) >= MAX_WRONG:
                writer.color("firebrick")
                writer.goto(0, 200)
                writer.write("You lose! The word was '" + word + "'",
                             align="center", font=FONT_RESULT)
                screen.update()
                break

            # ask for a letter
            answer = screen.textinput("Hangman", hint + "Enter a letter:")
            if answer is None:               # player pressed Cancel
                playing = False
                break

            letter = answer.strip().lower()

            # validate the input
            if len(letter) != 1 or not letter.isalpha():
                hint = "Please type exactly ONE letter.\n"
                continue
            if letter in guessed or letter in wrong:
                hint = "You already tried '" + letter + "'.\n"
                continue
            hint = ""

            # correct or wrong guess
            if letter in word:
                guessed.add(letter)
            else:
                if len(wrong) == 0:          # 1st mistake: draw the head
                    pen.goto(25, 80)
                    pen.setheading(0)
                    pen.pendown()
                    pen.circle(20)
                    pen.penup()
                else:                        # later mistakes: draw a line
                    x1, y1, x2, y2 = BODY_PARTS[len(wrong) - 1]
                    pen.goto(x1, y1)
                    pen.pendown()
                    pen.goto(x2, y2)
                    pen.penup()
                wrong.add(letter)

        # ---- play again? ----
        if playing:
            again = screen.textinput("Hangman", "Play again? (y/n)")
            playing = again is not None and again.strip().lower().startswith("y")

    # ---- goodbye ----
    writer.clear()
    writer.color("black")
    writer.goto(0, -250)
    writer.write("Thanks for playing!", align="center", font=FONT_RESULT)
    screen.update()
    screen.mainloop()                # keep the window open

except turtle.Terminator:
    pass                             # window was closed by the player