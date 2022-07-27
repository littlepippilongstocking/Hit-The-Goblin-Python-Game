"""
Dilyana Koleva, July 2022
Getting to know PyGame
Step 1 - Keys and Movement
"""
import pygame

pygame.init()  # always necessary
window = pygame.display.set_mode((500, 500))  # set up the window
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
velocity = 6

# main loop that runs throughout the game
run = True
while run:
    pygame.time.delay(100)

    # checks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # keyboard events for moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    window.fill((0, 0, 0))  # makes sure the background stays black after moving

    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
