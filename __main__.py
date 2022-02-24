""" This is the starting point. 
    The characters and the video display specifications are set and the game is started
    author: Samuel Beltran
"""
from game.gameControl.director import Director
from game.services.display import Display
from game.character.characterStorage import CharacterStorage
from game.character.actor import Actor

X_WIDTH = 900
Y_HEIGHT = 600
GAME_NAME = "Greed"
FRAME_NUMBER = 12
GAME_SCORE = 0  
GAME_POINTS = 10
WHITE_COLOR = (255,255,255,255)
CELL_SIZE = 15
SCALE = 15

def main():
    gem = Actor("*","gem",12,13,12,SCALE)
    rock = Actor("0","rock",12,13,12,SCALE)
    player = Actor("#","player",int(X_WIDTH / 2),(Y_HEIGHT - CELL_SIZE),12,SCALE,WHITE_COLOR)
    
    # print("gem: ",gem.get_group_name())
    # print("rock: ",rock.get_group_name())
    # print("player: ",player.get_group_name())

    characterStorage = CharacterStorage()
    characterStorage.add_new_character(player.get_group_name(),player)
    characterStorage.add_new_character(rock.get_group_name(),rock)
    characterStorage.add_new_character(gem.get_group_name(),gem)
    
    ##print( characterStorage.get_all_characters())

    display = Display(X_WIDTH,Y_HEIGHT,GAME_NAME,FRAME_NUMBER)
    director = Director(characterStorage,display,GAME_SCORE,GAME_POINTS)
    director.start_game()

main()