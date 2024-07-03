import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SNAKE_SIZE = 10
FOOD_SIZE = 5
SPEED = 20

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a snake as a list of coordinates
snake_coords = [(100, 100)]
direction = 'right'

# Generate the food
food_x = random.randint(0, WIDTH - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE
food_y = random.randint(0, HEIGHT - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE

# Set up the score and game state
score = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    # Move the snake
    if direction == 'left':
        snake_coords.append(
            (snake_coords[-1][0] - SNAKE_SIZE, snake_coords[-1][1]))
    elif direction == 'right':
        snake_coords.append(
            (snake_coords[-1][0] + SNAKE_SIZE, snake_coords[-1][1]))
    elif direction == 'up':
        snake_coords.append(
            (snake_coords[-1][0], snake_coords[-1][1] - SNAKE_SIZE))
    elif direction == 'down':
        snake_coords.append(
            (snake_coords[-1][0], snake_coords[-1][1] + SNAKE_SIZE))

    # Check for collisions with the food
    if snake_coords[-1] == (food_x, food_y):
        score += 1
        food_x = random.randint(0,
                                WIDTH - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE
        food_y = random.randint(0,
                                HEIGHT - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE
    else:
        snake_coords.pop(0)

    # Check for collisions with itself or the boundaries
    if (snake_coords[-1][0] < 0 or snake_coords[-1][0] >= WIDTH
            or snake_coords[-1][1] < 0 or snake_coords[-1][1] >= HEIGHT
            or snake_coords[-1] in snake_coords[:-1]):
        game_over = True

    # Redraw the game board
    screen.fill(BLACK)
    for x, y in snake_coords:
        pygame.draw.rect(screen, WHITE, (x, y, SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, WHITE, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(SPEED)

pygame.quit()

print("Game Over! Your score is", score)
