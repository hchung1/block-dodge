from car_colors import *
from car_message import *
from block_fall_setting import *
from car_objects import *
from pause_menu import paused
from car_crash import *
import pygame
import time
import random

pygame.init()

pygame.display.set_caption('RUNRUNRUNRUN')

def game_loop():
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
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    X_change = 0
                    push = 0

        GameImage.fill(oppisite_range[i])

        attacker(fall_startx, fall_starty, falling_spans, falling_bulk, color_range[i])
        fall_starty += thing_speed
        
        #crash scene with the wall
        if x > game_screen_x - player_size or x < 0:
            choice = knockedout(color_range[i])
            if choice == 1:
                game_loop()
        #crash scene with the objects
        if y < fall_starty + falling_bulk:
            if x > fall_startx and x < fall_startx + falling_spans or x + player_size > fall_startx and x + player_size < fall_startx + falling_spans:
                choice = crash(color_range[i])
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
            dodged += 1
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
