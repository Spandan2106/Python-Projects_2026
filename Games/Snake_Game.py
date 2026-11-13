
import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

snake = [(300, 200), (280, 200), (260, 200)]
direction = (CELL, 0)

food = (
    random.randrange(0, WIDTH, CELL),
    random.randrange(0, HEIGHT, CELL)
)

score = 0
high_score = 0
speed = 10

game_over = False
paused = False


def draw_game():
    screen.fill((20, 20, 20))

    # Draw snake
    for part in snake:
        pygame.draw.rect(
            screen, (0, 100, 255),
            (part[0], part[1], CELL, CELL)
        )

    # Draw food
    pygame.draw.rect(
        screen, (255, 0, 0),
        (food[0], food[1], CELL, CELL)
    )

    # Display score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Display high score
    high_text = font.render(
        f"High Score: {high_score}", True, (255, 255, 255)
    )
    screen.blit(high_text, (400, 10))

    # Game over message
    if game_over:
        message = font.render(
            "GAME OVER - Press R", True, (255, 255, 0)
        )
        screen.blit(message, (150, 180))

    # Pause message
    elif paused:
        message = font.render(
            "PAUSED - Press SPACE", True, (255, 255, 0)
        )
        screen.blit(message, (150, 180))

    pygame.display.update()


def create_food():
    while True:
        position = (
            random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL)
        )

        if position not in snake:
            return position


running = True

while running:

    # Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            # Pause and resume
            if event.key == pygame.K_SPACE and not game_over:
                paused = not paused

            # Restart game
            if game_over and event.key == pygame.K_r:
                snake = [(300, 200), (280, 200), (260, 200)]
                direction = (CELL, 0)

                score = 0
                speed = 10

                food = create_food()

                game_over = False
                paused = False

            # Snake direction
            if not game_over and not paused:

                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, CELL):
                    direction = (0, -CELL)

                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -CELL):
                    direction = (0, CELL)

                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (CELL, 0):
                    direction = (-CELL, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-CELL, 0):
                    direction = (CELL, 0)

    # Game movement and logic
    if not game_over and not paused:

        # Calculate new head position
        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        snake.insert(0, head)

        # Check food collision
        if head == food:
            score += 10

            # Increase speed every 50 points
            if score % 50 == 0:
                speed += 2

            food = create_food()

        else:
            snake.pop()

        # Check wall and self collision
        if (
            head[0] < 0 or head[0] >= WIDTH
            or head[1] < 0 or head[1] >= HEIGHT
            or head in snake[1:]
        ):
            high_score = max(score, high_score)
            game_over = True

    # Draw game
    draw_game()

    # Control game speed
    clock.tick(speed)

pygame.quit()
