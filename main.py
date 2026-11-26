import pygame
import random
import sys

# ============================
# 1. INITIALIZE PYGAME
# ============================
pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game - Hangman")

clock = pygame.time.Clock()

# ============================
# 2. COLORS
# ============================
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
RED = (220, 0, 0)
BLUE = (0, 80, 200)
GRAY = (120, 120, 120)

# ============================
# 3. FONTS
# ============================
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 20)
title_font = pygame.font.SysFont("Arial", 38, bold=True)

# ============================
# 4. GAME VARIABLES
# ============================
word = "PIGS"
guessed = []
wrong = 0
max_wrong = 6

win = False
game_over = False

# ============================
# 5. DRAW TEXT FUNCTION
# ============================
def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


# ============================
# 6. DRAW GALLOWS
# ============================
def draw_gallows():
    # Base
    pygame.draw.line(screen, BLACK, (150, 500), (400, 500), 5)

    # Vertical pole
    pygame.draw.line(screen, BLACK, (200, 500), (200, 100), 5)

    # Top beam
    pygame.draw.line(screen, BLACK, (200, 100), (380, 100), 5)

    # Rope
    pygame.draw.line(screen, BLACK, (380, 100), (380, 150), 5)


# ============================
# 7. DRAW HANGMAN
# ============================
def draw_hangman(wrong):
    # Head
    if wrong >= 1:
        pygame.draw.circle(screen, BLACK, (380, 180), 30, 5)

    # Body
    if wrong >= 2:
        pygame.draw.line(screen, BLACK, (380, 210), (380, 330), 5)

    # Left arm
    if wrong >= 3:
        pygame.draw.line(screen, BLACK, (380, 240), (330, 280), 5)

    # Right arm
    if wrong >= 4:
        pygame.draw.line(screen, BLACK, (380, 240), (430, 280), 5)

    # Left leg
    if wrong >= 5:
        pygame.draw.line(screen, BLACK, (380, 330), (340, 390), 5)

    # Right leg
    if wrong >= 6:
        pygame.draw.line(screen, BLACK, (380, 330), (420, 390), 5)


# ============================
# 8. DISPLAY THE WORD
# ============================
def display_word():
    result = ""

    for letter in word:
        if letter in guessed:
            result += letter + " "
        else:
            result += "_ "

    return result.strip()


# ============================
# 9. RESET GAME
# ============================
def reset_game():
    global word, guessed, wrong, win, game_over

    word = random.choice(["PIGS", "DUCKS", "APPLE", "TIGER", "PYTHON"])
    guessed = []
    wrong = 0
    win = False
    game_over = False


# ============================
# 10. MAIN GAME LOOP
# ============================
running = True

while running:

    # Background
    screen.fill(LIGHT_BLUE)

    # Draw title
    draw_text("HANGMAN GAME", title_font, BLUE, 150, 30)

    # Draw gallows
    draw_gallows()

    # Draw Hangman
    draw_hangman(wrong)

    # Display word
    draw_text("Word: " + display_word(), font, BLACK, 50, 120)

    # Display guessed letters
    draw_text("Guessed: " + " ".join(guessed), small_font, BLACK, 50, 180)

    # Display wrong guesses
    draw_text(
        f"Wrong guesses: {wrong}/{max_wrong}",
        small_font,
        RED,
        50,
        230
    )

    # Instructions
    draw_text("Press a letter on your keyboard", small_font, BLACK, 50, 420)

    # ============================
    # 11. WIN / LOSE MESSAGE
    # ============================
    if win:
        draw_text("YOU WIN!", title_font, GREEN, 200, 540)
        draw_text("Press R to play again", small_font, BLACK, 180, 575)

    elif game_over:
        draw_text("GAME OVER!", title_font, RED, 180, 540)
        draw_text("Word: " + word, small_font, BLACK, 230, 575)
        draw_text("Press R to play again", small_font, BLACK, 180, 595)

    # Update screen
    pygame.display.flip()

    # ============================
    # 12. HANDLE EVENTS
    # ============================
    for event in pygame.event.get():

        # Close the game
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:

            # Restart game
            if event.key == pygame.K_r and (win or game_over):
                reset_game()

            # Guess a letter
            elif not win and not game_over:

                if pygame.K_a <= event.key <= pygame.K_z:

                    letter = chr(event.key).upper()

                    # Ignore repeated guesses
                    if letter not in guessed:

                        guessed.append(letter)

                        # Correct guess
                        if letter in word:
                            print("Correct guess:", letter)

                        # Wrong guess
                        else:
                            wrong += 1
                            print("Wrong guess:", letter)

                        # Check win
                        if all(char in guessed for char in word):
                            win = True

                        # Check lose
                        if wrong >= max_wrong:
                            game_over = True

    clock.tick(60)

# ============================
# 13. EXIT
# ============================
pygame.quit()
sys.exit()