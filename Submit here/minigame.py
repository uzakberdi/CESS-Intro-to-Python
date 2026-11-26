
import turtle

# ===== Screen setting =====
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Hangman in Turtle")
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

# ===== Text panel =====
info = turtle.Turtle()
info.hideturtle()
info.penup()

# ===== Game settings =====
word = "python"
guessed = ""
wrong = 0
won = False

# ===== Game loop =====
for attempt in range(6):

    # --- 1. Showing word or mistakes number ---
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

    # --- 2. Word enter ---
    letter = screen.textinput("Hangman", "Enter your letter:")

    if letter is None:
        letter = ""

    letter = letter.strip().lower()

    # --- 3. Checking ---
    if len(letter) != 1 or not letter.isalpha():
        info.goto(-300, -270)
        info.write("Please enter one valid letter!",
                   font=("Arial", 12, "italic"))

    elif letter in guessed:
        info.goto(-300, -270)
        info.write("You've already entered this letter!",
                   font=("Arial", 12, "italic"))

    elif letter in word:
        guessed += letter

    else:
        guessed += letter
        wrong += 1

        # Drawing new part of body
        pen.penup()

        if wrong == 1:             # Head
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(20)

        elif wrong == 2:           # Body
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)

        elif wrong == 3:           # Left hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)

        elif wrong == 4:           # Right hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(100, 50)

        elif wrong == 5:           # Left leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(60, 10)

        elif wrong == 6:           # Right leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(100, 10)

    # --- 4. Checking the win ---
    win = True

    for letter in word:
        if letter not in guessed:
            win = False

    if win:
        won = True
        break

# ===== Final display =====
info.clear()

display = ""
for letter in word:
    if letter in guessed:
        display += letter + " "
    else:
        display += "_ "

info.goto(-300, -200)
info.write("Word: " + display, font=("Arial", 18, "normal"))

info.goto(-300, -235)
info.write("Mistakes: " + str(wrong) + " / 6",
           font=("Arial", 14, "normal"))

info.goto(-300, -305)

if won:
    info.write("Winner winner chicken dinner! Word is: " + word,
               font=("Arial", 18, "bold"))
else:
    info.write("You lose! Word was: " + word,
               font=("Arial", 18, "bold"))

screen.update()
turtle.done()
 
AdjeiKwameSarpong = 202453083001 