from car_colors import black, white
from car_message import *
from block_fall_setting import *
from librarian import reader
import pygame


def question():
    GameImage.fill(black)
    #Text for pause and go
    largeText = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = message_setting("Ingame", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*2))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("Movement : A - Left, D - Right", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*4))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("Other : M - Menu, P - Pause Esc - Quit", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*5))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("Dodge the falling blocks.", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*6))
    GameImage.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("P - Exit 'How to Play'", largeText, white)
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
def highscores():
    GameImage.fill(black)
    #Text for pause and go
    largeText = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = message_setting("High Score", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*4))
    GameImage.blit(TextSurf, TextRect)
    
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting(reader(), largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*6))
    GameImage.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("P - Return", largeText, white)
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
'''
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
'''
