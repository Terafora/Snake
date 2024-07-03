import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SNAKE_SIZE = 10
FOOD_SIZE = 5
SPEED = 15

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (0, 128, 128)

# Create a snake as a list of coordinates
snake_coords = [(100, 100)]
direction = 'right'

# Generate the food
food_x = random.randint(0, WIDTH - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE
food_y = random.randint(0, HEIGHT - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE

# Set up the score and game state
score = 0
game_over = False
font = pygame.font.SysFont('Arial', 24)

while True:
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
            if event.key == pygame.K_q:  # Add 'q' to quit the game
                game_over = True
                pygame.quit()
            elif event.key == pygame.K_c:  # Add 'c' to play again
                game_over = False
                snake_coords = [(100, 100)]
                direction = 'right'
                score = 0

    if not game_over:
        screen.fill(TEAL)
        for x, y in snake_coords:
            pygame.draw.rect(screen, WHITE, (x, y, SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(screen, WHITE, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

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

        if snake_coords[-1] == (food_x, food_y):
            score += 1
            food_x = random.randint(
                0, WIDTH - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE
            food_y = random.randint(
                0, HEIGHT - FOOD_SIZE) // SNAKE_SIZE * SNAKE_SIZE
        else:
            snake_coords.pop(0)

        if (snake_coords[-1][0] < 0 or snake_coords[-1][0] >= WIDTH
                or snake_coords[-1][1] < 0 or snake_coords[-1][1] >= HEIGHT
                or snake_coords[-1] in snake_coords[:-1]):
            game_over = True

        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (WIDTH - 100, 25))

    else:
        screen.fill(BLACK)  # Fill the screen with black when game is over
        game_over_text1 = font.render("Game Over!", True, WHITE)
        screen.blit(game_over_text1, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
        game_over_text2 = font.render("Press Q to quit or C to play again.",
                                      True, WHITE)
        screen.blit(game_over_text2,
                    (WIDTH // 2 - 150,
                     HEIGHT // 2 - 25 + game_over_text1.get_height()))

    pygame.display.flip()
    pygame.time.Clock().tick(SPEED)
