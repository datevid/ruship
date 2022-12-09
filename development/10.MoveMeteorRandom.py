import random

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

# Create a sprite object for meteor 1
meteor1 = pygame.sprite.Sprite()
meteor1.image = pygame.image.load("../assets/asteroid1.png")
meteor1.image = pygame.transform.scale(meteor1.image, (100, 100))
meteor1.rect = meteor1.image.get_rect()
#meteor1.rect.x = 200
meteor1.rect.x = random.randint(0, screen_width-meteor1.rect.width)
meteor1.rect.y = -100  # fuera de la pantalla
meteor1.speedX = -1.2
meteor1.speedY = random.randint(1,7)
# reducimos el tamaño a nivel interno para apreciar de mejor manera la colisión
meteor1.rect.height = meteor1.rect.height-15
meteor1.rect.width = meteor1.rect.width-15

# Create a sprite object for meteor 1
meteor2 = pygame.sprite.Sprite()
meteor2.image = pygame.image.load("../assets/asteroid2.png")
meteor2.image = pygame.transform.scale(meteor2.image, (100, 100))
meteor2.rect = meteor2.image.get_rect()
#meteor2.rect.x = 200
meteor2.rect.x = random.randint(0, screen_width-meteor2.rect.width)
meteor2.rect.y = -200  # fuera de la pantalla
meteor2.speedX = -0.5
meteor2.speedY = random.randint(1,7)
meteor2.rect.height = meteor2.rect.height-15
meteor2.rect.width = meteor2.rect.width-15

# Create a sprite object for meteor 1
meteor3 = pygame.sprite.Sprite()
meteor3.image = pygame.image.load("../assets/meteor3.png")
meteor3.image = pygame.transform.scale(meteor3.image, (100, 100))
meteor3.rect = meteor3.image.get_rect()
#meteor3.rect.x = 300
meteor3.rect.x = random.randint(0, screen_width-meteor3.rect.width)
meteor3.rect.y = -300  # fuera de la pantalla
meteor3.speedX = -0.2
meteor3.speedY = random.randint(1,7)
meteor3.rect.height = meteor3.rect.height-15
meteor3.rect.width = meteor3.rect.width-15

# ship
ship = pygame.sprite.Sprite()
ship.image = pygame.image.load("../assets/player.png")
ship.image = pygame.transform.scale(ship.image, (50, 50))
ship.rect = ship.image.get_rect()
ship.rect.center = (screen_width / 2, screen_height / 2)
ship.speedX = 5
ship.speedY = 5
# reducimos el tamaño a nivel interno para apreciar de mejor manera la colisión
ship.rect.height = ship.rect.height-10
ship.rect.width = ship.rect.width-10

#font = pygame.font.Font(None, 20)
game_over_font = pygame.font.SysFont('Verdana', 60)

# Flag to track whether the left or right key is being pressed
left_key_pressed = False
right_key_pressed = False
top_key_pressed = False
bottom_key_pressed = False

notCollision = True

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

    if notCollision:

        # Move the sprite if a key is being pressed
        if left_key_pressed:
            ship.rect.x -= 10
        elif right_key_pressed:
            ship.rect.x += 10
        elif top_key_pressed:
            ship.rect.y -= 10
        elif bottom_key_pressed:
            ship.rect.y += 10

        # mov meteor 1
        meteor1.rect.x += meteor1.speedX
        meteor1.rect.y += meteor1.speedY
        if meteor1.rect.bottom - 200 >= screen_height or meteor1.rect.top + 200 <= 0:
            #set y initial
            meteor1.rect.y = -200

            # set x random position initial:
            meteor1.rect.x = random.randint(0, screen_width - meteor1.rect.width)

            # random speed meteors
            meteor1.speedY = random.randint(1, 7)
        if meteor1.rect.right - 200 >= screen_width or meteor1.rect.left + 200 <= 0:
            meteor1.rect.x = -200

        # mov meteor 2
        meteor2.rect.x += meteor2.speedX
        meteor2.rect.y += meteor2.speedY
        if meteor2.rect.bottom - 200 >= screen_height or meteor2.rect.top + 200 <= 0:
            # set y initial
            meteor2.rect.y = -200

            # set x random position initial:
            meteor2.rect.x = random.randint(0, screen_width - meteor2.rect.width)

            # random speed meteors
            meteor2.speedY = random.randint(1, 7)
        if meteor2.rect.right - 200 >= screen_width or meteor2.rect.left +200 <= 0:
            meteor2.rect.x=-200

        # mov meteor 3
        meteor3.rect.x += meteor3.speedX
        meteor3.rect.y += meteor3.speedY
        if meteor3.rect.bottom - 200 >= screen_height or meteor3.rect.top + 200 <= 0:
            # set y initial
            meteor3.rect.y = -200

            # set x random position initial:
            meteor3.rect.x = random.randint(0, screen_width - meteor3.rect.width)

            # random speed meteors
            meteor3.speedY = random.randint(1, 7)
        if meteor3.rect.right - 200 >= screen_width or meteor3.rect.left + 200 <= 0:
            meteor3.rect.x=-200

        # fill the window with the background color
        window.fill(bg_color)

        # draw meteor1
        window.blit(meteor1.image, meteor1.rect)
        window.blit(meteor2.image, meteor2.rect)
        window.blit(meteor3.image, meteor3.rect)

        # window.blit(shipSurface,(100,100),shipObj)
        window.blit(ship.image, ship.rect)

        # check colision
        if ship.rect.colliderect(meteor1.rect):
            pygame.draw.rect(window, (255, 0, 0), ship.rect, 1)
            pygame.draw.rect(window, (255, 125, 125), meteor1.rect, 1)
            notCollision = False

        if ship.rect.colliderect(meteor2.rect):
            pygame.draw.ellipse(window, (255, 125, 125), ship.rect, 1)
            pygame.draw.rect(window, (255, 125, 125), meteor2.rect, 1)
            notCollision = False

        if ship.rect.colliderect(meteor3.rect):
            pygame.draw.ellipse(window, (255, 125, 125), ship.rect, 1)
            pygame.draw.rect(window, (255, 125, 125), meteor3.rect, 1)
            notCollision = False




        #pygame.draw.rect(window, (255, 0, 0), ship.rect, 1)

        # update the window
        pygame.display.update()
    else:
        #print("No está en juego, sin embargo deben mostrarse el game over en esta zona.")
        game_over = game_over_font.render("Game Over", True, (255, 0, 0))

    clock.tick(60)
