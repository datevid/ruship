import pygame

# initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
# create a window
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ship pixel by @Datevid")

clock = pygame.time.Clock()

# define the color of the background (black)
bg_color = (0, 0, 0)

# Create a sprite object
meteor1 = pygame.sprite.Sprite()
meteor1.image = pygame.image.load("assets/asteroid1.png")
meteor1.image = pygame.transform.scale(meteor1.image, (100, 100))
meteor1.rect = meteor1.image.get_rect()
meteor1.rect.x = 100
meteor1.rect.y = -100 #fuera de la pantalla
meteor1.speedX = 1
meteor1.speedY = 1

#ship
ship = pygame.sprite.Sprite()
ship.image = pygame.image.load("assets/player.png")
ship.image = pygame.transform.scale(ship.image, (50, 50))
ship.rect = ship.image.get_rect()
ship.rect.center = (screen_width / 2, screen_height / 2)
ship.speedX = 5
ship.speedY = 5

# obstacule
# obstaculeObj = pygame.Rect(400, 200, 100, 100)

# Flag to track whether the left or right key is being pressed
left_key_pressed = False
right_key_pressed = False
top_key_pressed = False
bottom_key_pressed = False
# wait for the user to close the window
while True:
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
                bottom_key_pressed = True
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
                bottom_key_pressed = False

    # Move the sprite if a key is being pressed
    if left_key_pressed:
        ship.rect.x -= 10
    elif right_key_pressed:
        ship.rect.x += 10
    elif top_key_pressed:
        ship.rect.y -= 10
    elif bottom_key_pressed:
        ship.rect.y += 10

    # mov meteor
    meteor1.rect.x += meteor1.speedX
    meteor1.rect.y += meteor1.speedY
    if meteor1.rect.bottom - 200 >= screen_height or meteor1.rect.top + 200 <= 0:
        meteor1.speedY *= -1
    if meteor1.rect.right - 200 >= screen_width or meteor1.rect.left + 200 <= 0:
        meteor1.speedX *= -1

    # fill the window with the background color
    window.fill(bg_color)

    # pygame.draw.ellipse(window, asteroideColor, asteroideObj)
    # blit (copy) the surface onto the window
    # window.blit(spriteSurface, spriteObj)

    # draw meteor1
    window.blit(meteor1.image, meteor1.rect)

    # window.blit(shipSurface,(100,100),shipObj)
    window.blit(ship.image, ship.rect)

    if ship.rect.colliderect(meteor1.rect):
        pygame.draw.rect(window, (255, 125, 125), ship.rect, 4)

    # update the window
    pygame.display.update()

    clock.tick(60)
