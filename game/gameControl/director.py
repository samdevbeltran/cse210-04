from  game.states.collision import Collision
from  game.services.keyboard import Keyboard
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
        
        # player = self._characters.get_character("player")
        # print(player[0].get_group_name())
        self._display.open_window()
        player = self._characters.get_character("player")[0]

        while self._display.is_playing():
            self._display.start_drawing()
            self.__input_player(player)
            self.__update()
            # self.__result()
            self._display.stop_drawing()
        self._display.close_window()

    def get_characters(self):
        return self._characters

    def get_display(self):
        return self._display
    
    def __input_player(self,player):

        keyboard = Keyboard().get_direction()
        x = player.get_x_position()
        
        if keyboard != 0:
            player.set_x_position(x + player.scale_x_position(keyboard))    

    def __update(self):
        player = self._characters.get_character("player")
        # collision = Collision(self._characters,self._score).check_collision()
        # self._score = collision.get_score()
        self._display.draw_character(player[0])
        

    def __result(self):
        print("here the result will be display")