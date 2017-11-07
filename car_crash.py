from default_game import *
from car_message import message_setting
from game_over import defeated
#Prints the message
def message_display (text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = message_setting(text, largeText, color)
    TextRect.center = ((game_screen_x/2), (game_screen_y/2))
    GameImage.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)
    
#Place the string on the define function above
def crash(color):
    message_display('You Crashed.', color)
    time.sleep(1)
    x = defeated()
    return x
#Wall collision
def knockedout(color):
    message_display('Knocked Out By Wall.', color)
    time.sleep(1)
    x = defeated()
    return x

#count the score
def counter(count, color):
    #set text size
    font = pygame.font.SysFont('freesansbold.ttf', 25)
    #set text color and import the counter
    text = font.render(str(count), True, color)
    #Places the text in the top center of the screen
    GameImage.blit(text,(game_screen_x/2,0))
