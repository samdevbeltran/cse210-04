from  game.states.collision import Collision
class Director:
    """ 
        All the parts of the game are managed in this file
        Attributes: 
            _characters (Character)
            _display (Display)
        author: Samuel Beltran
    """
    def __init__(self,characters,display,score,points):
        self._characters = characters
        self._display = display
        self._score = score
        self._points = points
    
    def start_game(self):
        
        self._display.open_window()
        
        while self._display.is_playing():
            self._display.start_drawing()
            self.__input_player()
            self.__update()
            self.__result()
            self._display.stop_drawing()
        self._display.close_window()

    def get_characters(self):
        return self._characters

    def get_display(self):
        return self._display
    
    def __input_player(self):
        print("it will work soon")

    def __update(self):
        collision = Collision(self._characters,self._score).check_collision()
        self._score = collision.get_score()

    def __result(self):
        print("here the result will be display")