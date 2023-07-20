import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON2 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/starship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

STARSHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/starship.png"))
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
STARSHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/starship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = {'image': pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))}
ENEMY_2 = {'image': pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))}

SHIP_WIDTH = 40
SHIP_HEIGHT = 60

FONT_STYLE = 'freesansbold.ttf'
