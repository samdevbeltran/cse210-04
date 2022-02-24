

from game.gameLogic.score import Score


class Collision:
    """ 
        dtects if the player hits a rock or a gem 
        Attributes:
            _characters (dict) : Dictionary of characters
            _player (Player) : the player
            _score (Score) : Instance of score
        Author:Vadim
    """

    def __init__(self, characters, score, points):
        self._characters = characters
        self._score = score
        self._points = points

    def check_collision(self):
        """Checks if the player is colliding with an object.

        Args:
            self (self): The cast of characters."""

        score = Score(self._points)

        player = self.characters.get_first_character("player")
        gems = self.characters.get_characters("gems")
        rocks = self.characters.get_characters("rocks")

        for gem in gems:
            if self.__is_colliding(player, gem):
                self._score = score.earn_point(self._score)

        for rock in rocks:
            if self.__is_colliding(player, rock):
                self._score = score.lose_point(self._score)

    def __is_colliding(self, player, character):
        if character.equals(character.get_position(), player.get_position()):
            return True

    def get_score(self):
        return self._score
