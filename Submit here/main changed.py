import turtle

win_screen = turtle.Screen()
win_screen.setup(700, 700)
win_screen.title("Hangman Game")
win_screen.bgcolor("green")
win_screen.tracer(0)

artist = turtle.Turtle()
artist.hideturtle()
artist.pensize(3)
artist.speed(0)


artist.penup()
artist.goto(-100, -100)
artist.pendown()
artist.goto(100, -100)
artist.penup()
artist.goto(0, -100)
artist.pendown()
artist.goto(0, 150)
artist.goto(80, 150)
artist.goto(80, 120)

hud = turtle.Turtle()
hud.hideturtle()
hud.penup()

alert = turtle.Turtle()
alert.hideturtle()
alert.penup()
alert.color("red")

secret = "rabbit"
found_letters = []
used_letters = []
mistakes = 0
victory = False


def draw_body_part(step):
    artist.penup()
    if step == 1:
        artist.goto(80, 80)
        artist.pendown()
        artist.circle(20)
    elif step == 2:
        artist.goto(80, 80)
        artist.pendown()
        artist.goto(80, 40)
    elif step == 3:
        artist.goto(80, 70)
        artist.pendown()
        artist.goto(60, 50)
    elif step == 4:
        artist.goto(80, 70)
        artist.pendown()
        artist.goto(100, 50)
    elif step == 5:
        artist.goto(80, 40)
        artist.pendown()
        artist.goto(60, 10)
    elif step == 6:
        artist.goto(80, 40)
        artist.pendown()
        artist.goto(100, 10)


def render_hud():
    masked = " ".join(ch if ch in found_letters else "_" for ch in secret)
    hud.clear()
    hud.goto(-300, -190)
    hud.write("Word: " + masked, font=("Times New Roman", 14, "normal"))
    hud.goto(-300, -220)
    hud.write("Mistakes: " + str(mistakes) + " / 6", font=("Times New Roman", 14, "normal"))
    hud.goto(-300, -250)
    hud.write("Guessed: " + " ".join(used_letters), font=("Times New Roman", 14, "normal"))


def show_alert(message):
    alert.clear()
    alert.goto(0, -285)
    alert.write(message, align="center", font=("Times New Roman", 14, "italic"))
    win_screen.update()


while mistakes < 6:
    render_hud()
    win_screen.update()

    raw_input = win_screen.textinput("Gallow", "Your letter:")
    if raw_input is None:
        break

    char = raw_input.strip().lower()
    if len(char) != 1 or not char.isalpha():
        show_alert("Please enter a single letter!")
        continue

    repeat_mode = None
    if char in used_letters:
        show_alert("You've already entered this letter!")
        choice = win_screen.textinput(
            "Repeated letter",
            "Enter it again or enter a new letter? (again / new)",
        )
        if choice is None:
            break

        repeat_mode = choice.strip().lower()
        if repeat_mode in ("new", "n"):
            second_input = win_screen.textinput("Gallow", "Your new letter:")
            if second_input is None:
                break
            char = second_input.strip().lower()
            if len(char) != 1 or not char.isalpha():
                show_alert("Please enter a single letter!")
                continue
            repeat_mode = None

    alert.clear()

    already_seen = char in used_letters
    if not already_seen:
        used_letters.append(char)

    if char in secret:
        if char not in found_letters:
            found_letters.append(char)
    else:
        if not already_seen or repeat_mode in ("again", "a"):
            mistakes += 1
            draw_body_part(mistakes)

    if all(ch in found_letters for ch in secret):
        victory = True
        break

alert.clear()
render_hud()

hud.goto(-300, -285)
if victory:
    hud.write("Winner winner chicken dinner! Word is: " + secret, font=("Times New Roman", 14, "bold"))
else:
    hud.write("You lose. Word was: " + secret, font=("Times New Roman", 14, "bold"))

win_screen.update()
turtle.done()