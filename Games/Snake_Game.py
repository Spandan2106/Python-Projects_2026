
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
game_over = False


def draw_game():
    screen.fill((20, 20, 20))

    for part in snake:
        pygame.draw.rect(
            screen, (0, 200, 0),
            (part[0], part[1], CELL, CELL)
        )

    pygame.draw.rect(
        screen, (255, 0, 0),
        (food[0], food[1], CELL, CELL)
    )

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if game_over:
        message = font.render("GAME OVER - Press R", True, (255, 255, 0))
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

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if game_over and event.key == pygame.K_r:
                snake = [(300, 200), (280, 200), (260, 200)]
                direction = (CELL, 0)
                score = 0
                food = create_food()
                game_over = False

            if not game_over:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, CELL):
                    direction = (0, -CELL)

                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -CELL):
                    direction = (0, CELL)

                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (CELL, 0):
                    direction = (-CELL, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-CELL, 0):
                    direction = (CELL, 0)

    if not game_over:

        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        snake.insert(0, head)

        if head == food:
            score += 10
            food = create_food()
        else:
            snake.pop()

        if (
            head[0] < 0 or head[0] >= WIDTH
            or head[1] < 0 or head[1] >= HEIGHT
            or head in snake[1:]
        ):
            game_over = True

    draw_game()
    clock.tick(10)

pygame.quit()
