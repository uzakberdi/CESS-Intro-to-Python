import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Gallow in turtle")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.speed(0)

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

my_name = "abubakar abdinur hersi 202651620015"
word = my_name
guessed = ""
wrong = 0
won = False

def wrap_text(text, width):
    lines = []
    for i in range(0, len(text), width):
        lines.append(text[i:i+width])
    return lines

for attempt in range(6):
    display = ""
    for ch in word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    info.clear()
    lines = wrap_text(display, 40)
    y = -180
    info.goto(-300, y)
    info.write("Word:", font=("Arial", 16, "normal"))
    for line in lines:
        y -= 22
        info.goto(-300, y)
        info.write(line, font=("Arial", 14, "normal"))

    info.goto(-300, y - 30)
    info.write("Mistakes: " + str(wrong) + " / 6", font=("Arial", 14, "normal"))

    screen.update()

    letter = screen.textinput("Gallow", "Your letter:")
    if letter is None:
        letter = ""
    letter = letter.strip().lower()

    if letter in guessed:
        info.goto(-300, y - 60)
        info.write("You've already entered this letter!", font=("Arial", 12, "italic"))
    elif letter in word:
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

    win = True
    for ch in word:
        if ch not in guessed:
            win = False
    if win:
        won = True
        break

info.goto(-300, -330)
if won:
    info.write("Winner winner chicken dinner! Word is: " + word, font=("Arial", 14, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Arial", 14, "bold"))

screen.update()
turtle.done()