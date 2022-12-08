import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacleManager import ObstacleManager
from dino_runner.components.score_menu.text_utils import *  #el asterisco significa importar todo lo que contiene el archivo
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

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
        self.points = 0
        self.running = True
        self.death_count = 0    
        self.player_heart_manager = PlayerHeartManager()

    def run(self):      
        self.obstacle_manager.reset_obstacles(self)
        self.player_heart_manager.reset_hearts
        self.playing = True
        while self.playing:         ## GAME LOOP: events, update, draw
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def events(self):           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.plying = False
                self.running = False

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
        self.score()
        self.player_heart_manager.draw(self.screen)
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

    def score(self):
        self.points += 1
        
        if self.points % 100 == 0:
            self.game_speed += 1 

        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)

    def show_menu(self):
        self.running = True

        white_color = (255,255 , 255)
        self.screen.fill(white_color)

        self.print_menu_elements(self.death_count)
        pygame.display.update()

        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count = 0):
        half_screen_height = SCREEN_HEIGHT // 2 
        half_screen_width = SCREEN_WIDTH // 2 

        if death_count == 0:
            text, text_rect = get_centered_message('Press any Key to Start')
            self.screen.blit(text, text_rect)
        elif death_count > 0:
            text, text_rect = get_centered_message('Press any Key to Restart')
            score, score_rect = get_centered_message('Your Score: ' + str(self.points), height=half_screen_height + 50 )
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Dino: good bye!!")
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

