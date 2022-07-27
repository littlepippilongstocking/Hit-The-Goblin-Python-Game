"""
Dilyana Koleva, July 2022
Getting to know PyGame
Step 9 - Sound Effects
"""
import pygame

pygame.init()  # always necessary

screen_height = 480
screen_width = 540

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

score = 0


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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

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

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walk_count = 0
        font1 = pygame.font.SysFont("comincsans", 100)
        text = font1.render("-5", 1, (255, 0, 0))
        window.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


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


class Enemy(object):
    walkRightList = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                     pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                     pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                     pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeftList = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                    pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                    pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                    pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.isVisible = True

    def drawing(self, win):
        self.move()
        if self.isVisible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.velocity > 0:
                win.blit(self.walkRightList[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walkLeftList[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255, 0, 0),self.hitbox, 2)

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.isVisible = False
        print("Hit!")


def redrawGameWindow():
    window.blit(background, (0, 0))
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    window.blit(text, (390, 10))

    character.drawing(window)
    goblin.drawing(window)
    for b in bullets:
        b.drawing(window)
    pygame.display.update()


# main loop
font = pygame.font.SysFont("comicsans", 30, True)
character = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
shoot = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if character.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and character.hitbox[1] + character.hitbox[3] > goblin.hitbox[1]:
        if character.hitbox[0] + character.hitbox[2] > goblin.hitbox[0] and character.hitbox[0] < goblin.hitbox[0] + \
                goblin.hitbox[2]:
            character.hit()
            score -= 5

    if shoot > 0:
        shoot += 1
    if shoot > 3:
        shoot = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot == 0:
        if character.isLeft:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Shooting(round(character.x + character.width // 2),
                                    round(character.y + character.height // 2),
                                    6, (0, 0, 0), facing))
        shoot = 1

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
