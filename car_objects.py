from default_game import *
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
