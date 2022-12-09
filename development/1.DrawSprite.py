import pygame

# initialize Pygame
pygame.init()

# create a window
window = pygame.display.set_mode((800, 600))

# define the color of the pixel (red, green, blue)
pixel_color = (255, 125, 125)

# create a surface to draw on
surface = pygame.Surface((10, 10))

# fill the surface with the pixel color
surface.fill(pixel_color)

# blit (copy) the surface onto the window
window.blit(surface, (100, 100))

# update the window
pygame.display.update()

# wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
