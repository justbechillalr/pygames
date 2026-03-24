import pygame
import sys
#Starter Spillet
pygame.init()
#Variabler
width, height = 825,700
#Display Settings
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Myworld")
#klokke
clock = pygame.time.Clock()

#Kollisjon












#player/block settings

square_size = 40
square_x = width //2
square_y = height // 2

y_velocity = 0
gravity = 0.6
jump_strength = -12
on_ground = False



#ground
Ground_y = height-50

#General Setting
speed = 5
size = 40
#Game Loop
#hvis spiller er startet/true 
while True:
    #gjøre alt inni denne funktionen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT
            sys.exit()
    
        #Walk Settings
        keys = pygame.key.get_pressed()
                    #event checking if Spacebar is pressed and if its on ground. If both are true do the rest
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                    y_velocity = jump_strength
                    on_ground = False
        #Left Right game
    if keys [pygame.K_a]:
            square_x -= speed
    if keys [pygame.K_d]:
            square_x += speed

    #idk ask håkon
    y_velocity += gravity
    square_y += y_velocity

    #ground logic
    if square_y + size >= Ground_y:
        square_y = Ground_y - size
        y_velocity = 0
        on_ground = True


    

    #Wall so block dont escape
    #variabel
    square_x = max(0, min(width-square_size, square_x))
    square_y = max(0, min(height-square_size, square_y))

   
    #Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(
        screen,
        (0,200,250),
        (square_x, square_y, square_size, square_size)
    )

    pygame.display.flip()
    clock.tick(100)
        
