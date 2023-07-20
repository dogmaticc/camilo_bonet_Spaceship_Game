import pygame
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.message = message
        self.text = self.font.render(str(self.message), True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, game, high_score):
        pygame.display.update()
        self.handle_events_on_menu(game, high_score)

    def draw(self, screen, x=HALF_SCREEN_WIDTH, y=HALF_SCREEN_HEIGHT, color=(0, 0, 0), message=None):
        if message is not None:
            self.message = message

        if isinstance(self.message, str):  
            text = self.font.render(str(self.message), True, color)
            text_rect = text.get_rect()
            text_rect.center = (x, y)
            screen.blit(text, text_rect)



    def handle_events_on_menu(self, game, high_score):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game.score = 0
                    game.high_score = high_score
                    game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, screen, game):
        messages = ['Game Over, Press X to restart',
                    f'Your Score:{game.score}',
                    f'Highest Score: {game.high_score}',
                    f'Total Deaths: {game.death_count}']
        Y = 300
        for message in messages:
            self.message = message
            self.text = self.font.render(self.message, True, (0, 0, 0))
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (SCREEN_WIDTH // 2, Y)
            screen.blit(self.text, self.text_rect)
            Y += 40


