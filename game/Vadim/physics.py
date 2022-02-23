from random import randint


import random

COLS = 60
ROWS = 40
CELL_SIZE = 15


class Physics:
    """
    This will generates the falling down of the rocks and the gems 
    Attributes:
        _characters (dict): a dictionary with the characters
        _gravity (int) : the gravity for the characters
    Author:Vadim
    """

    def __init__(self, x, y):
        """Constructs a new point using the specified x and y values.

        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Physics): The point to add.

        Returns:
            Point: A new point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Physics(x, y)

    def equals(self, other):
        """Whether or not this point is equal to the given one.

        Args:
            other (Point): The point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.

        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.

        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.

        Returns:
            Point: A new Point that is scaled.
        """
        return Physics(self._x * factor, self._y * factor)

    def falling_gems():
        text = "*"
        x = random.randint(1, COLS-1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
