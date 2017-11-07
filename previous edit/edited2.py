import pygame
import time
import random

pygame.init()

#Required
game_screen_x = 800
game_screen_y = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 170, 0)
blue = (0, 0, 255)
green = (11, 195, 108)



GameImage = pygame.display.set_mode((game_screen_x,game_screen_y))
pygame.display.set_caption('RUNRUNRUNRUN')
clock = pygame.time.Clock()


#count the score
def counter(count, color):
    #set text size
    font = pygame.font.SysFont('freesansbold.ttf', 25)
    #set text color and import the counter
    text = font.render(str(count), True, color)
    #Places the text in the top center of the screen
    GameImage.blit(text,(game_screen_x/2,0))

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


def message_setting(text, font, color):
    #Descripe the text
    textSurface = font.render(text, True, color)
    #Give to define function below and textSurface.get_rect() is define in pygame library
    return textSurface, textSurface.get_rect()
#Set up a mold for a text to be imported and paste in the middle of the screen
def message_display (text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = message_setting(text, largeText, color)
    TextRect.center = ((game_screen_x/2), (game_screen_y/2))
    GameImage.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
#Place the string on the define function above
def crash(color):
    message_display('You Got Smacked', color)
#Wall collision
def knockedout(color):
    message_display('Knocked Out By Wall', color)

def game_loop():
    x = (game_screen_x * 0.45)
    y = (game_screen_y * 0.82)
    player_size = 100
    X_change = 0
    i = 1
    #Range of Colors
    color_range = [white, black, orange, blue, green, red]
    oppisite_range = [black, white, blue, orange, red, green]

    thing_speed = 4
    falling_spans = 100
    falling_bulk = 100
    fall_starty = random.randrange(-600, -200)
    fall_startx = random.randrange(0, game_screen_x-falling_spans)
    
    dodged = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X_change = -10
                elif event.key == pygame.K_RIGHT:
                    X_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    X_change = 0

        x += X_change

        GameImage.fill(oppisite_range[i])

        counter(dodged, color_range[i])
        attacker(fall_startx, fall_starty, falling_spans, falling_bulk, color_range[i])
        fall_starty += thing_speed
        player (x,y)
        
        #crash scene with the wall
        if x > game_screen_x - player_size or x < 0:
            knockedout(color_range[i])
        #crash scene with the objects
        if y < fall_starty + falling_bulk:
            if x > fall_startx and x < fall_startx + falling_spans or x + player_size > fall_startx and x + player_size < fall_startx + falling_spans:
                crash(color_range[i])
                
        #increment height
        if fall_starty > game_screen_y:
            fall_starty = 0 - falling_bulk
            fall_startx = random.randrange(0, game_screen_x - falling_spans)
            #Add to counter
            dodged += 1
            #Color Changer
            i = random.randint(0,5)
            thing_speed += 0.2
            falling_spans = random.randrange(100,400)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
