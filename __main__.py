""" This is the starting point. 
    The characters and the video display specifications are set and the game is started
    author: Samuel Beltran
"""
from game.gameControl.director import Director
from game.services.display import Display

X_WIDTH = 700
Y_HEIGHT = 600
GAME_NAME = "Greed"
FRAME_NUMBER = 12
GAME_SCORE = 0  
GAME_POINTS = 10
def main():
    display = Display(X_WIDTH,Y_HEIGHT,GAME_NAME,FRAME_NUMBER,GAME_POINTS)
    director = Director("samuel",display,GAME_SCORE)
    director.start_game()

main()