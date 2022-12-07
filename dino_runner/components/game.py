import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacleManager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
        self.clock = pygame.time.Clock()    #Clock: contador hecho para videojuego ya definido por pygame
        self.playing = False    #define un estado para saber si estoy o no jugando
        self.game_speed = 20    #velocidad del juego
        self.x_pos_bg = 0       #posicion para el background en X
        self.y_pos_bg = 380     #posicion para el background en Y
        self.player = Dinosaur()    #llamando a la clase Dinosaur
        self.obstacle_manager = ObstacleManager()

    def run(self):      
        self.playing = True
        while self.playing:         ## GAME LOOP: events, update, draw
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.plying = False

    def update(self):       ##ira actualizando segun lo qe el usuario va presionando
        user_input = pygame.key.get_pressed()   #para que python nos ayude a reconocer que esta presionando el usuarios
        self.player.update(user_input) 
        self.obstacle_manager.update(self) 

    def draw(self):
        self.clock.tick(FPS) #tick es un funcion, que es un contador.
        self.screen.fill((255, 255, 255)) #fill, es un una funcion que rellena la pantalla con un color
        self.draw_background() 
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update() #update, para que la pantalla se vaya actualizando
        pygame.display.flip()   #nos va a ayudar a que se muestre de forma correcta los elementos actualizados en nuestra pantalla

    def draw_background(self):
        image_width = BG.get_width()        ##tip: ctrl + cursero del mouse: para ver detalles de cada variable
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))        ##blit funcion para mostrar algo en la pantalla
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
