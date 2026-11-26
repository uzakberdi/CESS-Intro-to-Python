import turtle

# ---- student details (shown in the title and on the screen) ----
student_name = 'ALLOTEY JESSICA E.A'
student_id = '202453083008'

screen = turtle.Screen()
screen.setup(700, 700)
screen.title('Hangman - ' + student_name + ' - ' + student_id)
screen.bgcolor('white')
screen.tracer(0)

# ---- drawing pen (gallows + body) ----
pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(4)

# base
pen.penup()
pen.goto(-50, -20)
pen.pendown()
pen.goto(50, -20)
# pole
pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.goto(0, 150)
# top beam and rope
pen.goto(80, 150)
pen.goto(80, 110)

# ---- text turtles ----
guess = turtle.Turtle()      # word + status text (cleared every round)
guess.hideturtle()
guess.penup()

info = turtle.Turtle()       # student name / id (written once)
info.hideturtle()
info.penup()
info.goto(-300, 300)
info.write('Name: ' + student_name + '\nID: ' + student_id,
           font=('Arial', 12, 'bold'))

word = 'ducks'
guessed = ''
MAX_WRONG = 6
wrong = 0
win = False
message = ''


def draw_part(n):
    """Draw body part number n (1-6)."""
    pen.penup()
    if n == 1:      # head
        pen.goto(80, 80)
        pen.pendown()
        pen.circle(15)
    elif n == 2:    # body
        pen.goto(80, 80)
        pen.pendown()
        pen.goto(80, 30)
    elif n == 3:    # left arm
        pen.goto(80, 65)
        pen.pendown()
        pen.goto(50, 45)
    elif n == 4:    # right arm
        pen.goto(80, 65)
        pen.pendown()
        pen.goto(110, 45)
    elif n == 5:    # left leg
        pen.goto(80, 30)
        pen.pendown()
        pen.goto(55, -10)
    elif n == 6:    # right leg
        pen.goto(80, 30)
        pen.pendown()
        pen.goto(105, -10)
    pen.penup()


while wrong < MAX_WRONG and not win:
    # build the word display
    display = ''
    for letter in word:
        if letter in guessed:
            display = display + letter + ' '
        else:
            display = display + '_ '

    # redraw status text
    guess.clear()
    guess.goto(-300, -100)
    guess.write(display, font=('Arial', 30, 'bold'))
    guess.goto(-300, -200)
    guess.write('Your letters: ' + guessed, font=('Arial', 12, 'normal'))
    guess.goto(150, -200)
    guess.write('Wrong guesses: ' + str(wrong) + '/' + str(MAX_WRONG),
                font=('Calibri', 15, 'bold'))
    guess.goto(-300, -270)
    guess.write(message, font=('Arial', 12, 'normal'))
    screen.update()

    answer = screen.textinput('Hangman', 'Enter one letter:')
    if answer is None:          # Cancel pressed -> quit
        break
    answer = answer.strip().lower()

    if len(answer) != 1 or not answer.isalpha():
        message = 'Please enter a single letter.'
    elif answer in guessed:
        message = 'You already entered this letter.'
    else:
        guessed = guessed + answer
        if answer in word:
            message = 'Good guess!'
        else:
            wrong = wrong + 1
            message = 'Wrong letter.'
            draw_part(wrong)

    # win check: every letter of the word has been guessed
    win = True
    for letter in word:
        if letter not in guessed:
            win = False

# ---- final screen ----
guess.clear()
guess.goto(-300, -100)
guess.write(' '.join(word), font=('Arial', 30, 'bold'))
guess.goto(-300, -200)
if win:
    guess.write('You win!', font=('Arial', 24, 'bold'))
elif wrong >= MAX_WRONG:
    guess.write('You lose! The word was: ' + word, font=('Arial', 24, 'bold'))
else:
    guess.write('Game cancelled.', font=('Arial', 24, 'bold'))
screen.update()

screen.mainloop()