import turtle


screen = turtle.Screen()
screen.setup(700, 750)
screen.title("Squid game")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.pensize(4)
pen.penup()
pen.goto(0, 100)
pen.pendown()
pen.goto(0, 150)
pen.goto(80, 150)
pen.goto(80, 120)

guess = turtle.Turtle()
guess.hideturtle()
guess.penup()

word = "ducks"
guessed = ""
wrong = 0
won = False

while wrong < 6 and not won:
    display = "".join(letter if letter in guessed else "_" for letter in word)
    guess.clear()
    guess.goto(-300, -200)
    guess.write("Word: " + display, font=("Arial", 18, "bold"))
    guess.goto(-300, -235)
    guess.write("Wrong guesses: " + str(wrong) + " / 6", font=("Arial", 15, "bold"))
    screen.update()

    letter = screen.textinput("Game name", "Enter one letter")
    if letter is None:
        break
    letter = letter.strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        guess.goto(-300, -270)
        guess.write("Enter a single letter.", font=("Arial", 12, "normal"))
        screen.update()
        continue

    if letter in guessed:
        guess.goto(-300, -270)
        guess.write("You already entered that letter.", font=("Arial", 12, "normal"))
        screen.update()
        continue

    guessed += letter
    if letter not in word:
        wrong += 1
        pen.penup()

        if wrong == 1:
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(15)
        elif wrong == 2:
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)
        elif wrong == 3:
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)
        elif wrong == 4:
            pen.goto(80, 40)
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

guess.clear()
guess.goto(-300, -200)
if won:
    guess.write("You win! Word: " + word, font=("Arial", 18, "bold"))
elif wrong == 6:
    guess.write("You lose. Word was: " + word, font=("Arial", 18, "bold"))
else:
    guess.write("Game canceled. Word was: " + word, font=("Arial", 18, "bold"))

screen.update()
turtle.done()

Dancan = 202652080007
