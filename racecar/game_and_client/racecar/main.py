from car_colors import *
from car_message import *
from block_fall_setting import *
from car_objects import *
from pause_menu import paused
from car_crash import *
from help import *
from librarian import check_files_start
import pygame, time, random

pygame.init()

pygame.display.set_caption('RUNRUNRUNRUN')

def game_loop():
    x = (400)#
    y = (game_screen_y * 0.82)
    player_size = 100
    X_change = 0
    i = 1
    pos = 0
    push = 0
    thing_speed = 4
    falling_spans = 100
    falling_bulk = 100
    fall_starty = random.randrange(-600, -200, 100)
    fall_startx = random.randrange(0, game_screen_x-falling_spans, 100)

    dodged = 0
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if pos > -4:
                        X_change = -100
                        pos -= 1
                        push = 1
                if event.key == pygame.K_d:
                    if pos < 3:
                        X_change = 100
                        pos += 1
                        push = 1
                if event.key == pygame.K_m:
                    center("o")
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    X_change = 0
                    push = 0
        if push == 1:
            x += X_change
            push = 2
        GameImage.fill(oppisite_range[i])

        counter(dodged, color_range[i])
        attacker(fall_startx, fall_starty, falling_spans, falling_bulk, color_range[i])
        fall_starty += thing_speed
        player(x,y)
        
        #crash scene with the objects
        if y < fall_starty + falling_bulk:
            if x > fall_startx and x < fall_startx + falling_spans or x + player_size > fall_startx and x + player_size < fall_startx + falling_spans:
                choice = crash(color_range[i], dodged)
                if choice == 1:
                    game_loop()
        #increment height
        if fall_starty > game_screen_y:
            fall_starty = 0 - falling_bulk
            fall_startx = random.randrange(0, game_screen_x - falling_spans, 100)
            #Add to counter
            dodged += 1
            #Color Changer
            if dodged % 5 == 0:
                i = random.randint(0,5)
            thing_speed += 0.5
            falling_spans = random.randrange(100,200)

        pygame.display.update()
        clock.tick(60)

def restart():
    game_main()

def game_main():

    GameImage.fill(black)
    #Text for pause and go
    largeText = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = message_setting("Welcome to Block Dodge", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*2))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("P - Play", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*4))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("H - How to Play", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*5))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("G - High Score", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*6))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("Esc - Quit", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*7))
    GameImage.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    center("m")
                if event.key == pygame.K_h:
                    question()
                    restart()
                if event.key == pygame.K_g:
                    highscores()
                    restart()

        pygame.display.update()
        clock.tick(15)

def center(start):
    while True:
        if start == "u":
            check_files_start()
            start = "o"
        if start == "o":
            game_main()
        if start == "m":
            game_loop()
