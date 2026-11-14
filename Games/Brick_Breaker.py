
import pygame
import random

pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

# Colors
BLACK = (20, 20, 30)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 70, 70)
GREEN = (50, 220, 100)
YELLOW = (255, 220, 50)

font = pygame.font.SysFont("Arial", 30)
small_font = pygame.font.SysFont("Arial", 22)

# Paddle
PADDLE_WIDTH = 110
PADDLE_HEIGHT = 15
PADDLE_SPEED = 7

paddle = pygame.Rect(
    WIDTH // 2 - PADDLE_WIDTH // 2,
    HEIGHT - 50,
    PADDLE_WIDTH,
    PADDLE_HEIGHT
)

# Ball
BALL_SIZE = 15
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

ball = pygame.Rect(
    WIDTH // 2 - BALL_SIZE // 2,
    HEIGHT // 2,
    BALL_SIZE,
    BALL_SIZE
)

ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Bricks
BRICK_ROWS = 5
BRICK_COLS = 10

BRICK_WIDTH = 70
BRICK_HEIGHT = 25
BRICK_GAP = 8

bricks = []

def create_bricks():
    bricks.clear()

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):

            x = 35 + col * (BRICK_WIDTH + BRICK_GAP)
            y = 60 + row * (BRICK_HEIGHT + BRICK_GAP)

            brick = pygame.Rect(
                x, y, BRICK_WIDTH, BRICK_HEIGHT
            )

            bricks.append(brick)


# Game variables
score = 0
lives = 3
game_state = "ready"

create_bricks()


def reset_ball():
    global ball_dx, ball_dy

    ball.center = (WIDTH // 2, HEIGHT // 2)

    ball_dx = random.choice([-4, 4])
    ball_dy = -4

    paddle.centerx = WIDTH // 2


def restart_game():
    global score, lives, game_state

    score = 0
    lives = 3

    create_bricks()
    reset_ball()

    game_state = "ready"


# Main game loop
running = True

while running:

    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:

                if game_state == "ready":
                    game_state = "playing"

                elif game_state in ("game_over", "won"):
                    restart_game()

    # Keyboard input
    keys = pygame.key.get_pressed()

    if game_state == "playing":

        # Paddle movement
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED

        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += PADDLE_SPEED

        # Ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # Wall collision
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_dx *= -1

        if ball.top <= 0:
            ball_dy *= -1

        # Paddle collision
        if ball.colliderect(paddle) and ball_dy > 0:
            ball.bottom = paddle.top
            ball_dy *= -1

            # Change horizontal direction based on hit position
            offset = (
                ball.centerx - paddle.centerx
            ) / (PADDLE_WIDTH / 2)

            ball_dx = offset * 6

        # Brick collision
        for brick in bricks[:]:

            if ball.colliderect(brick):

                bricks.remove(brick)
                score += 10

                ball_dy *= -1
                break

        # Ball falls below screen
        if ball.top > HEIGHT:

            lives -= 1
            reset_ball()

            if lives <= 0:
                game_state = "game_over"
            else:
                game_state = "ready"

        # Win condition
        if len(bricks) == 0:
            game_state = "won"

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)
        pygame.draw.rect(screen, WHITE, brick, 1)

    # Display score and lives
    score_text = font.render(
        f"Score: {score}", True, WHITE
    )

    lives_text = font.render(
        f"Lives: {lives}", True, WHITE
    )

    screen.blit(score_text, (20, 15))
    screen.blit(lives_text, (WIDTH - 130, 15))

    # Game states
    if game_state == "ready":

        message = small_font.render(
            "Press SPACE to start", True, YELLOW
        )

        screen.blit(
            message,
            (WIDTH // 2 - 110, HEIGHT // 2 + 80)
        )

    elif game_state == "game_over":

        message = font.render(
            "GAME OVER", True, RED
        )

        restart_message = small_font.render(
            "Press SPACE to restart", True, WHITE
        )

        screen.blit(
            message,
            (WIDTH // 2 - 90, HEIGHT // 2)
        )

        screen.blit(
            restart_message,
            (WIDTH // 2 - 110, HEIGHT // 2 + 50)
        )

    elif game_state == "won":

        message = font.render(
            "YOU WIN!", True, GREEN
        )

        restart_message = small_font.render(
            "Press SPACE to play again", True, WHITE
        )

        screen.blit(
            message,
            (WIDTH // 2 - 75, HEIGHT // 2)
        )

        screen.blit(
            restart_message,
            (WIDTH // 2 - 125, HEIGHT // 2 + 50)
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
