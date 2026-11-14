
import pygame
import random
import math

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
PURPLE = (170, 80, 220)
ORANGE = (255, 150, 40)

font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

# Paddle settings
PADDLE_WIDTH = 110
PADDLE_HEIGHT = 15
PADDLE_SPEED = 7

paddle = pygame.Rect(
    WIDTH // 2 - PADDLE_WIDTH // 2,
    HEIGHT - 50,
    PADDLE_WIDTH,
    PADDLE_HEIGHT
)

# Ball settings
BALL_SIZE = 15
BASE_SPEED = 5
MAX_SPEED = 10

ball = pygame.Rect(
    WIDTH // 2,
    HEIGHT // 2,
    BALL_SIZE,
    BALL_SIZE
)

ball_dx = 3
ball_dy = -4


# Brick settings
BRICK_WIDTH = 70
BRICK_HEIGHT = 25
BRICK_GAP = 8

# Brick colors and points
BRICK_TYPES = [
    (RED, 10),
    (ORANGE, 20),
    (YELLOW, 30),
    (GREEN, 40),
    (PURPLE, 50)
]

bricks = []


# Game variables
score = 0
high_score = 0
lives = 3
level = 1

game_state = "ready"


# Create bricks for different levels
def create_bricks():

    bricks.clear()

    if level == 1:
        rows = 3
        cols = 10

    elif level == 2:
        rows = 4
        cols = 8

    else:
        rows = 5
        cols = 10

    for row in range(rows):

        for col in range(cols):

            # Level 2: create a staggered arrangement
            if level == 2 and (row + col) % 2 != 0:
                continue

            # Level 3: create a diamond-like arrangement
            if level == 3:
                distance = abs(col - 4.5)

                if distance > row + 1:
                    continue

            x = (
                WIDTH // 2
                - (cols * (BRICK_WIDTH + BRICK_GAP) - BRICK_GAP) // 2
                + col * (BRICK_WIDTH + BRICK_GAP)
            )

            y = 70 + row * (BRICK_HEIGHT + BRICK_GAP)

            brick = pygame.Rect(
                x, y, BRICK_WIDTH, BRICK_HEIGHT
            )

            color, points = BRICK_TYPES[row % len(BRICK_TYPES)]

            bricks.append({
                "rect": brick,
                "color": color,
                "points": points
            })


# Calculate current ball speed
def get_ball_speed():

    speed = BASE_SPEED + (score // 50) * 0.5

    return min(speed, MAX_SPEED)


# Adjust velocity while preserving its direction
def update_ball_speed():

    global ball_dx, ball_dy

    current_speed = math.sqrt(
        ball_dx ** 2 + ball_dy ** 2
    )

    target_speed = get_ball_speed()

    if current_speed > 0:

        ball_dx = (ball_dx / current_speed) * target_speed
        ball_dy = (ball_dy / current_speed) * target_speed


# Reset ball
def reset_ball():

    global ball_dx, ball_dy

    ball.center = (WIDTH // 2, HEIGHT // 2)

    speed = get_ball_speed()

    ball_dx = random.choice([-1, 1]) * speed * 0.6
    ball_dy = -speed * 0.8

    paddle.centerx = WIDTH // 2


# Restart complete game
def restart_game():

    global score, lives, level, game_state

    score = 0
    lives = 3
    level = 1

    create_bricks()
    reset_ball()

    game_state = "ready"


# Initialize bricks
create_bricks()


# Main game loop
running = True

while running:

    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            # SPACE: start, pause, resume or restart
            if event.key == pygame.K_SPACE:

                if game_state == "ready":
                    game_state = "playing"

                elif game_state == "playing":
                    game_state = "paused"

                elif game_state == "paused":
                    game_state = "playing"

                elif game_state in ("game_over", "won"):
                    restart_game()

    # Get keyboard input
    keys = pygame.key.get_pressed()

    if game_state == "playing":

        # Paddle movement
        if keys[pygame.K_LEFT]:
            paddle.x -= PADDLE_SPEED

        if keys[pygame.K_RIGHT]:
            paddle.x += PADDLE_SPEED

        # Keep paddle inside screen
        paddle.clamp_ip(screen.get_rect())

        # Ball movement
        ball.x += round(ball_dx)
        ball.y += round(ball_dy)

        # Wall collision
        if ball.left <= 0:
            ball.left = 0
            ball_dx = abs(ball_dx)

        if ball.right >= WIDTH:
            ball.right = WIDTH
            ball_dx = -abs(ball_dx)

        if ball.top <= 0:
            ball.top = 0
            ball_dy = abs(ball_dy)

        # Paddle collision
        if ball.colliderect(paddle) and ball_dy > 0:

            ball.bottom = paddle.top

            speed = get_ball_speed()

            offset = (
                ball.centerx - paddle.centerx
            ) / (PADDLE_WIDTH / 2)

            offset = max(-1, min(1, offset))

            ball_dx = offset * speed * 0.9

            ball_dy = -math.sqrt(
                max(1, speed ** 2 - ball_dx ** 2)
            )

        # Brick collision
        for brick in bricks[:]:

            if ball.colliderect(brick["rect"]):

                bricks.remove(brick)

                score += brick["points"]

                # Update high score
                if score > high_score:
                    high_score = score

                # Increase speed according to score
                update_ball_speed()

                # Bounce ball
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

        # Level progression
        if len(bricks) == 0:

            if level < 3:

                level += 1

                create_bricks()
                reset_ball()

                game_state = "ready"

            else:
                game_state = "won"

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw bricks
    for brick in bricks:

        pygame.draw.rect(
            screen,
            brick["color"],
            brick["rect"]
        )

        pygame.draw.rect(
            screen,
            WHITE,
            brick["rect"],
            1
        )

    # Display score
    score_text = font.render(
        f"Score: {score}", True, WHITE
    )

    high_text = small_font.render(
        f"High Score: {high_score}", True, YELLOW
    )

    lives_text = font.render(
        f"Lives: {lives}", True, WHITE
    )

    level_text = font.render(
        f"Level: {level}", True, GREEN
    )

    screen.blit(score_text, (20, 15))
    screen.blit(high_text, (20, 48))
    screen.blit(lives_text, (WIDTH - 140, 15))
    screen.blit(level_text, (WIDTH // 2 - 50, 15))

    # Display game messages
    if game_state == "ready":

        if level == 1 and score == 0 and lives == 3:
            message = "Press SPACE to start"

        elif lives < 3:
            message = "Life lost! Press SPACE to continue"

        else:
            message = f"Level {level}! Press SPACE to continue"

        text = small_font.render(
            message, True, YELLOW
        )

        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2 + 80)
        )

    elif game_state == "paused":

        text = font.render(
            "PAUSED", True, YELLOW
        )

        instruction = small_font.render(
            "Press SPACE to resume", True, WHITE
        )

        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2)
        )

        screen.blit(
            instruction,
            (WIDTH // 2 - instruction.get_width() // 2,
             HEIGHT // 2 + 45)
        )

    elif game_state == "game_over":

        text = font.render(
            "GAME OVER", True, RED
        )

        instruction = small_font.render(
            "Press SPACE to restart", True, WHITE
        )

        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2)
        )

        screen.blit(
            instruction,
            (WIDTH // 2 - instruction.get_width() // 2,
             HEIGHT // 2 + 50)
        )

    elif game_state == "won":

        text = font.render(
            "YOU WIN!", True, GREEN
        )

        instruction = small_font.render(
            "Press SPACE to play again", True, WHITE
        )

        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2)
        )

        screen.blit(
            instruction,
            (WIDTH // 2 - instruction.get_width() // 2,
             HEIGHT // 2 + 50)
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
