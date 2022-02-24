from turtle import color
from typing_extensions import Self
from game.states import color

import random

class Character:
    """ 
    this will create a character,it could be either a gem or a rock 
    Attributes:
       
        _gems("") : the appearence of the gems
        _rocks("" : the appearence of the rocks
     
    Author:Yami
    """

    
    def __init__(self):
        self._gems = ""
        self._rocks = ""

        banner = color
        banner.set_gems_color(color)
        banner.set_rocks_color(color)
    
def create_gems(self):
    self._gems = "*"
    self._gems.set_gems_color(color)
    return self.gems


def create_rocks(self):
    self._rocks = "O"
    self._rocks.set_rocks_color(color)
    return self._rocks