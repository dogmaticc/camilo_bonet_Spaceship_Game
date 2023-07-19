import pygame

class BulletManager: 

    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            enemy = game.enemy_manager.get_enemy()
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'player':
                self.enemy_bullets.remove(bullet)
                self.remove_enemy(enemy)
                game.score += 1
                break

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                game.death_count += 1
                pygame.time.delay(1000)
                break

        self.update_player_bullets() 

    def update_player_bullets(self):
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

    def draw_player_bullets(self, screen):
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

    def add_player_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.player_bullets) < 1:
            self.player_bullets.append(bullet)



    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        self.draw_player_bullets(screen)




