"""
Dilyana Koleva, July 2022
Getting to know PyGame
Step 5 - Projectiles
"""
import pygame

pygame.init()  # always necessary

screen_height = 480
screen_width = 500

window = pygame.display.set_mode((screen_width, screen_height))  # set up the window w : h
pygame.display.set_caption("First Game")

walkRightList = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                 pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeftList = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

background = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJumping = False
        self.jump_count = 10
        self.isLeft = False
        self.isRight = False
        self.walk_count = 0
        self.standing = True

    def drawing(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not self.standing:
            if self.isLeft:
                win.blit(walkLeftList[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.isRight:
                win.blit(walkRightList[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.isRight:
                win.blit(walkRightList[0], (self.x, self.y))
            else:
                win.blit(walkLeftList[0], (self.x, self.y))


class Shooting(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.velocity = 8 * facing

    def drawing(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


def redrawGameWindow():
    window.blit(background, (0, 0))
    character.drawing(window)
    for bullet in bullets:
        bullet.drawing(window)
    pygame.display.update()


character = Player(300, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if character.isLeft:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Shooting(round(character.x + character.width // 2),
                                    round(character.y + character.height // 2),
                                    6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and character.x > character.velocity:
        character.x -= character.velocity
        character.isLeft = True
        character.isRight = False
        character.standing = False

    elif keys[pygame.K_RIGHT] and character.x < 500 - character.width - character.velocity:
        character.x += character.velocity
        character.isRight = True
        character.isLeft = False
        character.standing = False
    else:
        character.standing = True
        character.walk_count = 0

    if not character.isJumping:
        if keys[pygame.K_UP]:
            character.isJumping = True
            character.isRight = False
            character.isLeft = False
            character.walk_count = 0
    else:
        if character.jump_count >= -10:
            NEG = 1

            if character.jump_count < 0:
                NEG = -1

            character.y -= (character.jump_count ** 2) / 2 * NEG
            character.jump_count -= 1

        else:
            character.isJumping = False
            character.jump_count = 10

    redrawGameWindow()
pygame.quit()
