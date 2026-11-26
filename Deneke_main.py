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

# ===== Game settings =====
word = "python"           # task #1: insert your own word (any word you want)
guessed = ""
wrong = 0
max_wrong = 6
won = False

# task #2: 6 body parts = at most 6 mistakes, plus winning guesses.
# Using a loop up to 26 (alphabet size) ensures the player gets enough turns
# to win even after making mistakes, while stopping early on win or 6 mistakes.
for attempt in range(26):
    # --- 1. showing word or mistakes number ---
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
    info.write(
        "Mistakes: " + str(wrong) + " / " + str(max_wrong),
        font=("Arial", 14, "normal"),
    )

    screen.update()        # ← showing all before the second word enter

    # --- 2. word enter ---
    letter = screen.textinput("Gallow", "Your letter:")
    if letter is None:
        break              # player closed/cancelled the dialog
    letter = letter.strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        info.goto(-300, -270)
        info.write("Please enter a single letter!", font=("Arial", 12, "italic"))
        screen.update()
        continue

    # --- 3. checking ---
    if letter in guessed:
        info.goto(-300, -270)
        info.write("You've already entered this letter!", font=("Arial", 12, "italic"))
        screen.update()
        continue

    guessed += letter

    if letter not in word:
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
        elif wrong == 4:                  # task #3: right hand (mirrored from left hand)
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

    # --- 4. checking the win or loss ---
    win = True
    for ch in word:
        if ch not in guessed:
            win = False
            break

    if win:
        won = True
        break

    if wrong >= max_wrong:
        break

# ===== Final =====
info.clear()
display = " ".join(ch if ch in guessed else "_" for ch in word)
info.goto(-300, -200)
info.write("Word: " + display, font=("Arial", 18, "normal"))
info.goto(-300, -235)
info.write(
    "Mistakes: " + str(wrong) + " / " + str(max_wrong),
    font=("Arial", 14, "normal"),
)
info.goto(-300, -305)
if won:
    info.write("Winner winner chicken dinner! Word is: " + word, font=("Arial", 18, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Arial", 18, "bold"))

screen.update()
turtle.done()