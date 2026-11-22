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


youssof = 202553080037

# ===== Game settings =====
word = "yoco"   # task #1: insert your own word (any word you want)
guessed = ""
wrong = 0
won = False

for attempt in range(5):     # task #2: how many attempts should be?🤔
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
    info.write("Mistakes: " + str(wrong) + " / 6", font=("Arial", 14, "normal"))

    screen.update()        # ← showing all before the second word enter

    # --- 2. word enter ---
    letter = screen.textinput("Gallow", "Your letter:")
    if letter is None:
        letter = ""
    letter = letter.strip().lower()

    # --- 3. cehcking ---
    if letter in guessed:
        info.goto(-300, -270)
        info.write("You've already entered this letter!", font=("Arial", 12, "italic"))
    elif letter in word:
        guessed += letter
    else:
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
        elif wrong == 4:                  # task #3: I suddenly forgot how to draw right hand, will you help?
            pen.goto(80,70)
            pen.pendown()
            pen.goto(100,50)
            
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
info.goto(-300, -305)
if won:
    info.write("Winner winner chicken dinner! Word is: " + word, font=("Arial", 18, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Arial", 18, "bold"))

screen.update()
turtle.done()