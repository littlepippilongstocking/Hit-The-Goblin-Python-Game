"""
Dilyana Koleva, July 2022
Getting to know PyGame
Step 3 - Character Animation
"""
import pygame

pygame.init()  # always necessary

screen_height = 480
screen_width = 500

window = pygame.display.set_mode((screen_width, screen_height))  # set up the window w : h
pygame.display.set_caption("First Game")

# Lists for character moves
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

background = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400

width = 64
height = 64
velocity = 5

isJumping = False
jump_count = 10

isLeft = False
isRight = False
walk_count = 0


def redrawGameWindow():
    global walk_count
    window.blit(background, (0, 0))
    if walk_count + 1 >= 27:
        walk_count = 0
    if isLeft:
        window.blit(walkLeft[walk_count // 3], (x, y))
        walk_count += 1
    elif isRight:
        window.blit(walkRight[walk_count // 3], (x, y))
        walk_count += 1
    else:
        window.blit(char, (x, y))
    pygame.display.update()


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        isLeft = True
        isRight = False

    elif keys[pygame.K_RIGHT] and x < 500 - width - velocity:
        x += velocity
        isRight = True
        isLeft = False
    else:
        isRight = False
        isLeft = False
        walk_count = 0

    if not isJumping:
        if keys[pygame.K_SPACE]:
            isJumping = True
            isRight = False
            isLeft = False
            walk_count = 0
    else:
        if jump_count >= -10:
            NEG = 1

            if jump_count < 0:
                NEG = -1

            y -= (jump_count ** 2) / 2 * NEG
            jump_count -= 1

        else:
            isJumping = False
            jump_count = 10

    redrawGameWindow()
pygame.quit()
