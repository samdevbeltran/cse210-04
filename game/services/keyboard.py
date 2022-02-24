import pyray
from game.character.position import Position

class Keyboard:
    """ 
    the keyboard class will get the players input and calculate the new position of the players character 
    cell_size (int): For scaling directional input to a grid.
    Author:Yami
    """

    def __init__(self, cell_size = 2):
        """Constructs a new KeyboardService using the specified cell size.
        """
        self._size = cell_size


    def get_direction(self):
            """Gets the selected direction based on the currently pressed keys."""

            dx = 0
            dy = 0

            if pyray.is_key_down(pyray.KEY_LEFT):
                dx = -1
            
            if pyray.is_key_down(pyray.KEY_RIGHT):
                dx = 1
            
            if pyray.is_key_down(pyray.KEY_UP):
                dy = -1
            
            if pyray.is_key_down(pyray.KEY_DOWN):
                dy = 1

            direction = Position(dx, dy)
            direction = direction.scale(self._size)
            
            return direction

