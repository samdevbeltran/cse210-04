from  game.states.collision import Collision
from  game.services.keyboard import Keyboard
from  game.states.physics import Physics
from game.character.actor import Actor
import random


class Director:
    """ 
        All the parts of the game are managed in this file
        Attributes: 
            _characters (Character)
            _display (Display)
        author: Samuel Beltran
    """
    def __init__(self,characters,display,specificaions):
        
        self._characters = characters
        self._display = display
        self._specifications = specificaions
    
    def start_game(self):
        
        cols = self._specifications["cols"]
        cell = self._specifications["cell_size"]
        fontsize = self._specifications["font_size"]
        scale = self._specifications["scale"]

        self._display.open_window()
        player = self._characters.get_character("player")[0]
        
        while self._display.is_playing():

            rock = Actor("0","rock",random.randint(1,cols * (cell+scale)),0,fontsize,scale)
            gem = Actor("*","gem",random.randint(1,cols * (cell+scale)),0,fontsize,scale)
        
            self._characters.add_new_character(rock.get_group_name(),rock)
            self._characters.add_new_character(gem.get_group_name(),gem)    
            
            self._display.start_drawing()
            self.__input_player(player)
            self.__update()
            # self.__result()
            self._display.stop_drawing()
        self._display.close_window()

    def get_characters(self):
        return self._characters

    def get_display(self):
        return self._display
    
    def __input_player(self,player):

        keyboard = Keyboard().get_direction()
        x = player.get_x_position()
        
        if keyboard != 0:
            player.set_x_position(x + player.scale_x_position(keyboard))    

    def __update(self):
        player = self._characters.get_character("player")
        #collision = Collision(self._characters,self._score).check_collision()
        # self._score = collision.get_score()
        physics = Physics(self._characters,self._display,self._specifications["scale"],self._specifications["gravity"])
        self._display.draw_character(player[0])
        
        physics.move_gem()
        physics.move_rock()
        
        
        

    def __result(self):
        print("here the result will be display")