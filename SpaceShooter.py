#imports pygame
import pygame
import random
#launches pygame
pygame.init()
Screen_width, Screen_height = ((800,600))
#setting screen As the value for the screen settings#
screen = pygame.display.set_mode((Screen_width,Screen_height))
#Pregame: values naming#
#cooldownsystem#
Shoot_cooldown = 190
last_shot_time = 0
#farger
normal_color= (0,255,0)
hit_color = (255,0,0)

#Clock settings#
clock = pygame.time.Clock()
#Box spawn#
player_y = Screen_height / 1.2
player_x = Screen_width / 2
#Box settings#
player_size = 50
player_height = 50
player_width =  50
#bullets settings#
bullet_width = 10
bullet_height = 10
bullet_speed = 8
bullets = []
#Game settings#
speed = 10
#text dumy spawn#
target_y = Screen_height//2
target_x = Screen_width //2
target = pygame.Rect(target_x,target_y,player_width,player_height)
target_color = normal_color
target_list = pygame.Rect(target_x, target_y, player_width, player_width)

#statement

#fly = (Screen_width//2, Screen_height//2, size, size)

#dummy/bullet colide settings#
#main game loop#
running = True
while running:
    #first variables#
    now = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Movement Settings#
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_s]:
        player_y += speed
    if keys[pygame.K_SPACE]:
        if now - last_shot_time > Shoot_cooldown:
            testBullet = pygame.Rect(target_x,target_y,player_width,player_height)
            colliding = testBullet.colliderect(target)
            #Fire bullets
            bullet_x = player_x + player_size //2
            bullet_y = player_y + player_size // 2 - bullet_height // 2
            bullets.append([bullet_x, bullet_y])
            #resets cooldown#
            last_shot_time = now

    #move the bullet#
    
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            testBullet = pygame.Rect(bullet[0],bullet[1],bullet_width,bullet_height)
        
    
        if colliding:
            target_color = hit_color
            bullets.remove(bullet)
            

        


                                    
    #keeps Box in screen#
    player_x = max (0, min(Screen_width  - player_width,player_x))
    player_y = max (0, min(Screen_height - player_height,player_y))
    #background color#
    
    #screeen#                                LOADING SETTINGS
    screen.fill((0,0,0))

       #Target#
    pygame.draw.rect(
        screen,
        normal_color,
        (target_x,target_y,player_width,player_height)
    )
    #laster inn Box#
    pygame.draw.rect(
        screen,
        (0,255,255),
        (player_x,player_y,player_width,player_height)
    )
    #Loading bullets#
    for bullet in bullets[:]:
        pygame.draw.rect(
            screen,
            (255,0,0),
            (bullet[0],bullet[1],bullet_width,bullet_height)
        )
    #Screen logic#
    pygame.display.flip()
    #Clock activated#
    clock.tick(60)
    #Makes game stop if exit#
pygame.quit()