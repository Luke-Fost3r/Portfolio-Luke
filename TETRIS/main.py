#more comments added tn 10/12
import pygame
import extra
import time
import random
from sys import exit

pygame.init()

width, height = 402,570

pygame.display.set_caption('TETRIS')
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

def display_background():

    #backdrop surfaces
    l_side = pygame.Surface((100,570))
    r_side = pygame.Surface((2,570))
    b_side = pygame.Surface((402,10))
    
    l_side.fill("gray59")
    r_side.fill("gray59")
    b_side.fill("gray59")

    #top bar surface
    top_bar = pygame.Surface((402,50))
    top_bar.fill("white")

    #score box surface
    score_box = pygame.Surface((90,30))
    score_box.fill("black")

    #peice up next surface
    up_next = pygame.Surface((60,60))
    up_next.fill("black")

    screen.blit(l_side,(0,0))
    screen.blit(r_side,(400,0))
    screen.blit(b_side,(0,560))
    screen.blit(top_bar,(0,0))
    screen.blit(score_box,(5,70))
    screen.blit(up_next,(20,150))


    #TITLE letter surfaces
    #T
    t1 = pygame.Surface((21,7))
    t1.fill("red")
    t2 = pygame.Surface((7,28))
    t2.fill("red")
    screen.blit(t1,(10,10))
    screen.blit(t2,(17,17))

    #E
    e1 = pygame.Surface((21,7))
    e1.fill("orange")
    e2 = pygame.Surface((7,28))
    e2.fill("orange")
    screen.blit(e1,(38,10))
    screen.blit(e1,(38,24))
    screen.blit(e1,(38,38))
    screen.blit(e2,(38,17))

    #T2
    t1.fill("yellow")
    t2 = pygame.Surface((7,28))
    t2.fill("yellow")
    screen.blit(t1,(65,10))
    screen.blit(t2,(72,17))

    #R
    r1 = pygame.Surface((7,35))
    r1.fill("green")
    r2 = pygame.Surface((14,7))
    r2.fill("green")
    r3 = pygame.Surface((7,7))
    r3.fill("green")
    screen.blit(r1,(93,10))
    screen.blit(r2,(100,10))
    screen.blit(r2,(100,24))
    screen.blit(r3,(107,17))
    screen.blit(r3,(100,31))
    screen.blit(r3,(107,38))

    #I
    i = pygame.Surface((7,35))
    i.fill("blue")
    screen.blit(i,(121,10))

    #S
    s1 = pygame.Surface((21,7))
    s1.fill("purple")
    s2 = pygame.Surface((7,7))
    s2.fill("purple")
    screen.blit(s1,(135,10))
    screen.blit(s1,(135,24))
    screen.blit(s1,(135,38))
    screen.blit(s2,(135,17))
    screen.blit(s2,(149,31))

def blit_score(score):
    font = pygame.font.Font(None, 40) 
    score_surface = font.render(f'{score}', False, 'white')
    screen.blit(score_surface,(10,75))

def set_speed(score):
    speed = 60
    if score > 9000:
        speed = 1
    elif score > 8000:
        speed = 2
    elif score > 7000:
        speed = 3
    elif score > 6000:
        speed = 4
    elif score > 4300:
        speed = 5
    elif score > 3300:
        speed = 6
    elif score > 2500:
        speed = 7
    elif score > 1900:
        speed = 9
    elif score > 1300:
        speed = 11
    elif score > 1000:
        speed = 13
    elif score > 700:
        speed = 16
    elif score > 500:
        speed = 20
    elif score > 400:
        speed = 24
    elif score > 275:
        speed = 29
    elif score > 175:
        speed = 35
    elif score > 100:
        speed = 42
    elif score > 50:
        speed = 50
    return speed

def blit_grid():
    x_grid_line = pygame.Surface((1,510))
    x_grid_line.fill("black")
    y_grid_line = pygame.Surface((300,1))
    y_grid_line.fill("black")

    ### column grid lines
    for x in range(130,400,30):
        screen.blit(x_grid_line,(x,50)) 
    ### row grid lines
    for y in range(80,560,30):
        screen.blit(y_grid_line,(100,y))

def display_peice(peice_data):
    coordinates, color = peice_data[0], peice_data[1]
    block = pygame.Surface((30,30))
    block.fill(color)
    for x,y in coordinates:
        x = (x * 30) + 100
        y = (y * 30) - 70
        screen.blit(block,(x,y))

def blit_peices(peice_map):
    block = pygame.Surface((30,30))
    for y in range(17):
        for x in range(10):
            color = peice_map[y][x]
            if color == 0:
                block.fill("black")
            else:
                block.fill(color)
            c = (x * 30) + 100
            r = ((y+4) * 30) - 70
            screen.blit(block,(c,r))

def blit_onhold(onhold_peice):
    onhold_data = extra.peice_info(onhold_peice)
    coordinates, color = onhold_data[0], onhold_data[1]
    block = pygame.Surface((13,13))
    block.fill(color)
    for x,y in coordinates:
        if color == "green" or color == 'red' or color == "yellow" or color == "purple":
            y = (y * 13) + 169
        else:
            y = (y * 13) + 155
        x = (x * 13) - 18
        screen.blit(block,(x,y))

def cover_peice(peice_data):
    coordinates = peice_data[0]
    cover_block = pygame.Surface((30,30))
    for x, y in coordinates:
        x = (x * 30) + 100
        y = (y * 30) - 70
        screen.blit(cover_block,(x,y))  
    
def control():
    #initialize all starting variables (calling this function at any point should reset game) 
    x = 0
    speed = 60
    score = 0
    peice_map = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]
    onhold_peice = random.randint(0,6)
    current_peice = random.randint(0,6)
    peice_data = extra.peice_info(current_peice)

    blit_peices(peice_map)
    blit_onhold(onhold_peice)

    freeze = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and not freeze:
                cover_peice(peice_data)
                if event.key == pygame.K_RIGHT:
                    peice_data = extra.move_peice(peice_data, 1, 0, peice_map)

                if event.key == pygame.K_LEFT:
                    peice_data = extra.move_peice(peice_data, -1, 0, peice_map)

                if event.key == pygame.K_DOWN:
                    peice_data = extra.move_peice(peice_data, 0, 1, peice_map)
                    if peice_data[2] == 'S':
                        freeze = True

                if event.key == pygame.K_UP:
                    peice_data = extra.rotate_peice(peice_data, 0, 0, peice_map)

                if event.key == pygame.K_SPACE:
                    peice_data = extra.tela_peice(peice_data, peice_map)
                    if peice_data[2] == 'S':
                        freeze = True
        
        if freeze == True:
            score += 4 + (30 // speed)###

            extra.set_peice(peice_data,peice_map)
            points = extra.clear_row(peice_map)
            score += points + (100 // speed)###

            blit_peices(peice_map)
            blit_grid()

            if extra.player_dead(peice_data):#might need to be before blit peices
                break

            current_peice = onhold_peice
            onhold_peice = random.randint(0,6)

            peice_data = extra.peice_info(current_peice)

            speed = set_speed(score)
            x = 0
            freeze = False

        clock.tick(60)
        x += 1
        if x == speed:
            x = 0
            cover_peice(peice_data)
            peice_data = extra.move_peice(peice_data, 0, 1, peice_map)
            if peice_data[2] == 'S':
                freeze = True
        display_peice(peice_data)
        blit_grid()
        display_background()
        blit_score(score)
        blit_onhold(onhold_peice)
        pygame.display.update()
    display_background()
    blit_score(score)
    blit_onhold(onhold_peice)
    dead_restart()

def dead_restart():
    back = pygame.Surface((54,54))
    back.fill('white')
    block  = pygame.Surface((6,6))
    
    #restart symbol
    def blit_restart():
        screen.blit(back,(210,270))

        screen.blit(block,(213,273))
        screen.blit(block,(225,273))
        screen.blit(block,(231,273))
        screen.blit(block,(237,273))
        screen.blit(block,(243,273))

        screen.blit(block,(213,279))
        screen.blit(block,(219,279))
        screen.blit(block,(249,279))

        screen.blit(block,(213,285))
        screen.blit(block,(219,285))
        screen.blit(block,(225,285))
        screen.blit(block,(255,285))

        screen.blit(block,(255,291))
        screen.blit(block,(255,297))
        screen.blit(block,(255,303))
        
        screen.blit(block,(249,309))
        screen.blit(block,(219,309))

        screen.blit(block,(225,315))
        screen.blit(block,(231,315))
        screen.blit(block,(237,315))
        screen.blit(block,(243,315))
    
    blit_restart()
    pygame.display.update()
    restart = False
    while restart == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                back.fill("firebrick2")
                block.fill("cornsilk3")
                blit_restart()
                pygame.display.update()
                time.sleep(0.25)
                back.fill("white")
                block.fill("black")
                blit_restart()
                pygame.display.update()
                time.sleep(1)
                back.fill("black")
                blit_restart()
                pygame.display.update()
                restart = True
    control()

def start():
    #displays start button
    back = pygame.Surface((90,40))
    arrow = pygame.Surface((8,8))
    back.fill("white")

    #reusable function for colorless arrow in start button
    def blit_arrow():
        #back
        screen.blit(back,(155,250))

        #l1
        screen.blit(arrow,(185,253))
        screen.blit(arrow,(185,261))
        screen.blit(arrow,(185,269))
        screen.blit(arrow,(185,277))
        #l2
        screen.blit(arrow,(191,257))
        screen.blit(arrow,(191,265))
        screen.blit(arrow,(191,273))
        #l3
        screen.blit(arrow,(196,261))
        screen.blit(arrow,(196,269))
        #l4
        screen.blit(arrow,(200,265))
    blit_arrow()

    pygame.display.update()

    #checks for space; initiates button push "animation", then calls to game control loop
    start = False
    while start == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start = True
                back.fill("chartreuse2")
                arrow.fill("cornsilk3")
                blit_arrow()
                pygame.display.update()
                time.sleep(0.25)
                back.fill("white")
                arrow.fill("black")
                blit_arrow()
                pygame.display.update()
                time.sleep(1)

                back.fill("black")
                blit_arrow()
                pygame.display.update()
    control()

start()
