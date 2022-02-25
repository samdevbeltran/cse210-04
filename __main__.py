""" This is the starting point. 
    The characters and the video display specifications are set and the game is started
    author: Samuel Beltran
"""
#from tkinter.tix import ROW
from game.gameControl.director import Director
from game.services.display import Display
from game.character.characterStorage import CharacterStorage
from game.character.actor import Actor
import random

X_WIDTH = 900
Y_HEIGHT = 600
GAME_NAME = "Greed"
FRAME_NUMBER = 12
GAME_SCORE = 0  
GAME_POINTS = 10
WHITE_COLOR = (255,255,255,255)
CELL_SIZE = 25
SCALE = 35
FONT_SIZE = 25
COLS = 36
ROWS = 24
GRAVITY = 30

def main():
    specifications = {
                        "x_with":X_WIDTH,
                        "y_height":Y_HEIGHT,
                        "game_name":GAME_NAME,
                        "frame_number":FRAME_NUMBER,
                        "game_score": GAME_SCORE,
                        "game_points": GAME_POINTS,
                        "white_color":WHITE_COLOR,
                        "cell_size":CELL_SIZE,
                        "scale": SCALE,
                        "font_size":FONT_SIZE,
                        "cols":COLS,
                        "rows":ROWS,
                        "gravity":GRAVITY
                        }
    characterStorage = CharacterStorage()    
    player = Actor("#","player",int(X_WIDTH / 2),(Y_HEIGHT - CELL_SIZE),FONT_SIZE,SCALE,WHITE_COLOR)
    characterStorage.add_new_character(player.get_group_name(),player)
    display = Display(X_WIDTH,Y_HEIGHT,GAME_NAME,FRAME_NUMBER)
    director = Director(characterStorage,display,specifications)
    director.start_game()

main()