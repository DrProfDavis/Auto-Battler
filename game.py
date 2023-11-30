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
move_background = False

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

# Set up the button
button_offset = 300
button_rect = pygame.Rect(20, 20 + button_offset, 100, 50)
button_color = (0, 255, 0)  # Green
button_text = pygame.font.Font(None, 36).render("Move Left", True, (0, 0, 0))  # Black

# Set up clock to control the frame rate
clock = pygame.time.Clock()

# Variable to control background movement
move_background = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                move_background = not move_background  # Toggle the state


    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update player position based on arrow key input
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < width:
        player_rect.x += 5

    # Move background left if the button is pressed
    if move_background:
        background_rect = background_image.get_rect()
        screen.fill((255, 255, 255))
        screen.blit(background_image, background_rect)
        background_rect.x -= 500

    # Draw the background image
    else:
        screen.fill((255, 255, 255))
        screen.blit(background_image, (0, -65))

    # Draw the scaled player image
    screen.blit(player_image, player_rect)

    # Draw the button
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (30, 30 + button_offset))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)