import pygame
from random import randint
from game.components.spaceship import Spaceship
from game.utils.constants import STARSHIP, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullet.bullet import Bullet

class Starship(Spaceship):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    XPOS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    YPOS = 500
    STARSHIP_SPEED = 5

    def __init__(self, type = 'coop'):
        super().__init__()
        self.image = STARSHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) + self.SHIP_WIDTH
        self.rect.y = 500
        self.type = type
        self.shooting_time = 0
        self.score = 0
        self.high_score = 0
        self.death_count = 0

    def update(self, user_input, bullet_manager):

        if self.rect.right > SCREEN_WIDTH-1:
            self.rect.left = 2
        if self.rect.left < 1:
            self.rect.right = SCREEN_WIDTH-2
        self.is_shooting = False

        if user_input[pygame.K_a]:
            self.move_leftt()

        if user_input[pygame.K_d]:
            self.move_rightt()

        if user_input[pygame.K_w]:
            self.move_upp()

        if user_input[pygame.K_s]:
            self.move_downn()

        if user_input[pygame.K_g]:
            self.is_shooting = True
        else:
            self.is_shooting = False

    def move_leftt(self):
        self.rect.x -= self.STARSHIP_SPEED
        if self.rect.x < 0:
            self.rect.x = 0

    def move_rightt(self):
        self.rect.x += self.STARSHIP_SPEED
        if self.rect.x > SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_upp(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.STARSHIP_SPEED
    
    def move_downn(self):
        if self.rect.y < SCREEN_HEIGHT -70:
            self.rect.y += self.STARSHIP_SPEED

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.is_shooting and current_time >= self.shooting_time:
            bullet = Bullet(self)
            bullet_manager.add_player_bullet(bullet)
            self.shooting_time = current_time + randint(200, 500)

    def set_image(self, size = (40, 60), image = STARSHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    

