class Physics:
    """This will generates the falling down of the rocks and the gems 
            Attributes:
                _video_service (Display) : An instantiation of Display
                _characters (Character) : An instatiation of Character
                _scale (int) : The scale of position
                _gravity (int) : the farce that brings the characters down
        Author: Vadim
    """

    def __init__(self,characters,video_service,scale,gravity):

        self._video_service = video_service
        self._characters = characters
        self._scale = scale
        self._gravity = gravity

    def move_gem(self):
        """ Makes the gem fall down """
        for gem in self._characters.get_character("gem"):
            gem.set_y_position(gem.get_y_position() + self._gravity)
            self._video_service.draw_character(gem)


    def move_rock(self):
        """ Makes the rocks fall down """
        for rock in self._characters.get_character("rock"):            
            rock.set_y_position(rock.get_y_position() + (self._gravity))
            self._video_service.draw_character(rock)
        
