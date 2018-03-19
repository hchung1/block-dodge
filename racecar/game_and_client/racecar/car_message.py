##Basic message setting
def message_setting(text, font, color):
    #Descripe the text
    textSurface = font.render(text, True, color)
    #Give to define function below and textSurface.get_rect() is define in pygame library
    return textSurface, textSurface.get_rect()


