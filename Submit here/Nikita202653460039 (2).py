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

import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("It is my second game")
screen.bgcolor("grey")
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

status = turtle.Turtle()
status.hideturtle()
status.penup()
status.color("red")

word = "sixseven"
guessed = ""  
tried = []  
wrong = 0
won = False

# Replaced `for attempt in range(6)` with `while wrong < 6` because the game limit
# is 6 wrong guesses rather than 6 total turns, and correct guesses shouldn't consume a mistake life.
while wrong < 6:
    display = ""
    for ch in word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    info.clear()
    info.goto(-300, -190)
    info.write("Word: " + display, font=("Times New Roman", 14, "normal"))
    info.goto(-300, -220)
    info.write("Mistakes: " + str(wrong) + " / 6", font=("Times New Roman", 14, "normal"))
    info.goto(-300, -250)
    info.write("Guessed: " + " ".join(tried), font=("Times New Roman", 14, "normal"))

    screen.update()

    letter = screen.textinput("Gallow", "Your letter:")
    if letter is None:
        break

    letter = letter.strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        status.clear()
        status.goto(0, -285)
        status.write(
            "Please enter a single letter!",
            align="center",
            font=("Times New Roman", 14, "italic"),
        )
        screen.update()
        continue

    repeat_choice = None
    if letter in tried:
        status.clear()
        status.goto(0, -285)
        status.write(
            "You've already entered this letter!",
            align="center",
            font=("Times New Roman", 14, "italic"),
        )
        screen.update()

        answer = screen.textinput(
            "Repeated letter",
            "Enter it again or enter a new letter? (again / new)",
        )
        if answer is None:
            break
        repeat_choice = answer.strip().lower()

        if repeat_choice in ("new", "n"):
            new_letter = screen.textinput("Gallow", "Your new letter:")
            if new_letter is None:
                break
            new_letter = new_letter.strip().lower()
            if len(new_letter) != 1 or not new_letter.isalpha():
                status.clear()
                status.goto(0, -285)
                status.write(
                    "Please enter a single letter!",
                    align="center",
                    font=("Times New Roman", 14, "italic"),
                )
                screen.update()
                continue
            letter = new_letter
            repeat_choice = None

    status.clear()

    if letter not in tried:
        tried.append(letter)

    if letter in word:
        if letter not in guessed:
            guessed += letter
    else:
        if letter not in tried[:-1] or repeat_choice in ("again", "a"):
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

status.clear()

final_display = " ".join(ch if ch in guessed else "_" for ch in word)
info.clear()
info.goto(-300, -190)
info.write("Word: " + final_display, font=("Times New Roman", 14, "normal"))
info.goto(-300, -220)
info.write("Mistakes: " + str(wrong) + " / 6", font=("Times New Roman", 14, "normal"))

info.goto(-300, -285)
if won:
    info.write("Winner! Word is: " + word, font=("Times New Roman", 14, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Times New Roman", 14, "bold"))

screen.update()
turtle.done()

Nikita = 202653460039



# ===== Game settings =====
word = ""   # task #1: insert your own word (any word you want)
guessed = "car"
wrong = 0
won = False

for attempt in range(8):     # task #2: how many attempts should be?🤔
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
        elif wrong == 4:   # task #3: I suddenly forgot how to draw right hand, will you help?
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
info.goto(-300, -305)
if won:
    info.write("Winner winner chicken dinner! Word is: " + word, font=("Arial", 18, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Arial", 18, "bold"))

screen.update()
turtle.done()
