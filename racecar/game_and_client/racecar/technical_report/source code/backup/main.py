from car_colors import black, white
from car_message import *
from block_fall_setting import *
from help import *
from librarian import highscores
import pygame

pygame.init()

pygame.display.set_caption('RUNRUNRUNRUN')

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
                    key = "m"
                    return key
                if event.key == pygame.K_h:
                    question()
                    restart()
                if event.key == pygame.K_g:
                    highscores()
                    restart()

        pygame.display.update()
        clock.tick(15)
