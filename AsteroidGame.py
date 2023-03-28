import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroids")

# Load the player, asteroid, and bullet images
player_image = pygame.image.load("assets/player.png").convert_alpha()
asteroid_image = pygame.image.load("assets/asteroid.png").convert_alpha()
bullet_image = pygame.image.load("assets/bullet.png").convert_alpha()

# Set the size of the player, asteroid, and bullet images
player_size = (50, 50)
asteroid_size = (50, 50)
bullet_size = (10, 10)
player_image = pygame.transform.scale(player_image, player_size)
asteroid_image = pygame.transform.scale(asteroid_image, asteroid_size)
bullet_image = pygame.transform.scale(bullet_image, bullet_size)

# Set up the player, asteroid, and bullet sprites
player_rect = player_image.get_rect()
player_rect.centerx = screen_width / 2
player_rect.centery = screen_height / 2
asteroid_list = []
bullet_list = []

# Set up the game loop
game_running = True
clock = pygame.time.Clock()
score = 0
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.centery = player_rect.centery
                bullet_list.append(bullet_rect)

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player_rect.move_ip(0, 5)

    # Spawn new asteroids
    if random.randint(1, 50) == 1:
        asteroid_rect = asteroid_image.get_rect()
        asteroid_rect.centerx = random.randint(0, screen_width)
        asteroid_rect.centery = -50
        asteroid_list.append(asteroid_rect)

    # Move the asteroids and bullets
    for asteroid_rect in asteroid_list:
        asteroid_rect.move_ip(0, 5)
        if asteroid_rect.centery > screen_height + 50:
            asteroid_list.remove(asteroid_rect)
        if asteroid_rect.colliderect(player_rect):
            game_running = False
        for bullet_rect in bullet_list:
            if asteroid_rect.colliderect(bullet_rect):
                asteroid_list.remove(asteroid_rect)
                bullet_list.remove(bullet_rect)
                score += 10

    for bullet_rect in bullet_list:
        bullet_rect.move_ip(0, -10)
        if bullet_rect.centery < -50:
            bullet_list.remove(bullet_rect)

    # Draw game objects
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    for asteroid_rect in asteroid_list:
        screen.blit(asteroid_image, asteroid_rect)
    for bullet_rect in bullet_list:
        screen.blit(bullet_image, bullet_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score),True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display and limit the frame rate
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()