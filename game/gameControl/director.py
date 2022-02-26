from game.states.collision import Collision
from game.services.keyboard import Keyboard
from game.states.physics import Physics
from game.character.actor import Actor
import random

class Director:
    """ 
        All the parts of the game are managed in this file
        Attributes: 
            _characters (Character)
            _display (Display)
            _specifications (Dictionary)
            _score (Int)
            _player (Actor)
            _banner (Actor)
        author: Samuel Beltran
    """
    def __init__(self,characters,display,specificaions):
        
        self._characters = characters
        self._display = display
        self._specifications = specificaions
        self._score = 0
        self._player = self._characters.get_character("player")[0]
        self._banner = self._characters.get_character("score")[0]


    def start_game(self):
        """ Starts the game """

        counterRock = 0
        counterGem = 0
        gemPerFrame = self._specifications["a_gem_pf"]
        rockPerFrame = self._specifications["a_rock_pf"]
        cols = self._specifications["cols"]
        cell = self._specifications["cell_size"]
        fontsize = self._specifications["font_size"]
        scale = self._specifications["scale"]
    
        self._display.open_window()
        
        """ This loop runs the game """
        while self._display.is_playing():

            x = (random.randint(0,cols)*cell)-cell

            """ For a certain number of frames a gem is created """
            if counterGem == gemPerFrame:
                gem = Actor("*","gem",x+(cell*5),cell,fontsize,scale)
                self._characters.add_new_character(gem.get_group_name(),gem)    
                counterGem = 0            

            """ For a certain number of frames a rock is created """
            if counterRock == rockPerFrame:
                rock = Actor("0","rock",x,cell,fontsize,scale)
                self._characters.add_new_character(rock.get_group_name(),rock)
                counterRock = 0
            
            """ The __input_player and __update methods are called """
            self._display.start_drawing()
            self.__input_player()
            self.__update()

            counterGem += 1
            counterRock += 1

            self._display.stop_drawing()

        self._display.close_window()
    
    def __input_player(self):
        """ Receives players input and calls the methods """
        keyboard = Keyboard()
        if self._score < 0:
            if keyboard.get_key_board():
                print("self._score: ",self._score)
                self._score = 0
        else:
            x = self._player.get_x_position()
            if keyboard.get_direction() != 0:
                self._player.set_x_position(x + self._player.scale_x_position(keyboard.get_direction()))    
        

    def __update(self):
        """ Renders all the characters of the game """
        if self._score < 0:
            self._banner.set_appearance("GAME OVER ! you want to try again ? press : a")

        else:
            collision = Collision(self._characters,self._score,self._specifications["points"])
            collision.check_collision()
            self._score = collision.get_score()
            self._banner.set_appearance("Score: "+ str(self._score))

            """ The physics and the actions of the characters are rendered here """

            physics = Physics(self._characters,self._display,self._specifications["scale"],self._specifications["gravity"])
            physics.move_gem()
            physics.move_rock()
            self._display.draw_character(self._player)
        self._display.draw_character(self._banner)
               