import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 720/2, 1280/2
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame App")

# Set up the background image
background_image = pygame.image.load("./Projects/Auto-Battler/images/background.png")
original_bg_width, original_bg_height = background_image.get_size()
scaled_bg_width = original_bg_width // 3
scaled_bg_height = original_bg_height // 3
background_image = pygame.transform.scale(background_image, (scaled_bg_width, scaled_bg_height))


# Set up the player image
player_image = pygame.image.load("./Projects/Auto-Battler/images/cowboy.png")
original_width, original_height = player_image.get_size()
scaled_width = 180  # Adjust this to your desired width
scaled_height = int((scaled_width / original_width) * original_height)
player_image = pygame.transform.scale(player_image, (scaled_width, scaled_height))
player_rect = player_image.get_rect()

# Set the player's initial position higher and to the right on the screen
initial_x_position = (width - scaled_width) // 2 + -100  # Adjust this to your desired x-coordinate
initial_y_position = height - scaled_height - 350  # Adjust this to your desired y-coordinate
player_rect.topleft = (initial_x_position, initial_y_position)

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
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < width:
        player_rect.x += 5

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the background image
    screen.blit(background_image, (0, -65))

    # Draw the scaled player image
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)