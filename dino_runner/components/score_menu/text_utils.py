import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
black_color = (0, 0, 0)


def get_score_element(poinst):
    font = pygame.font.Font(FONT_STYLE, 20)

    text = font.render('Points: ' + str(poinst), True, black_color) #render nos ayuda a generar el texto que queremos mostrar
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    return text, text_rect

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect

def get_death_count(number_death_count):
    font = pygame.font.Font(FONT_STYLE, 20)

    text = font.render('Number death: ' + str(number_death_count), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    return text, text_rect
