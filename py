import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏁 Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Load assets (you can replace with your own images)
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 100

# Player Car
player_car = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - 120, PLAYER_WIDTH, PLAYER_HEIGHT)
player_speed = 5

# Enemy Cars
enemy_cars = []
enemy_speed = 5
spawn_timer = 0
SPAWN_INTERVAL = 40  # frames

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_road():
    SCREEN.fill(GRAY)
    pygame.draw.rect(SCREEN, BLACK, (100, 0, 300, HEIGHT))  # Road
    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(SCREEN, WHITE, (WIDTH//2 - 5, y, 10, 20))  # Center lines

def draw_player():
    pygame.draw.rect(SCREEN, GREEN, player_car)

def draw_enemies():
    for car in enemy_cars:
        pygame.draw.rect(SCREEN, RED, car)

def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(text, (10, 10))

def game_over():
    text = font.render("GAME OVER!", True, RED)
    SCREEN.blit(text, (WIDTH//2 - 80, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    clock.tick(FPS)
    spawn_timer += 1
    SCREEN.fill(GRAY)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car.left > 110:
        player_car.x -= player_speed
    if keys[pygame.K_RIGHT] and player_car.right < WIDTH - 110:
        player_car.x += player_speed

    # Spawn enemies
    if spawn_timer >= SPAWN_INTERVAL:
        enemy_x = random.randint(110, WIDTH - 110 - ENEMY_WIDTH)
        enemy_cars.append(pygame.Rect(enemy_x, -ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT))
        spawn_timer = 0

    # Move enemies
    for car in enemy_cars:
        car.y += enemy_speed

    # Remove off-screen enemies and update score
    enemy_cars = [car for car in enemy_cars if car.y < HEIGHT]
    score += 1

    # Collision detection
    for car in enemy_cars:
        if player_car.colliderect(car):
            game_over()

    # Draw everything
    draw_road()
    draw_player()
    draw_enemies()
    show_score()

    pygame.display.flip()

pygame.quit()
