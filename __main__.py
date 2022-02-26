from game.gameControl.director import Director
from game.services.display import Display
from game.character.characterStorage import CharacterStorage
from game.character.actor import Actor
import random

X_WIDTH = 900
Y_HEIGHT = 600
GAME_NAME = "Greed"
FRAME_NUMBER = 12
GAME_POINTS = 10
WHITE_COLOR = (255,255,255,255)
CELL_SIZE = 25
SCALE = 25
FONT_SIZE = 25
COLS = 36
ROWS = 24
GRAVITY = 10
A_GEM_PER_FRAME = 15
A_ROCK_PER_FRAME = 10

def main():
    """ This is the starting point. 
        The characters and the video display specifications are set and the game is started
        author: Samuel Beltran
    """

    specifications = {
                        "x_with":X_WIDTH,
                        "y_height":Y_HEIGHT,
                        "game_name":GAME_NAME,
                        "frame_number":FRAME_NUMBER,
                        "points": GAME_POINTS,
                        "white_color":WHITE_COLOR,
                        "cell_size":CELL_SIZE,
                        "scale": SCALE,
                        "font_size":FONT_SIZE,
                        "cols":COLS,
                        "rows":ROWS,
                        "gravity":GRAVITY,
                        "a_gem_pf": A_GEM_PER_FRAME,
                        "a_rock_pf": A_ROCK_PER_FRAME
                        }

    x = (random.randint(0,COLS)*CELL_SIZE)-CELL_SIZE
    characterStorage = CharacterStorage()    
    gem = Actor("*","gem",x,CELL_SIZE*2,FONT_SIZE,SCALE)
    rock = Actor("0","rock",x,CELL_SIZE,FONT_SIZE,SCALE)
    player = Actor("#","player",int(X_WIDTH / 2),(Y_HEIGHT - CELL_SIZE),FONT_SIZE,SCALE,WHITE_COLOR)
    score = Actor("Score: ","score",CELL_SIZE,0,FONT_SIZE,SCALE,WHITE_COLOR)
    
    characterStorage.add_new_character(player.get_group_name(),player)
    characterStorage.add_new_character(gem.get_group_name(),gem)
    characterStorage.add_new_character(rock.get_group_name(),rock)
    characterStorage.add_new_character(score.get_group_name(),score)

    display = Display(X_WIDTH,Y_HEIGHT,GAME_NAME,FRAME_NUMBER,CELL_SIZE)
    director = Director(characterStorage,display,specifications)
    director.start_game()

main()