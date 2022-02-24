import pyray
class Display:
    """ 
        Display class will be will be in charge of showing all the elements of the game
        Attributes:
            _width (int) : the width of the display window
            _height (int) : the height of the display window
            _game_name (str) : the name of the game
        Author:  Samuel Beltran

    """
    def __init__(self,width,height,gameName,frameNumber):
        self._width = width
        self._height = height
        self._game_name = gameName
        self._frame_nummber = frameNumber
        

    def open_window(self):
        pyray.init_window(self._width, self._height, self._game_name)
        pyray.set_target_fps(self._frame_nummber)

    def close_window(self):
        pyray.close_window()

    def is_playing(self):
        return not pyray.window_should_close()
        
    def start_drawing(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
    def stop_drawing(self):
        pyray.end_drawing()

    def draw_character(self,item):
        pyray.draw_text(item.get_appearance,item.get_x_position,item.get_y_position, item.get_fontsize,item.get_color)