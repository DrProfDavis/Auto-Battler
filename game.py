import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame App")

# Set up colors
red = (255, 0, 0)

# Set up the player rectangle
player_size = 50
player_x = (width - player_size) // 2
player_y = height - player_size - 10

# Set up clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update player position based on arrow key input
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += 5

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the player rectangle
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
