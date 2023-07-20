import pygame
from pygame.sprite import Sprite
from game.components.bullet.bullet import Bullet

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE
class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 5

    def __init__(self, type = 'player'):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.Y_POS
        self.rect.y = self.Y_POS
        self.type = type
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.is_shooting = False  
        self.shooting_delay = 1
        self.last_shot_time = pygame.time.get_ticks()  
        self.destroyed = False
        self.score = 0
        self.high_score = 0


    def update(self, user_input, bullet_manager):

        self.is_shooting = False

        if user_input[pygame.K_LEFT]:
            self.move_left()

        if user_input[pygame.K_RIGHT]:
            self.move_right()

        if user_input[pygame.K_UP]:
            self.move_up()

        if user_input[pygame.K_DOWN]:
            self.move_down()

        if user_input[pygame.K_SPACE]:
            self.is_shooting = True
        else:
            self.is_shooting = False

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
            
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT -70:
            self.rect.y += self.SHIP_SPEED

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.is_shooting and current_time - self.last_shot_time > self.shooting_delay:
            bullet = Bullet(self)
            bullet_manager.add_player_bullet(bullet)
            self.last_shot_time = current_time

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_image(self, size = (40, 60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

