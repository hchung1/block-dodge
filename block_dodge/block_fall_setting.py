import pygame, time

game_screen_x = 800#Game Screen width
game_screen_y = 600#Game Screen Height

#Game screen size
GameImage = pygame.display.set_mode((game_screen_x,game_screen_y))
#Basic Clock
clock = pygame.time.Clock()
#Colors and labeleb by name
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 170, 0)
blue = (0, 0, 255)
green = (11, 195, 108)
bright_red = (105, 0, 0)
bright_green = (11, 100, 108)

#List of colors
color_range = [white, black, orange, blue, green, red]
oppisite_range = [black, white, blue, orange, red, green]
