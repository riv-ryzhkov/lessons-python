import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, KSCAN_KP_ENTER
import random
from time import sleep
from os import listdir


pygame.init()
FPS = pygame.time.Clock()
screen = width, height = 800, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
font = pygame.font.SysFont('verdana', 40)
game_over = pygame.font.SysFont('verdana', 50)

main_surface = pygame.display.set_mode(screen)

player_size = (60, 60)
bonus_size = (40, 80)
enemy_size = (100, 60)

# player = pygame.image.load('player.png').convert_alpha()
IMG_PATH = 'goose'

player_img = [pygame.image.load(IMG_PATH + '/' + file).convert_alpha() for file in listdir(IMG_PATH)]
player = pygame.transform.scale(player_img[0], size=player_size)
player_rect = player.get_rect()
player_speed = 10

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3


def create_enemy():
    enemy_img = pygame.image.load('enemy.png').convert_alpha()
    enemy = pygame.transform.scale(enemy_img, size=enemy_size)
    enemy_rect = pygame.Rect(width, random.randint(0, height-enemy_size[1]), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1000)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)



img_index = 0
enemies = []
bonuses = []
score = 0


def create_bonus():
    bonus_img = pygame.image.load('bonus.png').convert_alpha()
    bonus = pygame.transform.scale(bonus_img, size=bonus_size)
    bonus_rect = pygame.Rect(random.randint(0, width-bonus_size[0]), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]


is_working = True
while is_working:
    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:

            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index >= len(player_img):
                img_index = 0
            # player = player_img[img_index]
            player = pygame.transform.scale(player_img[img_index], size=player_size)

    pressed_keys = pygame.key.get_pressed()

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(player, player_rect)
    main_surface.blit(font.render(str(score), True, BLUE), (width - 50, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if player_rect.colliderect(enemy[1]):
            # main_surface.blit(game_over.render('GAME OVER', True, BLACK), (width/2-100, height/2))
            # while not (event.type == pygame.KEYDOWN):
            #      while not pressed_keys[K_SPACE]:
            #         pressed_keys = pygame.key.get_pressed()
            #
            #
            # pygame.display.flip()
            # # input()
            #     # pass
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            score += 1

    if pressed_keys[K_DOWN] and player_rect.bottom < height:
        player_rect = player_rect.move(0, player_speed)
    if pressed_keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(0, -player_speed)
    if pressed_keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(-player_speed, 0)
    if pressed_keys[K_RIGHT] and player_rect.right < width:
        player_rect = player_rect.move(player_speed, 0)

    print(len(enemies), len(bonuses))
    pygame.display.flip()
sleep(5)
# pressed_keys = pygame.key.get_pressed()
# while not pressed_keys[KSCAN_KP_ENTER]:
#     pressed_keys = pygame.key.get_pressed()
pygame.quit()
# input()
# # pressed_keys1 = pygame.key.get_pressed()
# # while not pressed_keys1[K_SPACE]:
# #     pass