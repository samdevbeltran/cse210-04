class Collision:
    """ 
        dtects if the player hits a rock or a gem 
        Attributes:
            _characters (dict) : Dictionary of characters
            _player (Player) : the player
            _score (Score) : Instance of score
        Author:Vadim
    """

    def __init__(self):
        self

    def _do_updates(self, cast, score):
        """Updates the player's position and resolves any collisions with characters.

        Args:
            cast (Cast): The cast of characters."""

        player = cast.get_first_character("player")
        gems = cast.get_characters("gems")
        rocks = cast.get_characters("rocks")

        for gem in gems:
            if player.get_position().equals(gem.get_position()):
                score.lose_point()
            elif player.get_position().equals(rocks.get_position()):
                score.earn_point()
