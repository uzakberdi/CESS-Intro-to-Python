import turtle
screen = turtle.Screen()
print('Hello World')
screen.setup(700, 700)
screen.title('it is my first game')
screen.bgcolor('green')
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
guess.penup()
guessed = turtle.Turtle()
guessed.penup()

word = 'ducks'
guessed_letters = ''
wrong = 0

for attempts in range(6):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display = display + letter
        else:
            display = display + '-'

    guess.clear()
    guess.goto(-300, -200)
    guess.write('your letter: ' + display, font=('Arial', 20, 'normal'))

    guessed.clear()
    guessed.goto(-300, -230)
    guessed.write('your wrong guessed: ' + str(wrong) + ' / 6', font=('Arial', 20, 'normal'))
    screen.update()

    letter = screen.textinput('Letter you enter to game', 'Enter a letter:')
    if letter is None:
        letter = ''
    letter = letter.strip().lower()

    if letter in guessed_letters:
        guess.goto(-300, -270)
        guess.write('You already entered this letter', font=('Arial', 20, 'normal'))
    else:
        guessed_letters = guessed_letters + letter
        if letter not in word:
            wrong = wrong + 1
            pen.penup()
            if wrong == 1:
                pen.goto(80, 80)
                pen.pendown()
                pen.circle(15)
            elif wrong == 2:
                pen.goto(80, 65)
                pen.pendown()
                pen.goto(80, 30)
            elif wrong == 3:
                pen.goto(80, 55)
                pen.pendown()
                pen.goto(60, 40)
            elif wrong == 4:
                pen.goto(80, 55)
                pen.pendown()
                pen.goto(100, 40)
            elif wrong == 5:
                pen.goto(80, 30)
                pen.pendown()
                pen.goto(60, 10)
            elif wrong == 6:
                pen.goto(80, 30)
                pen.pendown()
                pen.goto(100, 10)

screen.update()
screen.mainloop()
## AZIZ AMMARA = 202652120004