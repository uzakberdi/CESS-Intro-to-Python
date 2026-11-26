
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

# ===== Gallow =====
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.goto(100, -100)
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.goto(0, 150)
pen.goto(80, 150)
pen.goto(80, 120)

# ===== Text panel =====
info = turtle.Turtle()
info.hideturtle()
info.penup()

# ===== Game settings =====
word = "python"
guessed = ""
wrong = 0
won = False

try:
    # ===== Game loop =====
    while wrong < 6:

        # Showing word
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        info.clear()
        info.goto(-300, -200)
        info.write("Word: " + display,
                   font=("Arial", 18, "normal"))

        info.goto(-300, -235)
        info.write("Mistakes: " + str(wrong) + " / 6",
                   font=("Arial", 14, "normal"))

        screen.update()

        # Enter letter
        letter = screen.textinput("Hangman", "Your letter:")

        if letter is None:
            break

        letter = letter.strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            continue

        # Checking letter
        if letter in guessed:
            info.goto(-300, -270)
            info.write("Already entered!",
                       font=("Arial", 12, "italic"))

        elif letter in word:
            guessed += letter

        else:
            guessed += letter
            wrong += 1

            pen.penup()

            if wrong == 1:       # Head
                pen.goto(80, 80)
                pen.pendown()
                pen.circle(20)

            elif wrong == 2:     # Body
                pen.goto(80, 80)
                pen.pendown()
                pen.goto(80, 40)

            elif wrong == 3:     # Left hand
                pen.goto(80, 70)
                pen.pendown()
                pen.goto(60, 50)

            elif wrong == 4:     # Right hand
                pen.goto(80, 70)
                pen.pendown()
                pen.goto(100, 50)

            elif wrong == 5:     # Left leg
                pen.goto(80, 40)
                pen.pendown()
                pen.goto(60, 10)

            elif wrong == 6:     # Right leg
                pen.goto(80, 40)
                pen.pendown()
                pen.goto(100, 10)

        # Checking win
        won = True

        for letter in word:
            if letter not in guessed:
                won = False

        if won:
            break

        screen.update()

    # ===== Final =====
    info.clear()
    info.goto(-300, -305)

    if won:
        info.write("You Win! Word: " + word,
                   font=("Arial", 18, "bold"))
    else:
        info.write("You Lose! Word: " + word,
                   font=("Arial", 18, "bold"))

    screen.update()
    turtle.done()

except turtle.Terminator:
    pass
