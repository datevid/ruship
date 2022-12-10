# Import the Pygame module
import sys

import pygame

# Define the size of the display window
width = 800
height = 600

# Initialize Pygame
pygame.init()

# Create the display window
screen = pygame.display.set_mode((width, height))

# Load the explosion animation image
explosion_image = pygame.image.load("../assets/Explosion.png")

# Extract the individual frames from the image
frame_width = explosion_image.get_width() / 12
frame_height = explosion_image.get_height()
explosion_frames = []
for i in range(12):
    x = i * frame_width
    y = 0
    frame_rect = (x, y, frame_width, frame_height)
    frame_image = explosion_image.subsurface(frame_rect)
    explosion_frames.append(frame_image)

# Set the initial frame index to 0
frame_index = 0

# Set the initial position of the explosion
pos_x = 0
pos_y = 0

# Set the animation speed in frames per second
fps = 30

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Process any events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the frame index
    frame_index += 1
    if frame_index >= len(explosion_frames):
        frame_index = 0

    # Draw the current frame of the explosion animation
    screen.blit(explosion_frames[frame_index], (pos_x, pos_y))

    # Update the display
    pygame.display.update()

    # Set the frame rate to the desired FPS
    clock.tick(fps)
