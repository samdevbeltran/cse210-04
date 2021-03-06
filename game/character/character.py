from game.states.color import Color
from game.character.position import Position
import random

class Character(Position):
    """ 
    this will create a character,it could be either a gem or a rock 
    Attributes:
       
        _appearance (str) : how the character will look like
        _position (Position): the position of the character
        _font_size (int) : the size of the character
        _color (rgb) : the color of the character
    Author:Yami
    """

    
    def __init__(self,appearance,x,y,fontSize,scale,color=""):
        self._appearance = appearance
        self._position = Position.__init__(self,x,y,scale)
        self._font_size = fontSize
        self._color = color
        if color == "":
            self._color = self.__set_character_color()
    
    def get_appearance(self):
        """ Gets the look of character
            return: str
        """
        return self._appearance

    def set_appearance(self,appearance):
        """ Sets the look of character """
        self._appearance = appearance

    def get_color(self):
        """ Get the color of the character
            return: rgb
        """
        return self._color

    def get_font_size(self):
        """ Gets the font size
            return:int
        """
        return self._font_size
    
    def __set_character_color(self):
        """ sets the color """
        return Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)).to_tuple()
