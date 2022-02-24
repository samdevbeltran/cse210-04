#from turtle import color
#from typing_extensions import Self
from game.states.color import Color
from game.character.position import Position
import random

class Character(Position):
    """ 
    this will create a character,it could be either a gem or a rock 
    Attributes:
       
        _gems("") : the appearance of the gems
        _rocks("" : the appearance of the rocks
     
    Author:Yami
    """

    
    def __init__(self,appearance,x,y,fontSize,color=""):
        # self._gems = ""
        # self._rocks = ""
        self._appearance = appearance
        self._position = Position.__init__(self,x,y)
        self._font_size = fontSize
        self._color = color
        if color == "":
            self._color = self.__set_character_color()
        #banner = Color()
        #banner.set_gems_color(color)
        #banner.set_rocks_color(color)
    
    def get_appearance(self):
         return self._appearance

    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._font_size
    # def create_gems(self):
    #     self._gems = "*"
    #     #self._gems.set_gems_color(color)
    #     return self.gems


    # def create_rocks(self):
    #     self._rocks = "O"
    #     #self._rocks.set_rocks_color(color)
    #     return self._rocks
    
    def __set_character_color(self):
        return Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)).to_tuple()

    def test(self):
        return print("this is a try")