import pygame

# initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# create a window
window = pygame.display.set_mode((800, 600))

# define the color of the background (black)
bg_color = (0, 0, 0)

rect_x_ini=100
rect_y_ini=100

# define the color of the rectangle (red, green, blue)
# sprite con color
rect_color = (255, 0, 0)

# create a surface to draw on
# sprite con superficie
rect_surface = pygame.Surface((rect_x_ini, rect_y_ini))

# fill the surface with the rectangle color
# asignamos el color al sprite
rect_surface.fill(rect_color)

# create a rectangle object to track the position
rectObj = rect_surface.get_rect()

ballColor=(255,255,255)
ballSurface=pygame.Surface((20,20))
ballSurface.fill(ballColor)
ballObj=ballSurface.get_rect()

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
                rectObj.x -= 10
            elif event.key == pygame.K_RIGHT:
                rectObj.x += 10
            elif event.key == pygame.K_UP:
                rectObj.y -= 10
            elif event.key == pygame.K_DOWN:
                rectObj.y += 10

    # fill the window with the background color
    window.fill(bg_color)

    # blit (copy) the surface onto the window
    window.blit(rect_surface, rectObj)
    
    window.blit(ballSurface, ballObj)

    # update the window
    pygame.display.update()

    clock.tick(60)
