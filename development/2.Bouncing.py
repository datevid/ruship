import pygame

# initialize Pygame
pygame.init()
screen_width,screen_height=800,600
# create a window
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite pixel by @Datevid")

clock = pygame.time.Clock()

# define the color of the background (black)
bg_color = (0, 0, 0)

# define the color of the pixel (red, green, blue)
spriteColor = (255, 125, 125)

# create object x y width height
spriteObj=pygame.Rect(0,0,30,30)
spriteObj.center=(screen_width/2,screen_height/2)

spriteSpeedX,spriteSpeedY=5,5
# wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    spriteObj.x+=spriteSpeedX
    spriteObj.y+=spriteSpeedY
    if spriteObj.bottom >=screen_height or spriteObj.top <= 0:
        spriteSpeedY*=-1
    if spriteObj.right >= screen_width or spriteObj.left <=0:
        spriteSpeedX*=-1

    # fill the window with the background color
    window.fill(bg_color)

    pygame.draw.ellipse(window,spriteColor,spriteObj)
    # blit (copy) the surface onto the window
    #window.blit(spriteSurface, spriteObj)

    # update the window
    pygame.display.update()

    clock.tick(60)
