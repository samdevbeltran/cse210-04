""" This is the starting point. 
    The characters and the video display specifications are set and the game is started
    author: Samuel Beltran
"""
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
SCALE = 25
FONT_SIZE = 25
COLS = 36
ROWS = 24
GRAVITY = 20

def main():

    characterStorage = CharacterStorage()    
    player = Actor("#","player",int(X_WIDTH / 2),(Y_HEIGHT - CELL_SIZE),FONT_SIZE,SCALE,WHITE_COLOR)
    
    # print("gem: ",gem.get_group_name())
    # print("rock: ",rock.get_group_name())
    # print("player: ",player.get_group_name())
    for i in range(COLS):
        rock = Actor("0","rock",random.randint(1,COLS * CELL_SIZE),random.randint(1,(CELL_SIZE * 5)),FONT_SIZE,SCALE)
        gem = Actor("*","gem",random.randint(1,COLS * CELL_SIZE),random.randint(1,(CELL_SIZE * 5)),FONT_SIZE,SCALE)
        characterStorage.add_new_character(rock.get_group_name(),rock)
        characterStorage.add_new_character(gem.get_group_name(),gem)    

    characterStorage.add_new_character(player.get_group_name(),player)
    
    display = Display(X_WIDTH,Y_HEIGHT,GAME_NAME,FRAME_NUMBER)
    director = Director(characterStorage,display,GAME_SCORE,GAME_POINTS,SCALE,GRAVITY)
    director.start_game()

main()