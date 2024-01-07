import pygame
from pygame.constants import QUIT
import random


pygame.init()
screen = width, heigth = 800, 600
main_suface = pygame.display.set_mode(screen)
ball = pygame.Surface((20, 20))
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
color = [WHITE, RED, GREEN, BLUE, YELLOW]
ball.fill(random.choice(color))
ball_rect = ball.get_rect()
ball_speed = [1, 1]
is_working = True
while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.bottom >= heigth or ball_rect.top <= 0:
        ball_speed[1] *= -1
        ball.fill(random.choice(color))
    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_speed[0] *= -1
        ball.fill(random.choice(color))
    main_suface.fill(BLACK)
    main_suface.blit(ball, ball_rect)

    pygame.display.flip()