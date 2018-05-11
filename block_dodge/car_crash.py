from block_fall_setting import *
from car_objects import message_setting
from block_fall_setting import black, white
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
#Prints the message
def message_display (text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = message_setting(text, largeText, color)
    TextRect.center = ((game_screen_x/2), (game_screen_y/2))
    GameImage.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    
#Place the string on the define function above
def crash(color, score):
    message_display('You Crashed.', color)
    time.sleep(1)
    x = defeated(score)
    return x

#count the score
def counter(count, color):
    #set text size
    font = pygame.font.SysFont('freesansbold.ttf', 25)
    #set text color and import the counter
    text = font.render(str(count), True, color)
    #Places the text in the top center of the screen
    GameImage.blit(text,(game_screen_x/2,0))
