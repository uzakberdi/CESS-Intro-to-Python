import turtle

screen = turtle.Screen()
screen.setup(700,700)
screen.title('10.000 chest to Token')
screen.bgcolor('yellow')
screen.tracer(0)

pen= turtle.Turtle()
pen.pensize(5)

pen.penup()
pen.goto(100,-100)
pen.pendown()
pen.goto(100,-100)

pen.penup()
pen.goto(0,100)
pen.pendown()
pen.goto(0,150)
pen.goto(80,150)
pen.goto(80,120)

guess= turtle.Turtle()
guess.penup()

word = 'Token'
guessed = ''

wrong = 0 
win = False

for attemps in range(6):
    display = ''
    for letter in word:
        if letter in guessed:
            display = display + letter
        else:
            display = display + '_'
    
    guess.clear()
    guess.goto(-300, -200)
    guess.write('Your letter: ' + guessed, font = ('Arial', 12, 'normal'))
    guess.goto(-300, -250)
    guess.write('your wrong guessed ' + str(wrong) + '/6', font = ('Calibri', 15, 'bold'))

    screen.update()

    letter = screen.textinput('Letter you enter to game', 'Enter a letter: ')
    if letter is None:
        letter = ''
    letter = letter.strip().lower()


    if letter in guessed:
        guess.goto(-300, -270)
        guess.write('You already guessed that letter!', font = ('Arial', 12, 'normal'))
    else:
        wrong += 1
        pen.penup()

        if wrong == 1:
            pen.goto(80,80)
            pen.pendown()
            pen.circle(15)
        elif wrong == 2:
            pen.goto(80,80)
            pen.pendown()
            pen.goto(80,40)
        elif wrong == 3:
            pen.goto(80,40)
            pen.pendown()
            pen.goto(60,20)
        elif wrong == 4:
            pen.goto(80,40)
            pen.pendown()
            pen.goto(100,20)
        elif wrong == 5:
            pen.goto(80,40)
            pen.pendown()
            pen.goto(60,0)
        elif wrong == 6:
            pen.goto(80,40)
            pen.pendown()
            pen.goto(100,0)
            guess.goto(-300, -300)
            guess.write('You lost! The word was: ' + word, font = ('Arial', 12, 'normal'))
            break

    Meiir = 202553080065

    










print('67')

turtle.done()