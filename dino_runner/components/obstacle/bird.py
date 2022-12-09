from dino_runner.components.obstacle.obstacle import Obstacle
import random

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)   
        super().__init__(image, self.type)
        self.rect.x = 1500
        self.rect.y = 50








        #self.rect.y.image.LARGE_CACTUS = 300