
import pygame
import random

pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Pong Game")

clock = pygame.time.Clock()

# Colors
BLACK = (15, 15, 20)
WHITE = (255, 255, 255)
BLUE = (40, 130, 255)
RED = (255, 70, 70)
YELLOW = (255, 220, 50)
GRAY = (120, 120, 120)

# Fonts
font = pygame.font.SysFont("Arial", 35)
small_font = pygame.font.SysFont("Arial", 22)
big_font = pygame.font.SysFont("Arial", 65)

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 15
BALL_SPEED = 5
MAX_BALL_SPEED = 12
MAX_BALL_ANGLE = 7

# Winning score
WINNING_SCORE = 5

# Game states
game_state = "ready"

# Countdown settings
countdown_start = 0
COUNTDOWN_DURATION = 3000

# Create paddles
left_paddle = pygame.Rect(
    30,
    HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH,
    PADDLE_HEIGHT
)

right_paddle = pygame.Rect(
    WIDTH - 30 - PADDLE_WIDTH,
    HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH,
    PADDLE_HEIGHT
)

# Create ball
ball = pygame.Rect(
    WIDTH // 2 - BALL_SIZE // 2,
    HEIGHT // 2 - BALL_SIZE // 2,
    BALL_SIZE,
    BALL_SIZE
)

# Ball velocity
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Scores
left_score = 0
right_score = 0


def reset_ball():

    global ball_dx, ball_dy

    ball.center = (WIDTH // 2, HEIGHT // 2)

    ball_dx = random.choice([-1, 1]) * BALL_SPEED
    ball_dy = random.choice([-1, 1]) * BALL_SPEED


def start_countdown():

    global game_state, countdown_start

    reset_ball()

    countdown_start = pygame.time.get_ticks()
    game_state = "countdown"


def reset_game():

    global left_score, right_score, game_state

    left_score = 0
    right_score = 0

    left_paddle.centery = HEIGHT // 2
    right_paddle.centery = HEIGHT // 2

    start_countdown()


def move_paddles(keys):

    # Player 1
    if keys[pygame.K_w]:
        left_paddle.y -= PADDLE_SPEED

    if keys[pygame.K_s]:
        left_paddle.y += PADDLE_SPEED

    # Player 2
    if keys[pygame.K_UP]:
        right_paddle.y -= PADDLE_SPEED

    if keys[pygame.K_DOWN]:
        right_paddle.y += PADDLE_SPEED

    # Keep paddles inside window
    left_paddle.top = max(0, left_paddle.top)
    left_paddle.bottom = min(HEIGHT, left_paddle.bottom)

    right_paddle.top = max(0, right_paddle.top)
    right_paddle.bottom = min(HEIGHT, right_paddle.bottom)


def check_paddle_collision():

    global ball_dx, ball_dy

    # Left paddle collision
    if ball.colliderect(left_paddle) and ball_dx < 0:

        # Calculate where the ball hits the paddle
        offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)

        # Convert impact position into vertical velocity
        ball_dy = offset * MAX_BALL_ANGLE

        # Increase horizontal speed
        ball_dx = min(abs(ball_dx) + 0.5, MAX_BALL_SPEED)

        # Send ball towards right
        ball.left = left_paddle.right

    # Right paddle collision
    elif ball.colliderect(right_paddle) and ball_dx > 0:

        offset = (ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2)

        ball_dy = offset * MAX_BALL_ANGLE

        ball_dx = -min(abs(ball_dx) + 0.5, MAX_BALL_SPEED)

        # Send ball towards left
        ball.right = right_paddle.left


def draw_text(text, selected_font, color, y):

    image = selected_font.render(text, True, color)

    screen.blit(
        image,
        (WIDTH // 2 - image.get_width() // 2, y)
    )


def draw_game():

    screen.fill(BLACK)

    # Draw center line
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(
            screen,
            GRAY,
            (WIDTH // 2 - 2, y, 4, 15)
        )

    # Draw paddles
    pygame.draw.rect(screen, BLUE, left_paddle)
    pygame.draw.rect(screen, RED, right_paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    left_text = font.render(str(left_score), True, BLUE)
    right_text = font.render(str(right_score), True, RED)

    screen.blit(left_text, (WIDTH // 4, 25))
    screen.blit(right_text, (3 * WIDTH // 4, 25))

    # Starting screen
    if game_state == "ready":

        draw_text(
            "PONG GAME",
            big_font,
            YELLOW,
            130
        )

        draw_text(
            "Select Winning Score",
            small_font,
            WHITE,
            230
        )

        draw_text(
            "1 = 5     2 = 10     3 = 15",
            font,
            YELLOW,
            270
        )

        draw_text(
            "Press SPACE to Start",
            small_font,
            WHITE,
            340
        )

    # Countdown screen
    elif game_state == "countdown":

        elapsed = pygame.time.get_ticks() - countdown_start

        remaining = 3 - elapsed // 1000

        if remaining > 0:
            draw_text(
                str(remaining),
                big_font,
                YELLOW,
                HEIGHT // 2 - 50
            )

        else:
            draw_text(
                "GO!",
                big_font,
                YELLOW,
                HEIGHT // 2 - 50
            )

    # Pause screen
    elif game_state == "paused":

        draw_text(
            "PAUSED",
            big_font,
            YELLOW,
            HEIGHT // 2 - 60
        )

        draw_text(
            "Press SPACE to Resume",
            small_font,
            WHITE,
            HEIGHT // 2 + 20
        )

    # Game over screen
    elif game_state == "game_over":

        if left_score >= WINNING_SCORE:
            winner = "PLAYER 1 WINS!"
        else:
            winner = "PLAYER 2 WINS!"

        draw_text(
            winner,
            big_font,
            YELLOW,
            HEIGHT // 2 - 70
        )

        draw_text(
            "Press SPACE to Restart",
            small_font,
            WHITE,
            HEIGHT // 2 + 20
        )

    pygame.display.update()


# Main game loop
running = True

while running:

    # Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            # Select winning score on starting screen
            if game_state == "ready":

                if event.key == pygame.K_1:
                    WINNING_SCORE = 5

                elif event.key == pygame.K_2:
                    WINNING_SCORE = 10

                elif event.key == pygame.K_3:
                    WINNING_SCORE = 15

                elif event.key == pygame.K_SPACE:
                    start_countdown()

            # Pause and resume
            elif event.key == pygame.K_SPACE:

                if game_state == "playing":
                    game_state = "paused"

                elif game_state == "paused":
                    game_state = "playing"

                elif game_state == "game_over":
                    reset_game()

    # Read keyboard state
    keys = pygame.key.get_pressed()

    # Countdown logic
    if game_state == "countdown":

        elapsed = pygame.time.get_ticks() - countdown_start

        if elapsed >= COUNTDOWN_DURATION:
            game_state = "playing"

    # Playing logic
    if game_state == "playing":

        # Move paddles
        move_paddles(keys)

        # Move ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Top and bottom wall collision
        if ball.top <= 0:
            ball.top = 0
            ball_dy = abs(ball_dy)

        elif ball.bottom >= HEIGHT:
            ball.bottom = HEIGHT
            ball_dy = -abs(ball_dy)

        # Paddle collision
        check_paddle_collision()

        # Ball goes outside left side
        if ball.right < 0:

            right_score += 1
            start_countdown()

        # Ball goes outside right side
        elif ball.left > WIDTH:

            left_score += 1
            start_countdown()

        # Check winner
        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:

            game_state = "game_over"

    # Draw everything
    draw_game()

    # Control FPS
    clock.tick(60)


pygame.quit()
