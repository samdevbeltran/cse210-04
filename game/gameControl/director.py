class Director:
    """ 
        All the parts of the game are managed in this file
        Attributes: 
            _characters (Character)
            _display (Display)
        author: Samuel Beltran
    """
    def __init__(self,characters,display):
        self._characters = characters
        self._display = display
    
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
        print("the input will be taken")

    def __update(self):
        print("this will update all the characters")

    def __result(self):
        print("here the result will be display")