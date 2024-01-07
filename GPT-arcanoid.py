import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Arkanoid')

# Set up game clock
clock = pygame.time.Clock()

# Define game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up game objects
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
paddle = pygame.Rect((WINDOW_WIDTH - PADDLE_WIDTH) // 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH,
                     PADDLE_HEIGHT)

BALL_RADIUS = 10
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, -5]

BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
NUM_BLOCKS = 10
blocks = [pygame.Rect(i * (BLOCK_WIDTH + 10) + 50, j * (BLOCK_HEIGHT + 10) + 50, BLOCK_WIDTH, BLOCK_HEIGHT) for i in
          range(NUM_BLOCKS) for j in range(3)]

# Set up game state
game_over = False
score = 0

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 5
    if keys[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
        paddle.right += 5

    # Move ball
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Check for collision with walls
    if ball.left < 0 or ball.right > WINDOW_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top < 0:
        ball_speed[1] = -ball_speed[1]

    # Check for collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Check for collision with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = -ball_speed[1]
            score += 10

    # Clear screen
    window.fill(BLACK)

    # Draw game objects
    pygame.draw.rect(window, WHITE, paddle)
    pygame.draw.circle(window, RED, (ball.centerx, ball.centery), BALL_RADIUS)
    for block in blocks:
        pygame.draw.rect(window, GREEN, block)

    # Update display
    pygame.display.update()

    # Check for game over
    if ball.bottom > WINDOW_HEIGHT:
        game_over = True

    # Set game speed
    clock.tick(60)

# Game over screen
font = pygame.font.Font(None, 36)
text = font.render('Game over! Score: ' + str(score), True, YELLOW)
# text_rect = text.get_rect(center=(WINDOW_WIDTH // 2,

