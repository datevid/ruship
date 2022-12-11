import random

import pygame

# initialize Pygame
pygame.init()
screen_width, screen_height = 400, 600
# create a window
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ruship by @Datevid")

clock = pygame.time.Clock()

music = pygame.mixer.music.load('assets/Time-and-Space-Dramatic-Epic-Music.mp3')
pygame.mixer.music.play(-1)

# Load the background image
bgImage = pygame.sprite.Sprite()
bgImage.image = pygame.image.load('assets/bg5.png')
bgImage.image = pygame.transform.scale(bgImage.image, (screen_width, screen_height))
bgImage.rect = bgImage.image.get_rect()

# Create a sprite object for meteor 1
# meteoritos se caracterizan por ser lentos
meteor1 = pygame.sprite.Sprite()
meteor1.image = pygame.image.load("assets/meteor1.png")
meteor1.image = pygame.transform.scale(meteor1.image, (100, 100))
meteor1.rect = meteor1.image.get_rect()
meteor1.rect.x = random.randint(0, screen_width - meteor1.rect.width)
meteor1.rect.y = -100  # fuera de la pantalla
meteor1.speedX = random.uniform(-3, 3)
meteor1.speedY = random.randint(1, 3)
# reducimos el tamaño a nivel interno para apreciar de mejor manera la colisión
meteor1.rect.height = meteor1.rect.height - 15
meteor1.rect.width = meteor1.rect.width - 15

# Create a sprite object for meteor 2
# meteoritos se caracterizan por ser más rápidos que el anterior
meteor2 = pygame.sprite.Sprite()
meteor2.image = pygame.image.load("assets/meteor2.png")
meteor2.image = pygame.transform.scale(meteor2.image, (100, 100))
meteor2.rect = meteor2.image.get_rect()
# meteor2.rect.x = 200
meteor2.rect.x = random.randint(0, screen_width - meteor2.rect.width)
meteor2.rect.y = -200  # fuera de la pantalla
meteor2.speedX = random.uniform(-3, 3)
meteor2.speedY = random.randint(3, 5)
meteor2.rect.height = meteor2.rect.height - 15
meteor2.rect.width = meteor2.rect.width - 15

# Create a sprite object for meteor 3
# meteoritos se caracterizan tener múltiples direcciones
meteor3 = pygame.sprite.Sprite()
meteor3.image = pygame.image.load("assets/asteroid3.png")
meteor3.image = pygame.transform.scale(meteor3.image, (100, 100))
meteor3.rect = meteor3.image.get_rect()
# meteor3.rect.x = 300
meteor3.rect.x = random.randint(0, screen_width - meteor3.rect.width)
meteor3.rect.y = -300  # fuera de la pantalla
meteor3.speedX = random.uniform(-3, 3)
meteor3.speedY = random.randint(-3, 0)
meteor3.rect.height = meteor3.rect.height - 15
meteor3.rect.width = meteor3.rect.width - 15

# Create a sprite object for meteor 4
# meteoritos se caracterizan por ser veloces
meteor4 = pygame.sprite.Sprite()
meteor4.image = pygame.image.load("assets/meteor4.png")
meteor4.image = pygame.transform.scale(meteor4.image, (100, 100))
meteor4.rect = meteor4.image.get_rect()
# meteor4.rect.x = 300
meteor4.rect.x = random.randint(0, screen_width - meteor4.rect.width)
meteor4.rect.y = -300  # fuera de la pantalla
meteor4.speedX = random.uniform(-3, 3)
meteor4.speedY = random.randint(5, 7)  # tienen más velocidad
meteor4.rect.height = meteor4.rect.height - 15
meteor4.rect.width = meteor4.rect.width - 15

# Create a sprite object for meteor 5
# meteoritos se caracterizan por ser muy veloces y a una sola dirección
meteor5 = pygame.sprite.Sprite()
meteor5.image = pygame.image.load("assets/meteor5.png")
meteor5.image = pygame.transform.scale(meteor5.image, (100, 100))
meteor5.rect = meteor5.image.get_rect()
# meteor5.rect.x = 300
meteor5.rect.x = random.randint(0, screen_width - meteor5.rect.width)
meteor5.rect.y = -300  # fuera de la pantalla
meteor5.speedX = random.uniform(-3, 3)
meteor5.speedY = random.randint(7, 10)  # tienen más velocidad
meteor5.rect.height = meteor5.rect.height - 15
meteor5.rect.width = meteor5.rect.width - 15

# ship
ship = pygame.sprite.Sprite()
ship.image = pygame.image.load("assets/ship-0.png")
ship.image = pygame.transform.scale(ship.image, (50, 50))
ship.rect = ship.image.get_rect()
ship.rect.center = (screen_width / 2, screen_height / 2)
ship.speedX = 5
ship.speedY = 5
# reducimos el tamaño a nivel interno para apreciar de mejor manera la colisión
ship.rect.height = ship.rect.height - 20
ship.rect.width = ship.rect.width - 20

# shipExplosion
shipExplosion = pygame.sprite.Sprite()
shipExplosion.image = pygame.image.load("assets/pixel-explosion-png-6.png")
shipExplosion.image = pygame.transform.scale(shipExplosion.image, (50, 50))
shipExplosion.rect = shipExplosion.image.get_rect()
shipExplosion.rect.center = (screen_width / 2, screen_height / 2)


# font
# Create a font file by passing font file
# and size of the font
#font1 = pygame.font.SysFont('freesanbold.ttf', 60)
#font2 = pygame.font.SysFont('chalkduster.ttf', 50)
#font3 = pygame.font.SysFont(None, 30)
#font4 = pygame.font.SysFont(None, 30)
fontJoystixPath="assets/joystix monospace.ttf"
font1 = pygame.font.Font(fontJoystixPath, 45)
font2 = pygame.font.Font(fontJoystixPath, 35)
font3 = pygame.font.Font(fontJoystixPath, 20)
font4 = pygame.font.Font(fontJoystixPath, 20)

# Render the texts that you want to display
text1 = font1.render('Game Over', True, (0, 255, 0))
text2 = font2.render('Download code', True, (0, 255, 0))
text3 = font3.render('Github/Datevid', True, (0, 255, 0))
text4 = font4.render('Thanks ^_^', True, (0, 255, 0))
# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()

textRect1.center = (screen_width / 2, screen_height / 2 - 100)
textRect2.center = (screen_width / 2, screen_height / 2)
textRect3.center = (screen_width / 2, screen_height / 2 + 100)
textRect4.center = (screen_width / 2, screen_height / 2 + 200)

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
            # set x random position initial:
            meteor1.rect.y = -200
            meteor1.rect.x = random.randint(0, screen_width - meteor1.rect.width)

            # random speed meteors
            meteor1.speedX = random.uniform(-3, 3)
            meteor1.speedY = random.randint(1, 7)
        if meteor1.rect.right - 200 >= screen_width or meteor1.rect.left + 200 <= 0:
            meteor1.rect.x = -200

        # mov meteor 2
        meteor2.rect.x += meteor2.speedX
        meteor2.rect.y += meteor2.speedY
        if meteor2.rect.bottom - 200 >= screen_height or meteor2.rect.top + 200 <= 0:
            # set x random position initial:
            meteor2.rect.y = -200
            meteor2.rect.x = random.randint(0, screen_width - meteor2.rect.width)

            # random speed meteors
            meteor2.speedX = random.uniform(-3, 3)
            meteor2.speedY = random.randint(1, 7)
        if meteor2.rect.right - 200 >= screen_width or meteor2.rect.left + 200 <= 0:
            meteor2.rect.x = -200

        # mov meteor 3
        meteor3.rect.x += meteor3.speedX
        meteor3.rect.y += meteor3.speedY
        if meteor3.rect.bottom - 200 >= screen_height or meteor3.rect.top + 200 <= 0:
            # set x random position initial:
            meteor3.rect.y = -200
            meteor3.rect.x = random.randint(0, screen_width - meteor3.rect.width)

            # random speed meteors
            meteor3.speedX = random.uniform(-3, 3)
            meteor3.speedY = random.randint(1, 7)
        if meteor3.rect.right - 200 >= screen_width or meteor3.rect.left + 200 <= 0:
            meteor3.rect.x = -200

        # mov meteor 4
        meteor4.rect.x += meteor4.speedX
        meteor4.rect.y += meteor4.speedY
        if meteor4.rect.bottom - 200 >= screen_height or meteor4.rect.top + 200 <= 0:
            # set x random position initial:
            meteor4.rect.y = -200
            meteor4.rect.x = random.randint(0, screen_width - meteor4.rect.width)

            # random speed meteors
            meteor4.speedX = random.uniform(-3, 3)
            meteor4.speedY = random.randint(5, 10)  # tienen más velocidad
        if meteor4.rect.right - 200 >= screen_width or meteor4.rect.left + 200 <= 0:
            meteor4.rect.x = -200

        # mov meteor 5
        meteor5.rect.x += meteor5.speedX
        meteor5.rect.y += meteor5.speedY
        if meteor5.rect.bottom - 200 >= screen_height or meteor5.rect.top + 200 <= 0:
            # set x random position initial:
            meteor5.rect.y = -200
            meteor5.rect.x = random.randint(0, screen_width - meteor5.rect.width)

            # random speed meteors
            meteor5.speedX = random.uniform(-3, 3)
            meteor5.speedY = random.randint(5, 10)  # tienen más velocidad
        if meteor5.rect.right - 200 >= screen_width or meteor5.rect.left + 200 <= 0:
            meteor5.rect.x = -200

        # fill the window with the background color
        # Draw the background image
        window.blit(bgImage.image, bgImage.rect)

        # draw meteor1
        window.blit(meteor1.image, meteor1.rect)
        window.blit(meteor2.image, meteor2.rect)
        window.blit(meteor3.image, meteor3.rect)
        window.blit(meteor4.image, meteor4.rect)
        window.blit(meteor5.image, meteor5.rect)

        # window.blit(shipSurface,(100,100),shipObj)
        window.blit(ship.image, ship.rect)

        # check colision
        if ship.rect.colliderect(meteor1.rect):
            window.blit(shipExplosion.image, ship.rect)
            notCollision = False

        if ship.rect.colliderect(meteor2.rect):
            window.blit(shipExplosion.image, ship.rect)
            notCollision = False

        if ship.rect.colliderect(meteor3.rect):
            window.blit(shipExplosion.image, ship.rect)
            notCollision = False

        if ship.rect.colliderect(meteor4.rect):
            window.blit(shipExplosion.image, ship.rect)
            notCollision = False

        if ship.rect.colliderect(meteor5.rect):
            window.blit(shipExplosion.image, ship.rect)
            notCollision = False

    else:
        # font
        window.blit(text1, textRect1)
        window.blit(text2, textRect2)
        window.blit(text3, textRect3)
        window.blit(text4, textRect4)

    # update the window
    pygame.display.update()

    clock.tick(60)
