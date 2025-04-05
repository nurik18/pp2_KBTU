import pygame
import sys
import random
import time

#  initailizin
pygame.init()

# variabls
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
SPEED = 5
SCORE = 0
TENGE = 0

# rgbs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# fonts texts
font_large = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font_large.render("Game Over", True, BLACK)

# bg
background = pygame.image.load("Back.png")

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# fps timer
clock = pygame.time.Clock()
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# clases
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy1-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect().inflate(-50, -15)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player1-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect().inflate(-50, -15)
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)


class Tenge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tenge-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect().inflate(5, 5)
        self.respawn()

    def move(self):
        pass

    def respawn(self):
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(100, SCREEN_HEIGHT - 200)
        )

# objecs
player = Player()
enemy = Enemy()
tenge = Tenge()

enemies = pygame.sprite.Group()
enemies.add(enemy)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, tenge)

# game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED:
            SPEED += 0.5

    # bg fon
    screen.blit(background, (0, 0))

    # sprite obnovlenie
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # crash
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound("crash.mp3").play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)

        for entity in all_sprites:
            entity.kill()

        pygame.quit()
        sys.exit()

    # monetochka
    if pygame.sprite.collide_rect(player, tenge):
        TENGE += 1
        tenge.respawn()

    # points
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    tenge_text = font_small.render(f"Tenge: {TENGE}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(tenge_text, (SCREEN_WIDTH - 100, 10))

    pygame.display.update()
    clock.tick(FPS)
