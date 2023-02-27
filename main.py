import pygame
from sys import exit

#Score system
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_sf = t_font.render(("score:")  + f"{current_time}", False, (28, 252, 3))
    score_rekt = score_sf.get_rect(center=(200, 100))
    screen.blit(score_sf,score_rekt)
    return current_time
def player_animations():
    global playersurf, playerindex
    if playerrekt.bottom < 390:
        playersurf = playerjump
    else:
        playerindex += 0.4
        if playerindex >= len(playerwalk): playerindex = 0
        playersurf = playerwalk[int(playerindex)]
pygame.init()
isgameon = False
pygame.display.set_caption("METROID RUNNER!")
t_font = pygame.font.Font("Font.ttf",50)
t2_font = pygame.font.Font("Font.ttf",20)

screen = pygame.display.set_mode((800,600))
fpsclock = pygame.time.Clock()

background = pygame.image.load("bk.jpeg").convert_alpha()
background2 = pygame.image.load("bk2.png").convert_alpha()




player_surface1 = pygame.image.load("samusani/1.gif").convert_alpha()
player_surface2 = pygame.image.load("samusani/2.gif").convert_alpha()
player_surface3 = pygame.image.load("samusani/3.gif").convert_alpha()
player_surface4 = pygame.image.load("samusani/4.gif").convert_alpha()
player_surface5 = pygame.image.load("samusani/5.gif").convert_alpha()
player_surface6 = pygame.image.load("samusani/6.gif").convert_alpha()
player_surface7 = pygame.image.load("samusani/7.gif").convert_alpha()
player_surface8 = pygame.image.load("samusani/8.gif").convert_alpha()
player_surface9 = pygame.image.load("samusani/9.gif").convert_alpha()
player_surface10 = pygame.image.load("samusani/10.gif").convert_alpha()
playerwalk= [player_surface1,player_surface2,player_surface3,player_surface4,player_surface5,player_surface6,player_surface7,player_surface8,player_surface9,player_surface10]
playerindex = 0
playersurf = playerwalk[playerindex]
playerjump = pygame.image.load("samusani/4.gif").convert_alpha()
playerrekt = playersurf.get_rect(center = (70,390))
playerrekt.inflate_ip(-50,-50)









pgrav = 0







flysf = pygame.image.load("fly.png")
flyrekt = flysf.get_rect(center = (800,200))
enemy_sf = pygame.image.load("Enemy.png")
enemyrekt= enemy_sf.get_rect(center =(700,390))
enemyrekt.inflate_ip(-30,-30)
start_time = 0
gamestarttext= t2_font.render("Press RETURN to start the game",False,(28,252,3))
gamestarttextrect = gamestarttext.get_rect(center = (400,500))
gamename= t_font.render("Metroid Runner",False,(28,252,3))
gamename_rekt = gamename.get_rect(center = (400,300))
score = 0
enenmymovespeed= 4

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        isgameon = True
        enemyrekt.left = 800
        flyrekt.left = 800
        playerrekt.center = 70,390
        pygame.display.set_caption("METROID RUNNER! ")
        start_time = int(pygame.time.get_ticks()/1000)



    if isgameon:







        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and playerrekt.bottom >= 390:
            pgrav = -20
        if keys[pygame.K_d]:
            playerrekt.x += 9
        if keys[pygame.K_a]:
            playerrekt.x -= 9
        player_animations()

        screen.blit(background, (0, 0))
        screen.blit(background2,(0,450))
        score = display_score()


        enemyrekt.x -= enenmymovespeed
        if enemyrekt.right <= 0 : enemyrekt.left = 800
        screen.blit(enemy_sf,enemyrekt)






        if score > 10:

            flyrekt.x -= 9
            if flyrekt.right <= 0: flyrekt.left = 800
            screen.blit(flysf, flyrekt)


        pgrav += 1
        playerrekt.y += pgrav
        if playerrekt.bottom >= 390 : playerrekt.bottom = 390
        screen.blit(playersurf,playerrekt)


        #End
        if enemyrekt.colliderect(playerrekt):
            pygame.display.set_caption("PRESS RETURN TO RESTART")
            isgameon = False
        elif flyrekt.colliderect(playerrekt):
            pygame.display.set_caption("PRESS RETURN TO RESTART")
            isgameon = False
    else:

        screen.fill((0,0,0))

        screen.blit(gamename,gamename_rekt)
        Winmsg= t_font.render("YOU WON!",False,(28,252,3))
        Winmsgrekt = Winmsg.get_rect(center = (400,500))
        score_msg = t_font.render(f"Score:{score}",False,(28,252,3))
        score_msgrekt= score_msg.get_rect(center = (400,500))
        if score == 0:
            screen.blit(gamestarttext,gamestarttextrect)

        elif score == 50:
            screen.blit(Winmsg,Winmsgrekt)


        else:
            screen.blit(score_msg,score_msgrekt)





    pygame.display.update()
    fpsclock.tick(60)