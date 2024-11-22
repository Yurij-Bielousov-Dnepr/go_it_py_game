import pygame
import random
from pygame import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
pygame.init()
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 800
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
bonus
player_size = (20, 20)
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
# player_speed = [1, 1]
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_move_down = player_rect[0, 1]
player_move_right = player_rect[1, 0]
player_move_up = player_rect[1, 0]
player_move_left = player_rect[0, 1]


def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]


def create_bonus():
    bonus_size = (15, 15)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_RED)
    bonus_rect = pygame.Rect(
        HEIGHT, random.randint(0, WIDTH), *bonus_size)  # ???
    bonus_move = [random.randint(-6, -1), 0]
    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY, 1500)
CREATE_BONUS = pygame.USEREVENT+2
pygame.time.set_timer(CREATE_BONUS, 1000)

playing = True
enemyes = []
bonuses = []
while playing:
    FPS.tick(180)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemyes.append(create_enemy())
    main_display.fill(COLOR_BLACK)
    keys = pygame.key.get_pressed()
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
    if keys[K_RIGHT] and player_rect.bottom < WIDTH:
        player_rect = player_rect.move(player_move_right)
    if keys[K_UP] and player_rect.bottom < 0:
        player_rect = player_rect.move(player_move_up)
    if keys[K_LEFT] and player_rect.bottom < 0:
        player_rect = player_rect.move(player_move_left)
    for enemy in enemyes:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

    # enemy_rect = enemy_rect.move(enemy_move)
    main_display.blit(player, player_rect)
    main_display.blit(enemy, enemy_rect)
    pygame.display.flip()
    for enemy in enemyes:
        if enemy[1].left < 0:
            enemyes.pop(enemyes.index(enemy))
