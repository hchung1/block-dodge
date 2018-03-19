from main import game_main
from graphic_main import game_loop


def center(start):
    while True:
        if start == "o":
            start = game_main()
        if start == "m":
            start = game_loop()
center("o")
