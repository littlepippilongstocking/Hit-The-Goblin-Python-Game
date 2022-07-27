"""
Dilyana Koleva, July 2022
Getting to know PyGame
Step 2 - Jumping and Boundaries
"""
import pygame

pygame.init()  # always necessary

# adjust height and width to your monitor
screen_height = 600
screen_width = 800

window = pygame.display.set_mode((screen_width, screen_height))  # set up the window w : h
pygame.display.set_caption("First Game")

x = 50
y = 440

width = 40
height = 60
velocity = 5

isJumping = False
jump_count = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Ensures the rectangle doesn't go off the screen
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity

    if keys[pygame.K_RIGHT] and x < screen_width - width - velocity:
        x += velocity

    if not isJumping:
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity

        if keys[pygame.K_DOWN] and y < screen_height - height - velocity:
            y += velocity

        if keys[pygame.K_SPACE]:
            isJumping = True
    else:
        if jump_count > -10:
            NEG = 1

            if jump_count < 0:
                NEG = -1

            y -= (jump_count ** 2) / 2 * NEG
            jump_count -= 1

        else:
            isJumping = False
            jump_count = 10

    window.fill((0, 0, 0))  # makes sure the background stays black after moving

    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
