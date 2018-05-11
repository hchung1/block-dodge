from block_fall_setting import *
import pygame

#The falling Objects
def attacker(posx, posy, attackerx, attackery, color):
    #Sent the boulders
    pygame.draw.rect(GameImage, color, [posx, posy, attackerx, attackery])

#The character you're moving
def player(x,y):
    #Find the image
    player_image = pygame.image.load('mainblock.png')
    #Display the image
    GameImage.blit(player_image,(x,y))
##Basic message setting
def message_setting(text, font, color):
    #Descripe the text
    textSurface = font.render(text, True, color)
    #Give to define function below and textSurface.get_rect() is define in pygame library
    return textSurface, textSurface.get_rect()


