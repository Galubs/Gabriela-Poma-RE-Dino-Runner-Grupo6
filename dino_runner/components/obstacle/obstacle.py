from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacle):
        self.rect.x -= game_speed   #le restamos la velocidad del juego para que recorra dependiendo de la velocidad que lleva el juego
        if self.rect.x < -self.rect.width:
            obstacle.pop()  #funcion que ayuda a eliminar un elemento de las listas

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect) ## aqui falta codigo, una pequenia linea
