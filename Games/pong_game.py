
import pygame
import random

pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.SysFont("Arial", 35)
small_font = pygame.font.SysFont("Arial", 22)

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 15
BALL_SPEED = 5
MAX_BALL_SPEED = 12

# Create paddles
left_paddle = pygame.Rect(
    30, HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH, PADDLE_HEIGHT
)

right_paddle = pygame.Rect(
    WIDTH - 30 - PADDLE_WIDTH,
    HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH, PADDLE_HEIGHT
)

# Create ball
ball = pygame.Rect(
    WIDTH // 2 - BALL_SIZE // 2,
    HEIGHT // 2 - BALL_SIZE // 2,
    BALL_SIZE, BALL_SIZE
)

# Ball velocity
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Scores
left_score = 0
right_score = 0

# Game states: ready, playing, game_over
game_state = "ready"

WINNING_SCORE = 5


def reset_ball():
    global ball_dx, ball_dy

    ball.center = (WIDTH // 2, HEIGHT // 2)

    ball_dx = random.choice([-1, 1]) * BALL_SPEED
    ball_dy = random.choice([-1, 1]) * BALL_SPEED


def reset_game():
    global left_score, right_score, game_state

    left_score = 0
    right_score = 0

    left_paddle.centery = HEIGHT // 2
    right_paddle.centery = HEIGHT // 2

    reset_ball()
    game_state = "ready"


def draw_game():
    screen.fill(BLACK)

    # Draw center line
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(
            screen, WHITE,
            (WIDTH // 2 - 2, y, 4, 15)
        )

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(left_text, (WIDTH // 4, 30))
    screen.blit(right_text, (3 * WIDTH // 4, 30))

    # Show instructions
    if game_state == "ready":
        message = small_font.render(
            "Press SPACE to Start", True, YELLOW
        )
        screen.blit(
            message,
            (WIDTH // 2 - message.get_width() // 2, HEIGHT - 50)
        )

    elif game_state == "game_over":
        if left_score == WINNING_SCORE:
            winner = "PLAYER 1 WINS!"
        else:
            winner = "PLAYER 2 WINS!"

        message = font.render(winner, True, YELLOW)
        restart = small_font.render(
            "Press SPACE to Restart", True, WHITE
        )

        screen.blit(
            message,
            (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 30)
        )

        screen.blit(
            restart,
            (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2 + 20)
        )

    pygame.display.update()


running = True

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:

                if game_state == "ready":
                    game_state = "playing"

                elif game_state == "game_over":
                    reset_game()

    # Get currently pressed keys
    keys = pygame.key.get_pressed()

    # Update game only while playing
    if game_state == "playing":

        # Player 1 movement
        if keys[pygame.K_w]:
            left_paddle.y -= PADDLE_SPEED

        if keys[pygame.K_s]:
            left_paddle.y += PADDLE_SPEED

        # Player 2 movement
        if keys[pygame.K_UP]:
            right_paddle.y -= PADDLE_SPEED

        if keys[pygame.K_DOWN]:
            right_paddle.y += PADDLE_SPEED

        # Keep paddles inside the window
        left_paddle.top = max(0, left_paddle.top)
        left_paddle.bottom = min(HEIGHT, left_paddle.bottom)

        right_paddle.top = max(0, right_paddle.top)
        right_paddle.bottom = min(HEIGHT, right_paddle.bottom)

        # Move ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Top and bottom wall collision
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Left paddle collision
        if ball.colliderect(left_paddle) and ball_dx < 0:
            ball.left = left_paddle.right
            ball_dx = min(abs(ball_dx) + 0.5, MAX_BALL_SPEED)

        # Right paddle collision
        if ball.colliderect(right_paddle) and ball_dx > 0:
            ball.right = right_paddle.left
            ball_dx = -min(abs(ball_dx) + 0.5, MAX_BALL_SPEED)

        # Left player misses the ball
        if ball.right < 0:
            right_score += 1
            reset_ball()

        # Right player misses the ball
        elif ball.left > WIDTH:
            left_score += 1
            reset_ball()

        # Check winner
        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
            game_state = "game_over"

    # Draw everything
    draw_game()

    # Control FPS
    clock.tick(60)

pygame.quit()
