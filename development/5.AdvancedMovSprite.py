import pygame

# initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# create a window
window = pygame.display.set_mode((800, 600))

# define the color of the background (black)
bg_color = (0, 0, 0)

# Load the image of nave espacial or spaceship
shipSurface = pygame.image.load("../assets/player.png")
shipSurface=pygame.transform.scale(shipSurface,(50,50))
shipObj=shipSurface.get_rect()

# Flag to track whether the left or right key is being pressed
left_key_pressed = False
right_key_pressed = False
top_key_pressed=False
bottom_key_pressed=False

# game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
         # chek for keypress events for spaceship
        elif event.type == pygame.KEYDOWN:
            # Handle key down events
            if event.key == pygame.K_LEFT:
                # Set the left key flag to True
                left_key_pressed = True
            elif event.key == pygame.K_RIGHT:
                # Set the right key flag to True
                right_key_pressed = True
            elif event.key == pygame.K_UP:
                top_key_pressed = True
            elif event.key == pygame.K_DOWN:
                bottom_key_pressed=True
        elif event.type == pygame.KEYUP:
            # Handle key up events
            if event.key == pygame.K_LEFT:
                # Set the left key flag to False
                left_key_pressed = False
            elif event.key == pygame.K_RIGHT:
                # Set the right key flag to False
                right_key_pressed = False
            elif event.key == pygame.K_UP:
                top_key_pressed = False
            elif event.key == pygame.K_DOWN:
                bottom_key_pressed=False

    # Move the sprite if a key is being pressed
    if left_key_pressed:
        shipObj.x -= 10
    elif right_key_pressed:
        shipObj.x += 10
    elif top_key_pressed:
        shipObj.y -= 10
    elif bottom_key_pressed:
        shipObj.y += 10
        
    # fill the window with the background color
    window.fill(bg_color)

    # blit (copy) the surface onto the window
    window.blit(shipSurface, shipObj)

    # update the window
    pygame.display.update()

    clock.tick(60)
