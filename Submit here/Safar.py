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

stage = turtle.Screen()
stage.setup(700, 700)
stage.title("Word Guess")
stage.bgcolor("red")
stage.tracer(0)

marker = turtle.Turtle()
marker.hideturtle()
marker.pensize(3)
marker.speed(0)


marker.penup()
marker.goto(-100, -100)
marker.pendown()
marker.goto(100, -100)
marker.penup()
marker.goto(0, -100)
marker.pendown()
marker.goto(0, 150)
marker.goto(80, 150)
marker.goto(80, 120)

board = turtle.Turtle()
board.hideturtle()
board.penup()

notice = turtle.Turtle()
notice.hideturtle()
notice.penup()
notice.color("yellow")

target_word = "kazakhstan"
opened = set()
history = []
errors = 0
is_win = False


def paint_limb(error_count):
    marker.penup()
    if error_count == 1:
        marker.goto(80, 80)
        marker.pendown()
        marker.circle(20)
    elif error_count == 2:
        marker.goto(80, 80)
        marker.pendown()
        marker.goto(80, 40)
    elif error_count == 3:
        marker.goto(80, 70)
        marker.pendown()
        marker.goto(60, 50)
    elif error_count == 4:
        marker.goto(80, 70)
        marker.pendown()
        marker.goto(100, 50)
    elif error_count == 5:
        marker.goto(80, 40)
        marker.pendown()
        marker.goto(60, 10)
    elif error_count == 6:
        marker.goto(80, 40)
        marker.pendown()
        marker.goto(100, 10)


def refresh_board():
    progress = " ".join(letter if letter in opened else "_" for letter in target_word)
    board.clear()
    board.goto(-300, -190)
    board.write("Word: " + progress, font=("Times New Roman", 14, "normal"))
    board.goto(-300, -220)
    board.write("Mistakes: " + str(errors) + " / 6", font=("Times New Roman", 14, "normal"))
    board.goto(-300, -250)
    board.write("Guessed: " + " ".join(history), font=("Times New Roman", 14, "normal"))


def display_notice(text):
    notice.clear()
    notice.goto(0, -285)
    notice.write(text, align="center", font=("Times New Roman", 14, "italic"))
    stage.update()



while errors < 6:
    refresh_board()
    stage.update()

    typed = stage.textinput("Gallow", "Your letter:")
    if typed is None:
        break

    symbol = typed.strip().lower()
    if len(symbol) != 1 or not symbol.isalpha():
        display_notice("Please enter a single letter!")
        continue

    reenter_mode = None
    if symbol in history:
        display_notice("You've already entered this letter!")
        reply = stage.textinput(
            "Repeated letter",
            "Enter it again or enter a new letter? (again / new)",
        )
        if reply is None:
            break

        reenter_mode = reply.strip().lower()
        if reenter_mode in ("new", "n"):
            next_typed = stage.textinput("Gallow", "Your new letter:")
            if next_typed is None:
                break
            symbol = next_typed.strip().lower()
            if len(symbol) != 1 or not symbol.isalpha():
                display_notice("Please enter a single letter!")
                continue
            reenter_mode = None

    notice.clear()

    was_used = symbol in history
    if not was_used:
        history.append(symbol)

    if symbol in target_word:
        opened.add(symbol)
    else:
        if not was_used or reenter_mode in ("again", "a"):
            errors += 1
            paint_limb(errors)

    if all(letter in opened for letter in target_word):
        is_win = True
        break

notice.clear()
refresh_board()

board.goto(-300, -285)
if is_win:
    board.write(
        "Winner winner chicken dinner! Word is: " + target_word,
        font=("Times New Roman", 14, "bold"),
    )
else:
    board.write(
        "You lose. Word was: " + target_word,
        font=("Times New Roman", 14, "bold"),
    )

stage.update()
turtle.done()

Safar = 202653300012



# ===== Game settings =====
word = "Vabe"   # task #1: insert your own word (any word you want)
guessed = ""
wrong = 0
won = False

for attempt in range(6):     # task #2: how many attempts should be?🤔
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
