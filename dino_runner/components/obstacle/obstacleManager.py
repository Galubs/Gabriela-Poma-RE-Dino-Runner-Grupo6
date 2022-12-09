import pygame
import random

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            self.obstacles.append(Cactus(LARGE_CACTUS))
            self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                #pygame.time.delay(500)  #delay lentea el tiempo
                #game.playing = False
                #game.death_count += 1
                #break
                if not game.player.shield:
                    pygame.time.delay(100)  #delay para que detecte la colicion
                    self.obstacles = []

                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break

                #else:
                    #self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []     #al pasarle la lista vacia le decimos que se limpie

