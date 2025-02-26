from random import choice
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class EnemyManager:
    ENEMY_1['speed_x'] = 5
    ENEMY_1['speed_y'] = 0.5
    ENEMY_1['move_x_for'] = 90

    ENEMY_2['speed_x'] = 10
    ENEMY_2['speed_y'] = 1
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

    def get_enemy(self):
        if self.enemies:
            return self.enemies[0]  
        return None  

    def remove_enemy(self, game):
        if self.enemies:
            self.enemies.pop(0)



