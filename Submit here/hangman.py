import turtle

# Name: YOUSSEF AKHARCHAF
# Student ID: 202651200006

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Hangman Game")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.speed(0)

# Gallows
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

info = turtle.Turtle()
info.hideturtle()
info.penup()

word = "computer"
guessed = ""
wrong = 0
won = False
message = ""

while wrong < 6 and not won:
    display = ""
    for character in word:
        if character in guessed:
            display += character + " "
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
        message = ""
    screen.update()

    letter = screen.textinput("Hangman", "Enter a letter:")

    if letter is None:
        letter = ""
    letter = letter.strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        message = "Please enter one letter only!"
        continue

    if letter in guessed:
        message = "You've already entered this letter!"
        continue

    if letter in word:
        guessed += letter
    else:
        wrong += 1
        pen.penup()

        if wrong == 1:
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(20)
        elif wrong == 2:
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)
        elif wrong == 3:
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)
        elif wrong == 4:
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(100, 50)
        elif wrong == 5:
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(60, 10)
        elif wrong == 6:
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(100, 10)

    won = all(character in guessed for character in word)

# Final screen
info.clear()
info.goto(-300, -200)
info.write("Word: " + " ".join(word), font=("Arial", 18, "normal"))
info.goto(-300, -305)

if won:
    info.write(
        "Winner winner chicken dinner! Word is: " + word,
        font=("Arial", 18, "bold")
    )
else:
    info.write(
        "You lose. Word was: " + word,
        font=("Arial", 18, "bold")
    )

screen.update()
turtle.done()
