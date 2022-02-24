from random import randint
import pyray
import random

from game.character.character import Character
from game.states.color import Color
from game.character.position import Position
from game.character.cast import Cast

COLS = 60
ROWS = 40
CELL_SIZE = 15
FONT_SIZE = 15


class FallingGems:
    """This will generates the falling down of the rocks and the gems """

    def __init__(self, video_service):

        self._video_service = video_service
        self._gem_position = Position()

    def create_gems(self, x, y):

        cast = Cast()

        # creates a gem

        text = "*"
        x_gem = x
        y_gem = y
        position = Position(x_gem, y_gem)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        character = Character()
        character.set_text(text)
        character.set_font_size(FONT_SIZE)
        character.set_color(color)
        character.set_position(position)
        cast.add_actor("character", character)

        # draw character
        self._video_service.draw_character(character)

    def move_gem(self, ):
        # changes the position of gem to 1 size of gem
        x = random.randint(1, COLS-1)
        y = 0
        add(self, )
