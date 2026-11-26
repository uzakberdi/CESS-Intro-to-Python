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

"""
HANGMAN - detailed turtle edition

Controls:
    A-Z        guess a letter (or click the on-screen keys)
    SPACE      hint: reveals a letter but costs one life
    ENTER      new word (after the game ends, or any time)
    ESC        quit
"""

import random
import string
import turtle

# --------------------------------------------------------------------------
# Settings
# --------------------------------------------------------------------------
WIDTH, HEIGHT = 1000, 700
MAX_WRONG = 8            # head, face, body, 2 arms, 2 legs, final "dead" face
PANEL_CX = 250           # horizontal centre of the right-hand panel
KEY = 46                 # on-screen key size
GAP = 6

SKIN = '#f5cba7'
SKIN_EDGE = '#a1704a'
WOOD = '#8d6e63'
WOOD_DARK = '#5d4037'

WORDS = {
    'Animals':   ['ducks', 'elephant', 'giraffe', 'penguin', 'dolphin', 'kangaroo', 'octopus'],
    'Countries': ['canada', 'brazil', 'germany', 'mexico', 'portugal', 'iceland'],
    'Food':      ['pancake', 'burger', 'chicken', 'noodles', 'avocado', 'broccoli'],
    'Computers': ['python', 'keyboard', 'monitor', 'internet', 'program', 'turtle'],
    'Space':     ['planet', 'galaxy', 'rocket', 'asteroid', 'comet', 'mercury'],
}

# --------------------------------------------------------------------------
# Screen and turtles
# --------------------------------------------------------------------------
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Hangman')
screen.bgcolor('#87ceeb')
screen.tracer(0)

scene = turtle.Turtle()   # static background + gallows
fig = turtle.Turtle()     # the hanged man (grows with every mistake)
hud = turtle.Turtle()     # everything that changes every turn
for t in (scene, fig, hud):
    t.hideturtle()
    t.penup()
    t.speed(0)


# --------------------------------------------------------------------------
# Drawing helpers
# --------------------------------------------------------------------------
def lerp_color(c1, c2, k):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(int(a[i] + (b[i] - a[i]) * k) for i in range(3))


def line(t, x1, y1, x2, y2, color='black', width=2):
    t.penup()
    t.goto(x1, y1)
    t.color(color)
    t.pensize(width)
    t.pendown()
    t.goto(x2, y2)
    t.penup()


def rect(t, x, y, w, h, fill, outline=None, width=1):
    """Filled rectangle, (x, y) is the bottom-left corner."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(outline or fill, fill)
    t.pensize(width)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.penup()


def disc(t, x, y, r, fill, outline=None, width=1):
    t.penup()
    t.goto(x, y - r)
    t.setheading(0)
    t.color(outline or fill, fill)
    t.pensize(width)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()


def write(t, x, y, s, size=14, color='white', weight='normal', align='center'):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.write(s, align=align, font=('Arial', size, weight))


def cloud(x, y, s=1.0):
    for dx, dy, r in ((0, 0, 22), (26, 8, 28), (56, 0, 22), (28, -8, 22)):
        disc(scene, x + dx * s, y + dy * s, r * s, 'white')


def bird(x, y):
    line(scene, x, y, x + 8, y - 6, '#2c3e50', 2)
    line(scene, x + 8, y - 6, x + 16, y, '#2c3e50', 2)
    line(scene, x + 16, y, x + 24, y - 6, '#2c3e50', 2)
    line(scene, x + 24, y - 6, x + 32, y, '#2c3e50', 2)


# --------------------------------------------------------------------------
# Static scene: sky, sun, hills, ground, tree, gallows, panel
# --------------------------------------------------------------------------
def draw_scene():
    # sky gradient
    bands = 20
    band_h = HEIGHT / bands
    for i in range(bands):
        col = lerp_color('#4a90d9', '#d6eeff', i / (bands - 1))
        rect(scene, -500, 350 - (i + 1) * band_h, WIDTH, band_h + 1, col)

    # sun with rays
    sx, sy = -30, 295
    for k in range(12):
        scene.penup()
        scene.goto(sx, sy)
        scene.setheading(k * 30)
        scene.forward(34)
        scene.pendown()
        scene.color('#ffd54f')
        scene.pensize(3)
        scene.forward(14)
        scene.penup()
    disc(scene, sx, sy, 28, '#ffd54f', '#ffb300', 2)

    # clouds and birds
    cloud(-450, 190, 0.9)
    cloud(-70, 175, 0.7)
    bird(-330, 130)
    bird(-290, 160)

    # hills
    disc(scene, -440, -380, 260, '#7cb342')
    disc(scene, -200, -420, 300, '#8bc34a')

    # ground
    rect(scene, -500, -350, 505, 150, '#4e9a2f')
    rect(scene, -500, -210, 505, 10, '#3f7f26')
    rnd = random.Random(7)
    for _ in range(70):
        gx = rnd.randint(-495, 0)
        gy = rnd.randint(-345, -215)
        line(scene, gx, gy, gx - 3, gy + 9, '#3a7a24', 2)
        line(scene, gx, gy, gx + 3, gy + 8, '#3a7a24', 2)

    # tree
    rect(scene, -472, -200, 24, 110, '#6d4c41', '#4e342e', 2)
    for dx, dy, r in ((-460, -50, 48), (-490, -85, 36), (-430, -85, 36), (-460, -20, 36)):
        disc(scene, dx, dy, r, '#2e7d32', '#1b5e20', 2)

    # gallows: platform
    rect(scene, -420, -230, 320, 30, WOOD, WOOD_DARK, 3)
    for px in range(-380, -100, 40):
        line(scene, px, -230, px, -200, WOOD_DARK, 1)
    # pole
    rect(scene, -330, -200, 30, 450, WOOD, WOOD_DARK, 3)
    for gy in range(-170, 240, 55):
        line(scene, -322, gy, -322, gy + 30, WOOD_DARK, 1)
        line(scene, -310, gy + 20, -310, gy + 45, WOOD_DARK, 1)
    # top beam
    rect(scene, -330, 220, 230, 30, WOOD, WOOD_DARK, 3)
    for gx in range(-300, -110, 45):
        line(scene, gx, 228, gx + 25, 228, WOOD_DARK, 1)
        line(scene, gx + 10, 240, gx + 35, 240, WOOD_DARK, 1)
    # diagonal brace
    line(scene, -300, 150, -235, 220, WOOD_DARK, 16)
    line(scene, -300, 150, -235, 220, WOOD, 10)
    # bolts
    for bx, by in ((-315, -190), (-315, 235), (-115, 235)):
        disc(scene, bx, by, 3, '#cfd8dc', '#455a64', 1)

    # rope and knot
    line(scene, -160, 220, -160, 172, '#d2b48c', 6)
    for ty in range(214, 176, -8):
        line(scene, -164, ty, -156, ty - 4, '#8d6e3b', 1)
    disc(scene, -160, 170, 6, '#c9a66b', '#8d6e3b', 2)

    # right-hand panel
    rect(scene, 5, -335, 490, 665, '#1b2838', '#0d1520', 4)
    screen.update()


# --------------------------------------------------------------------------
# The hanged man, built one stage per mistake
# --------------------------------------------------------------------------
def smile(t, color, width):
    t.penup()
    t.goto(-172, 132)
    t.setheading(-60)
    t.color(color)
    t.pensize(width)
    t.pendown()
    t.circle(12, 120)
    t.penup()


def frown(t, color, width):
    t.penup()
    t.goto(-172, 124)
    t.setheading(60)
    t.color(color)
    t.pensize(width)
    t.pendown()
    t.circle(-12, 120)
    t.penup()


def draw_stage(n):
    if n == 1:      # head
        disc(fig, -160, 140, 30, SKIN, SKIN_EDGE, 3)
    elif n == 2:    # face
        disc(fig, -171, 148, 4, 'black')
        disc(fig, -149, 148, 4, 'black')
        line(fig, -178, 158, -165, 156, '#5d4037', 3)     # eyebrows
        line(fig, -155, 156, -142, 158, '#5d4037', 3)
        line(fig, -160, 146, -160, 138, SKIN_EDGE, 2)     # nose
        smile(fig, 'black', 3)
    elif n == 3:    # torso
        rect(fig, -178, 10, 36, 98, '#3498db', '#21618c', 3)
        for by in (88, 62, 36):
            disc(fig, -160, by - 10 + 10, 3, 'white')
    elif n == 4:    # left arm
        line(fig, -176, 98, -212, 42, '#21618c', 14)
        line(fig, -176, 98, -212, 42, '#3498db', 10)
        disc(fig, -214, 38, 8, SKIN, SKIN_EDGE, 2)
    elif n == 5:    # right arm
        line(fig, -144, 98, -108, 42, '#21618c', 14)
        line(fig, -144, 98, -108, 42, '#3498db', 10)
        disc(fig, -106, 38, 8, SKIN, SKIN_EDGE, 2)
    elif n == 6:    # left leg + shoe
        line(fig, -168, 12, -188, -72, '#2c3e50', 16)
        rect(fig, -206, -86, 32, 14, '#111111', '#000000', 2)
    elif n == 7:    # right leg + shoe
        line(fig, -152, 12, -132, -72, '#2c3e50', 16)
        rect(fig, -150, -86, 32, 14, '#111111', '#000000', 2)
    elif n == 8:    # dead face: X eyes + frown
        disc(fig, -171, 148, 6, SKIN)
        disc(fig, -149, 148, 6, SKIN)
        for ex in (-171, -149):
            line(fig, ex - 5, 153, ex + 5, 143, 'black', 3)
            line(fig, ex - 5, 143, ex + 5, 153, 'black', 3)
        smile(fig, SKIN, 6)
        frown(fig, 'black', 3)
    screen.update()


# --------------------------------------------------------------------------
# Game state
# --------------------------------------------------------------------------
word = ''
category = ''
guessed = set()
wrong = 0
phase = 'playing'        # 'playing', 'won', 'lost'
message = ''
wins = 0
losses = 0
last_word = ''

# on-screen keyboard geometry
key_boxes = {}
for row_letters, row_y in (('abcdefghi', 0), ('jklmnopqr', -52), ('stuvwxyz', -104)):
    n = len(row_letters)
    total = n * KEY + (n - 1) * GAP
    x0 = PANEL_CX - total / 2
    for i, ch in enumerate(row_letters):
        key_boxes[ch] = (x0 + i * (KEY + GAP), row_y)

HINT_BOX = (19, -250, 218, 46)
NEW_BOX = (263, -250, 218, 46)


def inside(box, x, y):
    bx, by, bw, bh = box
    return bx <= x <= bx + bw and by <= y <= by + bh


# --------------------------------------------------------------------------
# HUD (redrawn after every action)
# --------------------------------------------------------------------------
def draw_hud():
    hud.clear()

    # title and category
    write(hud, PANEL_CX, 280, 'H A N G M A N', 30, '#ffd54f', 'bold')
    write(hud, PANEL_CX, 240, 'Category: ' + category, 16, '#aed6f1', 'bold')
    write(hud, PANEL_CX, 205, 'Word length: ' + str(len(word)) + ' letters', 12, '#85929e')

    # word slots
    n = len(word)
    total = n * 60 - 10
    start = PANEL_CX - total / 2
    for i, ch in enumerate(word):
        x = start + i * 60
        line(hud, x, 118, x + 50, 118, 'white', 4)
        if ch in guessed:
            write(hud, x + 25, 124, ch.upper(), 34, 'white', 'bold')
        elif phase == 'lost':
            write(hud, x + 25, 124, ch.upper(), 34, '#ff6b6b', 'bold')

    # lives
    write(hud, 19, 66, 'Lives:', 15, 'white', 'bold', 'left')
    for i in range(MAX_WRONG):
        alive = i < MAX_WRONG - wrong
        disc(hud, 120 + i * 40, 74, 13,
             '#e74c3c' if alive else '#34495e',
             '#922b21' if alive else '#2c3e50', 2)

    # keyboard
    for ch, (kx, ky) in key_boxes.items():
        if ch in guessed and ch in word:
            fill, edge = '#27ae60', '#1e8449'
        elif ch in guessed:
            fill, edge = '#c0392b', '#922b21'
        else:
            fill, edge = '#34495e', '#5d6d7e'
        rect(hud, kx, ky, KEY, KEY, fill, edge, 3)
        write(hud, kx + KEY / 2, ky + 11, ch.upper(), 18, 'white', 'bold')

    # message line
    write(hud, PANEL_CX, -153, message, 15, '#ffe082', 'bold')

    # buttons
    can_hint = phase == 'playing' and wrong < MAX_WRONG - 1
    for box, label, ok in ((HINT_BOX, 'Hint (-1 life)  [SPACE]', can_hint),
                           (NEW_BOX, 'New word  [ENTER]', True)):
        bx, by, bw, bh = box
        rect(hud, bx, by, bw, bh, '#2e86c1' if ok else '#2c3e50',
             '#1b4f72' if ok else '#212f3d', 3)
        write(hud, bx + bw / 2, by + 14, label, 13, 'white' if ok else '#7f8c8d', 'bold')

    # score
    write(hud, PANEL_CX, -305, 'Wins: %d     Losses: %d' % (wins, losses), 14, '#d5d8dc', 'bold')

    # end-of-game banner over the scene
    if phase != 'playing':
        rect(hud, -380, 262, 300, 72, '#1b2838', '#0d1520', 4)
        if phase == 'won':
            write(hud, -230, 296, 'YOU WIN!', 28, '#58d68d', 'bold')
        else:
            write(hud, -230, 296, 'GAME OVER', 28, '#ff6b6b', 'bold')
        write(hud, -230, 270, 'The word was: ' + word.upper(), 13, 'white', 'bold')

    screen.update()


# --------------------------------------------------------------------------
# Game logic
# --------------------------------------------------------------------------
def new_game():
    global word, category, guessed, wrong, phase, message, last_word
    while True:
        category = random.choice(list(WORDS))
        word = random.choice(WORDS[category])
        if word != last_word:
            break
    last_word = word
    guessed = set()
    wrong = 0
    phase = 'playing'
    message = 'Pick a letter!'
    fig.clear()
    draw_hud()


def check_end():
    """Update phase after any change; returns True if the game finished."""
    global phase, wins, losses
    if all(ch in guessed for ch in word):
        phase = 'won'
        wins += 1
        return True
    if wrong >= MAX_WRONG:
        phase = 'lost'
        losses += 1
        return True
    return False


def guess(letter):
    global wrong, message
    if phase != 'playing':
        return
    if letter in guessed:
        message = 'You already tried "%s"!' % letter.upper()
    elif letter in word:
        guessed.add(letter)
        count = word.count(letter)
        message = 'Nice! "%s" appears %d time%s.' % (letter.upper(), count, 's' if count > 1 else '')
        if check_end():
            message = 'You saved him! Press ENTER for a new word.'
    else:
        guessed.add(letter)
        wrong += 1
        message = 'No "%s" in the word...' % letter.upper()
        draw_stage(wrong)
        if check_end():
            message = 'Too late... Press ENTER for a new word.'
    draw_hud()


def hint():
    global wrong, message
    if phase != 'playing':
        return
    if wrong >= MAX_WRONG - 1:
        message = 'Too risky - a hint costs a life!'
        draw_hud()
        return
    hidden = sorted(set(word) - guessed)
    if not hidden:
        return
    letter = random.choice(hidden)
    guessed.add(letter)
    wrong += 1
    draw_stage(wrong)
    message = 'Hint: "%s" revealed (-1 life)' % letter.upper()
    if check_end():
        message = 'You saved him! Press ENTER for a new word.'
    draw_hud()


def on_click(x, y):
    if inside(NEW_BOX, x, y):
        new_game()
        return
    if inside(HINT_BOX, x, y):
        hint()
        return
    for ch, (kx, ky) in key_boxes.items():
        if inside((kx, ky, KEY, KEY), x, y):
            guess(ch)
            return
    if phase != 'playing':
        new_game()


def quit_game():
    screen.bye()


# --------------------------------------------------------------------------
# Start
# --------------------------------------------------------------------------
draw_scene()
new_game()

for c in string.ascii_lowercase:
    screen.onkeypress(lambda ch=c: guess(ch), c)
    screen.onkeypress(lambda ch=c: guess(ch), c.upper())
screen.onkeypress(hint, 'space')
screen.onkeypress(new_game, 'Return')
screen.onkeypress(quit_game, 'Escape')
screen.onclick(on_click)
screen.listen()

screen.mainloop()
