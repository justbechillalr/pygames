#imports pygame#
import pygame
#launches pygame#
pygame.init()
Screen_width, Screen_height = ((800,600))
#setting screen As the value for the screen settings#
screen = pygame.display.set_mode((Screen_width,Screen_height))
#Pregame: values naming#
#Clock settings#
clock = pygame.time.Clock()
#Box spawn#
box_y = Screen_height / 1.2
box_x = Screen_width / 2
#Box settings#

box_height = 50
box_width =  50

#Game settings#
speed = 10

#main game loop#
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Movement Settings#
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        box_x -= speed
    if keys[pygame.K_d]:
        box_x += speed
    #keeps Box in screen#
    box_x = max (0, min(Screen_width- box_width,box_x))
    box_y = max (0, min(Screen_height- box_height,box_y))
#background color#
    screen.fill((0,0,0))
    #laster inn Box#
    pygame.draw.rect(
        screen,
        (0,200,255),
        (box_x,box_y,box_width,box_height)
    )
    #Screen logic#
    pygame.display.flip()
    #Clock activated#
    clock.tick(60)
    #Makes game stop if exit#
pygame.quit()