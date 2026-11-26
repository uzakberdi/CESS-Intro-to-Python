import turtle


screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Gallow in turtle")
screen.bgcolor("pink")
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

# ===== Game settings =====
MAX_WRONG = 6         
word = "fun".lower()   # task #1: insert your own word (any word you want)
 
guessed = ""
wrong = 0
won = False

for attempt in range(MAX_WRONG):       # task #2: how many attempts should be?🤔 
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

    screen.update()        

    
    letter = screen.textinput("Hello", "Your letter:")
    if letter is None:
        letter = ""
    letter = letter.strip().lower()

    
    if letter in guessed:
        info.goto(-300, -270)
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

        elif wrong == 4:         # task #3: I suddenly forgot how to draw right hand, will you help?          
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
    for letter in word:
        if letter not in guessed:
            win = False
    if win:
        won = True
        break


info.goto(-300, -305)
if won:
    info.write("Bravo, you won! The Word is: " + word, font=("Arial", 15, "bold"))
else:
    info.write("You lose. The Word was: " + word, font=("Arial", 15, "bold"))

screen.update()
turtle.done()