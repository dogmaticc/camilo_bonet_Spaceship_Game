import pygame
from game.utils.constants import BG, ICON, ICON2, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.starship import Starship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullet.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.playing = False
        self.player = Spaceship(type='player')
        self.coop_player = Starship(type='player')
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu('Press X to start ...', self.screen)
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        self.power_up_manager = PowerUpManager()
        self.all_spaceships = [self.player, self.coop_player]

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def shoot_player_bullet(self):
        self.player.shoot(self.bullet_manager)
        self.coop_player.shoot(self.bullet_manager)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.is_shooting = True
                    self.coop_player.is_shooting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.is_shooting = False
                    self.coop_player.is_shooting = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.coop_player.update(user_input, self.bullet_manager)
        self.power_up_manager.update(self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.shoot_player_bullet()

        for bullet in self.bullet_manager.player_bullets:
            if bullet.rect.colliderect(self.enemy_manager.get_enemy().rect):
                self.bullet_manager.player_bullets.remove(bullet)
                self.enemy_manager.remove_enemy(self)
                self.score += 1

        for bullet in self.bullet_manager.enemy_bullets:
            if bullet.rect.colliderect(self.player.rect):
                self.player.destroyed = True
                self.bullet_manager.enemy_bullets.remove(bullet)
            if bullet.rect.colliderect(self.coop_player.rect):
                self.coop_player.destroyed = True
                self.bullet_manager.enemy_bullets.remove(bullet)

        if not self.playing:
            if self.score > self.high_score:
                self.high_score = self.score
            self.death_count += 1

            for enemy in self.enemy_manager.enemies:
                enemy.reset_position()
            self.show_menu()

        if user_input[pygame.K_g]:
            self.shoot_player_bullet()

        for spaceship in self.all_spaceships:
            user_input = pygame.key.get_pressed()
            spaceship.update(user_input, self.bullet_manager)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.coop_player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message(self.screen, self)
        icon = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 5)))
        self.menu.update(self, self.high_score)
        icon = pygame.transform.scale(ICON2, (80, 120))
        self.screen.blit(icon, ((SCREEN_WIDTH // 2) - 100, (SCREEN_HEIGHT // 5)))
        self.menu.update(self, self.high_score)

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(550, 50))
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                message = f"{self.player.power_up_type} is enabled for {time_to_show} seconds"
                self.menu.draw(self.screen, message=message, x=540, y=100, color=(255, 255, 255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()





    

