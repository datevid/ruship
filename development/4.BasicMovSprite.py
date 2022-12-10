import pygame

# initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# create a window
window = pygame.display.set_mode((800, 600))

# define the color of the background (black)
bg_color = (0, 0, 0)

# Load the image of nave espacial or spaceship
shipSurface = pygame.image.load("assets/player.png")
shipSurface=pygame.transform.scale(shipSurface,(50,50))
shipObj=shipSurface.get_rect()

# game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # check for keypress events
        elif event.type == pygame.KEYDOWN:
            # move the rectangle based on the key pressed
            if event.key == pygame.K_LEFT:
                shipObj.x -= 10
            elif event.key == pygame.K_RIGHT:
                shipObj.x += 10
            elif event.key == pygame.K_UP:
                shipObj.y -= 10
            elif event.key == pygame.K_DOWN:
                shipObj.y += 10

    # fill the window with the background color
    window.fill(bg_color)

    # blit (copy) the surface onto the window
    window.blit(shipSurface, shipObj)

    # update the window
    pygame.display.update()

    clock.tick(60)
