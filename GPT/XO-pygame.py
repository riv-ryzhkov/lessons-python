import pygame
import numpy as np
from time import sleep

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the game board
board = np.zeros((3, 3))

# Set up the font
font = pygame.font.Font('freesansbold.ttf', 32)

# Set up the players
player = 1
player_color = {1: RED, -1: BLUE}

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            row = pos[1] // (HEIGHT // 3)
            col = pos[0] // (WIDTH // 3)
            if board[row][col] == 0:
                board[row][col] = player
                player *= -1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the game board
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * (HEIGHT // 3)), (WIDTH, i * (HEIGHT // 3)), 5)
        pygame.draw.line(screen, BLACK, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), 5)

    # Draw the X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, player_color[1], (col * (WIDTH // 3) + 20, row * (HEIGHT // 3) + 20),
                                 ((col + 1) * (WIDTH // 3) - 20, (row + 1) * (HEIGHT // 3) - 20), 5)
                pygame.draw.line(screen, player_color[1], ((col + 1) * (WIDTH // 3) - 20, row * (HEIGHT // 3) + 20),
                                 (col * (WIDTH // 3) + 20, (row + 1) * (HEIGHT // 3) - 20), 5)
            elif board[row][col] == -1:
                pygame.draw.circle(screen, player_color[-1],
                                   (col * (WIDTH // 3) + WIDTH // 6, row * (HEIGHT // 3) + HEIGHT // 6),
                                   WIDTH // 6 - 20, 5)

    # Check for a winner
    winner = 0
    for i in range(3):
        if abs(np.sum(board[i])) == 3:
            winner = np.sign(np.sum(board[i]))
        if abs(np.sum(board[:, i])) == 3:
            winner = np.sign(np.sum(board[:, i]))
    if abs(np.trace(board)) == 3:
        winner = np.sign(np.trace(board))
    if abs(np.trace(np.fliplr(board))) == 3:
        winner = np.sign(np.trace(np.fliplr(board)))

    # pygame.display.flip()
    if winner != 0:
        text = font.render("Player {} wins!".format(winner), True, player_color[winner])
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        running = False

    # Check for a tie
    if np.all(board != 0) and winner == 0:
        text = font.render("Tie game!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        running = False

    # Update the screen
    pygame.display.update()
sleep(3000)
