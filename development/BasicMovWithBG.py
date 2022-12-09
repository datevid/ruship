import pygame

# Initialize Pygame
pygame.init()

# Load the sprite image
sprite_image = pygame.image.load('../assets/player.png')

# Load the background image
background_image = pygame.image.load('../assets/bg3.gif')

# Create a Pygame display with the same dimensions as the background image
display = pygame.display.set_mode(background_image.get_size())

# Define the position of the sprite
sprite_pos = [0, 0]

# Define the speed of the sprite (pixels per frame)
sprite_speed = [3, 3]

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the sprite
    sprite_pos[0] += sprite_speed[0]
    sprite_pos[1] += sprite_speed[1]

    # Check if the sprite has moved off the screen
    if sprite_pos[0] < 0 or sprite_pos[0] > display.get_width() - sprite_image.get_width():
        sprite_speed[0] = -sprite_speed[0]
    if sprite_pos[1] < 0 or sprite_pos[1] > display.get_height() - sprite_image.get_height():
        sprite_speed[1] = -sprite_speed[1]

    # Draw the background image
    display.blit(background_image, (0, 0))

    # Draw the sprite
    display.blit(sprite_image, sprite_pos)

    # Update the display
    pygame.display.update()
