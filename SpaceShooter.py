#imports pygame
import pygame
#launches pygame
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
box_size = 50
box_height = 50
box_width =  50
#bullets settings#
bullet_width = 10
bullet_height = 10
bullet_speed = 8
bullets = []

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
    if keys[pygame.K_SPACE]:
        
    #Fire bullets
        bullet_x = box_x + box_size //2
        bullet_y = box_y + box_size // 2 - bullet_height // 2
        bullets.append([bullet_x, bullet_y])
    #move the bullet#
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] > Screen_height:
            bullets.remove(bullet)

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
    #Loading bullets#
    for bullet in bullets:
        pygame.draw.rect(
            screen,
            (255,0,0),
            (bullet[0], bullet[1],bullet_width,bullet_height)
        )
    #Screen logic#
    pygame.display.flip()
    #Clock activated#
    clock.tick(60)
    #Makes game stop if exit#
pygame.quit()