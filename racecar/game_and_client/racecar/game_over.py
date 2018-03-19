from car_colors import black, white
from car_message import message_setting
from block_fall_setting import *
from librarian import scorer
import pygame
def defeated(score):
    GameImage.fill(black)
    #Text for pause and go
    largeText = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = message_setting("Game Over", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*3))
    GameImage.blit(TextSurf, TextRect)
    
    scorer(score)
    
    score = "Your Score: " + str(score)
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting(score, largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*5))
    GameImage.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("Esc - Quit, P - Start Over", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*6))
    GameImage.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("M - Main Menu on Game Screen", largeText, white)
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
                    x = 1
                    return x

        pygame.display.update()
        clock.tick(15)
