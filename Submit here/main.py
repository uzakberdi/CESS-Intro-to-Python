import turtle

# ===== Screen setting =====
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Gallow in turtle")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.speed(0)

# ===== Gallow (drawing before the game) =====
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.goto(100, -100)       # earth
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.goto(0, 150)          # post
pen.goto(80, 150)         # crossbar
pen.goto(80, 120)         # rope

# ===== text panel =====
info = turtle.Turtle()
info.hideturtle()
info.penup()

Derrick = 202453083003


# ===== Game settings =====
word = "python"           # task #1: your own word
guessed = ""
wrong = 0
won = False
message = ""              # message shown on the next screen refresh


def show_status():
    """Redraw the word, mistakes counter and any message."""
    display = ""
    for ch in word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    info.clear()
    info.goto(-300, -200)
    info.write("Word: " + display, font=("Arial", 18, "normal"))
    info.goto(-300, -235)
    info.write("Mistakes: " + str(wrong) + " / 6", font=("Arial", 14, "normal"))
    if message:
        info.goto(-300, -270)
        info.write(message, font=("Arial", 12, "italic"))
    screen.update()


# task #2: 26 letters in the alphabet is the most guesses anyone could need;
# the loop also stops as soon as the player wins or makes 6 mistakes
for attempt in range(26):
    # --- 1. showing word or mistakes number ---
    show_status()
    message = ""

    # --- 2. letter enter ---
    letter = screen.textinput("Gallow", "Your letter:")
    if letter is None:
        letter = ""
    letter = letter.strip().lower()

    # --- 3. checking ---
    if len(letter) != 1 or not letter.isalpha():
        message = "Please enter exactly one letter!"
    elif letter in guessed:
        message = "You've already entered this letter!"
    elif letter in word:
        guessed += letter
    else:
        guessed += letter         # remember wrong letters too
        wrong += 1
        # drawing new part of body
        pen.penup()
        if wrong == 1:                    # head
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(20)
        elif wrong == 2:                  # body
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)
        elif wrong == 3:                  # left hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)
        elif wrong == 4:                  # task #3: right hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(100, 50)
        elif wrong == 5:                  # left leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(60, 10)
        elif wrong == 6:                  # right leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(100, 10)

    # --- 4. checking the win / loss ---
    win = True
    for ch in word:
        if ch not in guessed:
            win = False
    if win:
        won = True
        break
    if wrong >= 6:
        break

# ===== Final =====
message = ""
show_status()             # refresh so the last guess is visible
info.goto(-300, -305)
if won:
    info.write("Winner winner chicken dinner! Word is: " + word, font=("Arial", 18, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Arial", 18, "bold"))

screen.update()
turtle.done()