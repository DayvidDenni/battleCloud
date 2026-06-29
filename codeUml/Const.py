# C
import pygame

C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_CYAN = (0, 128, 128)
C_GREEN = (0, 130, 0)
C_BLACK = (0, 0, 0)
# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'LevelBG0': 0,
    'LevelBG1': 1,
    'LevelBG2': 1,
    'LevelBG3': 2,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 1,
    'Enemy1': 1,
    'Enemy1Shot': 4,
    'Enemy2': 1,
    'Enemy2Shot': 2
}
ENTITY_HEALTH = {
    'LevelBG0': 999,
    'LevelBG1': 999,
    'LevelBG2': 999,
    'LevelBG3': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}
ENTITY_SHOT_DELAY = {
    'Player1': 18,
    'Player2': 15,
    'Enemy1': 110,
    'Enemy2': 230,
}
ENTITY_DAMAGE = {
    'LevelBG0': 0,
    'LevelBG1': 0,
    'LevelBG2': 0,
    'LevelBG3': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 15,
    'Enemy2': 1,
    'Enemy2Shot': 20
}
ENTITY_SCORE = {
'LevelBG0': 0,
    'LevelBG1': 0,
    'LevelBG2': 0,
    'LevelBG3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 110,
    'Enemy2Shot': 0
}
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w, }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s, }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a, }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d, }
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}
# S
SPAWN_TIME = 4000
# W
WIN_WIDTH = 575
WIN_HEIGHT = 325
