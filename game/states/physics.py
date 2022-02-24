from random import randint
import random

from game.character.character import Character
from game.states.color import Color
from game.character.position import Position
from game.character.characterStorage import CharacterStorage

COLS = 60
ROWS = 40
CELL_SIZE = 15
FONT_SIZE = 15


class Physics:
    """This will generates the falling down of the rocks and the gems """

    def __init__(self, video_service):

        self._video_service = video_service
        self._gem_position = Position()
        self._rock_position = Position()

    def gem_position(self, x, y):

        # creates a gem

        x_gem = x
        y_gem = y
        position = Position(x_gem, y_gem)
        position = position.scale(CELL_SIZE)

    def move_gem(self):
        chStorage = CharacterStorage()

        # changes the position of gem to 1 size of gem
        text = "*"
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        character = Character()
        character.set_text(text)
        character.set_font_size(FONT_SIZE)
        character.set_color(color)
        cast.add_character("character", character)

        x = random.randint(1, COLS-1)
        y = 0

        for _ in range(1, ROWS):
            self._video_service.clear_buffer()
            x = x
            y = y + FONT_SIZE
            self.gem_position(self, x, y)
            # draw character
            self._video_service.draw_character(character)

    def rock_position(self, x, y):

        # creates a gem

        x_rock = x
        y_rock = y
        position = Position(x_rock, y_rock)
        position = position.scale(CELL_SIZE)

    def move_rock(self):
        cast = Cast()

        # changes the position of gem to 1 size of gem
        text = "O"
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        character = Character()
        character.set_text(text)
        character.set_font_size(FONT_SIZE)
        character.set_color(color)
        cast.add_character("character", character)

        x = random.randint(1, COLS-1)
        y = 0

        for _ in range(1, ROWS):
            self._video_service.clear_buffer()
            x = x
            y = y + FONT_SIZE
            self.rock_position(self, x, y)
            # draw character
            self._video_service.draw_character(character)
