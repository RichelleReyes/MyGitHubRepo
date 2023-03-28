import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroids")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player sprite
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.centerx = screen_width / 2
player_rect.centery = screen_height / 2
player_speed = 5

# Set up the asteroid sprite
asteroid_image = pygame.image.load("asteroid.png")
asteroid_rect = asteroid_image.get_rect()
asteroid_rect.centerx = random.randint(0, screen_width)
asteroid_rect.centery = random.randint(0, screen_height)
asteroid_speed = 3

# Set up the game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Handle player movement
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        player_rect.move_ip(-player_speed, 0)
    if keys_pressed[pygame.K_RIGHT]:
        player_rect.move_ip(player_speed, 0)
    if keys_pressed[pygame.K_UP]:
        player_rect.move_ip(0, -player_speed)
    if keys_pressed[pygame.K_DOWN]:
        player_rect.move_ip(0, player_speed)

    # Update game objects
    asteroid_rect.move_ip(0, asteroid_speed)
    if asteroid_rect.bottom > screen_height:
        asteroid_rect.top = 0
        asteroid_rect.centerx = random.randint(0, screen_width)

    # Draw game objects
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(asteroid_image, asteroid_rect)
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()