import pygame
import random

pygame.init()
pygame.font.init()
pygame.font.get_init()
Screen_width, Screen_height = (800, 600)
screen = pygame.display.set_mode((Screen_width, Screen_height))

clock = pygame.time.Clock()

#player
player_x = Screen_width // 2
player_y = Screen_height - 80
player_speed = 6
player_size = 50

#hearts (health)
player_hearts = 10

#bullets (player)
bullets = []
bullet_speed = 8
bullet_cooldown = 200
last_shot = 0

#enemy bullets
enemy_bullets = []
enemy_bullet_speed = 4

#targets
targets = []
spawn_timer = 0
spawn_delay = 1200
player_color = (255,0,0)

#Colors
black = (0,0,0)
score = 0
#YOU DIED#
#display_surface = pygame.display.setmode((100,100))
font = pygame.font.SysFont(None, 50)

#font settings and values/ variables#

#NPC die counter#
font1 = pygame.font.SysFont('freesanbold.ttf', 50)


running = True
while running:
    text1 = font1.render(f'Score: {score}', True, (0, 255, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (250, 250)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed

    #shoot
    if keys[pygame.K_SPACE]:
        if now - last_shot > bullet_cooldown:
            bullets.append([player_x + 25, player_y])
            last_shot = now

    #spawn enemies
    if now - spawn_timer > spawn_delay:
        spawn_timer = now

        x = random.randint(0, Screen_width - 50)
        y = random.randint(50, 200)

        if random.choice([True, False]):
            hp = 2
            color = (255, 0, 0)
        else:
            hp = 1
            color = (0, 255, 0)

        targets.append([x, y, hp, color, 0])  # last value = shoot timer

    #player bullets
    for b in bullets[:]:
        b[1] -= bullet_speed

        b_rect = pygame.Rect(b[0], b[1], 10, 10)

        hit = False

        for t in targets:
            t_rect = pygame.Rect(t[0], t[1], 50, 50)

            if b_rect.colliderect(t_rect):
                t[2] -= 1
                hit = True
                score += 1
                
                if t[2] <= 0:
                    targets.remove(t)

                break

        if hit or b[1] < 0:
            bullets.remove(b)

    #enemy shooting + movement
    for t in targets:
        t[4] += 1

        #move toward player slowly
        if t[0] < player_x:
            t[0] += 2
        if t[0] > player_x:
            t[0] -= 2

        #enemy shoots every ~1.5 sec
        if t[4] > 90:
            enemy_bullets.append([t[0] + 25, t[1] + 50])
            t[4] = 0

    #enemy bullets move
    for eb in enemy_bullets[:]:
        eb[1] += enemy_bullet_speed

        eb_rect = pygame.Rect(eb[0], eb[1], 10, 10)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        if eb_rect.colliderect(player_rect):
            player_hearts -= 1
            enemy_bullets.remove(eb)
            continue
       
        if eb[1] > Screen_height:
            enemy_bullets.remove(eb)
  
            
    #draw background (sun warm)
    screen.fill((255, 140, 0))
    pygame.draw.circle(screen, (255, 220, 0), (650, 120), 60)
    pygame.draw.circle(screen, (255, 180, 0), (650, 120), 100, 20)

    #player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    #player bullets
    for b in bullets:
        pygame.draw.rect(screen, (255, 0, 0), (b[0], b[1], 10, 10))

    #enemies
    for t in targets:
        pygame.draw.rect(screen, t[3], (t[0], t[1], 50, 50))

    #enemy bullets
    for eb in enemy_bullets:
        pygame.draw.rect(screen, (255, 255, 0), (eb[0], eb[1], 10, 10))

    #hearts UI
    for i in range(player_hearts):
        pygame.draw.rect(screen, (255, 0, 100), (10 + i * 20, 10, 15, 15))
    
    player_dead = player_hearts <= 0
    if player_dead:
        text = font.render('you died', True, (255,0,0))
        screen.blit(text,(300,300))
        with open("highscore.txt", "a") as f:
            f.write("Now the file has more content!")

            #open and read the file after the appending:
        with open("highscore.txt") as f:
            print(f.read())
    screen.blit(text1, textRect1)
        
        ######################
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()