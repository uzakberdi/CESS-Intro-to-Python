
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
word = "python"   # Task 1: insert your own word
guessed = ""
wrong = 0
won = False

# -----Additional task------

info.goto(-300, 250)
info.write("Welcome to Hangman!",
           font=("Arial", 18, "bold"))
screen.update()

for attempt in range(6):     # Task 2: six attempts

    # --- 1. showing word or mistakes number ---
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
    info.write("Mistakes: " + str(wrong) + " / 6",
               font=("Arial", 14, "normal"))

    screen.update()

    # --- 2. word enter ---
    letter = screen.textinput("Gallow", "Your letter:")
    if letter is None:
        break

    letter = letter.strip().lower()

    # --- 3. checking ---
    if len(letter) != 1 or not letter.isalpha():
        info.goto(-300, -270)
        info.write("Please enter only one letter!",
                   font=("Arial", 12, "italic"))

    elif letter in guessed:
        info.goto(-300, -270)
        info.write("You've already entered this letter!",
                   font=("Arial", 12, "italic"))

    else:
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

            elif wrong == 4:                  # Task 3: right hand
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

    # --- 4. checking the win ---
    win = True
    for letter in word:
        if letter not in guessed:
            win = False

    if win:
        won = True
        break

# ===== Final =====
info.clear()
info.goto(-300, -305)

if won:
    info.write("Winner winner chicken dinner! Word is: " + word,
               font=("Arial", 18, "bold"))
else:
    info.write("You lose. Word was: " + word,
               font=("Arial", 18, "bold"))

screen.update()
turtle.done()

