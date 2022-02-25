class Physics:
    """This will generates the falling down of the rocks and the gems """

    def __init__(self,characters,video_service,scale,gravity):

        self._video_service = video_service
        self._characters = characters
        self._scale = scale
        self._gravity = gravity

    def move_gem(self):
        
        gems = self._characters.get_character("gem")
       
        for gem in gems:
            gem.set_y_position(gem.get_y_position() + (self._scale - self._gravity))
            self._video_service.draw_character(gem)


    def move_rock(self):
        
        for rock in self._characters.get_character("rock"):            
            
            rock.set_y_position(rock.get_y_position() + (self._scale - self._gravity))
            self._video_service.draw_character(rock)
        
