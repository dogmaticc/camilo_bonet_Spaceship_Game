from random import choice
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class EnemyManager:
    ENEMY_1['speed_x'] = 5
    ENEMY_1['speed_y'] = 1
    ENEMY_1['move_x_for'] = 90

    ENEMY_2['speed_x'] = 7
    ENEMY_2['speed_y'] = 2
    ENEMY_2['move_x_for'] = 40

    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy_data = choice([ENEMY_1, ENEMY_2])
            enemy = Enemy(enemy_data)
            self.enemies.append(enemy)


