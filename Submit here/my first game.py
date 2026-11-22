import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("It is my first game")
screen.bgcolor("blue")
screen.tracer(0)

pen = turtle.Turtle()
pen.pensize(4)

# Draw the gallows
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

# Text display
guess = turtle.Turtle()
guess.hideturtle()
guess.penup()

word = "cows"
guessed = ""
wrong = 0
win = False

while wrong < 6 and not win:
    # Show guessed letters and blanks
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    guess.clear()
    guess.goto(-300, -200)
    guess.write("Word: " + display, font=("Arial", 18, "normal"))
    guess.goto(-300, -235)
    guess.write("Wrong guesses: " + str(wrong) + " / 6",
                font=("Arial", 15, "bold"))
    screen.update()

    # Ask for a letter
    letter = screen.textinput("Game name", "Enter a letter:")

    if letter is None:
        break

    letter = letter.strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        guess.goto(-300, -270)
        guess.write("Please enter one letter.", font=("Arial", 12, "normal"))
        screen.update()
        continue

    if letter in guessed:
        guess.goto(-300, -270)
        guess.write("You already entered this letter!",
                    font=("Arial", 12, "normal"))
        screen.update()
        continue

    guessed += letter

    if letter not in word:
        wrong += 1
        pen.penup()

        if wrong == 1:          # Head
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(15)
        elif wrong == 2:        # Body
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)
        elif wrong == 3:        # Left arm
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)
        elif wrong == 4:        # Right arm
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(100, 50)
        elif wrong == 5:        # Left leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(60, 10)
        elif wrong == 6:        # Right leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(100, 10)

    win = all(letter in guessed for letter in word)

# Show the final result
display = ""
for letter in word:
    if letter in guessed:
        display += letter + " "
    else:
        display += "_ "

guess.clear()
guess.goto(-300, -200)
guess.write("Word: " + display, font=("Arial", 18, "normal"))
guess.goto(-300, -235)
guess.write("Wrong guesses: " + str(wrong) + " / 6",
            font=("Arial", 15, "bold"))
guess.goto(-300, -305)

if win:
    guess.write("You win! The word was: " + word,
                font=("Arial", 18, "bold"))
else:
    guess.write("You lose! The word was: " + word,
                font=("Arial", 18, "bold"))

screen.update()
turtle.done()