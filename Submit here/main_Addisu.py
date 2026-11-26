import turtle

# ===== Screen setting =====
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Hangman Game")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.speed(0)

# ===== Gallow (draw before the game) =====
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.goto(100, -100)       # ground
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.goto(0, 150)          # post
pen.goto(80, 150)         # crossbar
pen.goto(80, 120)         # rope

# ===== Text panel =====
info = turtle.Turtle()
info.hideturtle()
info.penup()

# ===== Game settings =====
word = "python"           # Change this to any lowercase word
guessed = ""
wrong = 0
won = False
cancelled = False
max_attempts = 6

# ===== Main game loop =====
for attempt in range(max_attempts):

    # --- 1. Show the word and number of mistakes ---
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    info.clear()
    info.goto(-300, -200)
    info.write("Word: " + display, font=("Arial", 18, "normal"))
    info.goto(-300, -235)
    info.write(
        "Mistakes: " + str(wrong) + " / " + str(max_attempts),
        font=("Arial", 14, "normal")
    )
    screen.update()

    # --- 2. Ask for a letter ---
    while True:
        letter = screen.textinput("Hangman", "Enter one letter:")

        if letter is None:
            cancelled = True
            break

        letter = letter.strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            info.goto(-300, -270)
            info.write(
                "Please enter ONE letter (A-Z).",
                font=("Arial", 12, "italic")
            )
            screen.update()
            continue

        if letter in guessed:
            info.goto(-300, -270)
            info.write(
                "You have already entered that letter!",
                font=("Arial", 12, "italic")
            )
            screen.update()
            continue

        break

    if cancelled:
        break

    guessed += letter

    # --- 3. Check the letter ---
    if letter not in word:
        wrong += 1

        # Draw the next part of the person
        pen.penup()

        if wrong == 1:                  # Head
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(20)

        elif wrong == 2:                # Body
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)

        elif wrong == 3:                # Left hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)

        elif wrong == 4:                # Right hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(100, 50)

        elif wrong == 5:                # Left leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(60, 10)

        elif wrong == 6:                # Right leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(100, 10)

    # --- 4. Check whether the player has won ---
    won = True
    for letter_in_word in word:
        if letter_in_word not in guessed:
            won = False
            break

    if won:
        break

# ===== Final result =====
info.clear()
info.goto(-300, -200)

if won:
    info.write(
        "You win! The word is: " + word,
        font=("Arial", 18, "bold")
    )
elif cancelled:
    info.write(
        "Game cancelled. The word was: " + word,
        font=("Arial", 18, "bold")
    )
else:
    info.write(
        "You lose! The word was: " + word,
        font=("Arial", 18, "bold")
    )

# ===== Clickable close button =====
info.goto(-75, -270)
info.write(
    "[ CLICK HERE TO CLOSE ]",
    font=("Arial", 12, "bold")
)

def close_game(x, y):
    # Close only when the player clicks the displayed button area
    if -110 <= x <= 150 and -300 <= y <= -265:
        screen.bye()

screen.onclick(close_game)
screen.update()
turtle.done()
