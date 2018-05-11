from car_colors import black, white
from car_message import *
from block_fall_setting import *
import pygame, os

def scorer(score):
    location = os.getcwd()
    location = location.split('/')
    path = ("/{}/{}/.jokes".format(location[1],location[2]))
    os.chdir(path)
    f = open("scores.txt", "r")
    score_list = (f.read()).split(" ")
    score_list[-1] = score_list[-1].strip()
    f.close()
    score_list.append(score)
    score_list = sorted(score_list, key=int, reverse=True)
    del score_list[-1]
    result = ' '.join(str(x) for x in score_list)
    f = open("scores.txt", "w+")
    f.write(result)
    f.close()

def reader():
    location = os.getcwd()
    location = location.split('/')
    path = ("/{}/{}/.jokes".format(location[1],location[2]))
    os.chdir(path)
    f = open("scores.txt", "r")
    score_list = (f.read()).split(" ")
    score_list[-1] = score_list[-1].strip()
    f.close()
    score_list = ', '.join(str(x) for x in score_list)
    return score_list

def highscores():
    GameImage.fill(black)
    #Text for pause and go
    largeText = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = message_setting("High Score", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*3))
    GameImage.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting(reader(), largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*5))
    GameImage.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("P - Go Back", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*7))
    GameImage.blit(TextSurf, TextRect)

    x = True

    while x is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    x = False

        pygame.display.update()
        clock.tick(15)
