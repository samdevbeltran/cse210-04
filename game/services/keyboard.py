import pyray
from game.character.position import Position

class Keyboard:
    """ 
    the keyboard class will get the players input and calculate the new position of the players character 
        Attribute:
            _size (int): size of a cell
    Author:Yami
    """

    def __init__(self, cell_size = 2):
        """Constructs a new KeyboardService using the specified cell size.
        """
        self._size = cell_size


    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

            return: int
        """

        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        return dx

    def get_key_board(self):
        """ It checks the key that was pressed
        
            return: boolean
        """
        return pyray.is_key_down(pyray.KEY_A)

