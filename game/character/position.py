class Position:
    """ 
    this will set the position of a character 
    Atributes:
    _X (int) : this is the position in x
    _y (int) : this is the position in y
    Author:Karras
    """
    def __init__(self,x,y):
      self._x = x
      self._y = y  
    
    def set_x_position(self,x):
        self._X = x
    
    def set_y_position(self,y):
        self._y = y
    
    def get_x_position(self):
        return self._x
    
    def get_y_position(self):
        return self._y
    
    def get_position(self):
        return Position(self._x,self._y)

    def equals(self,charcterA,charcterB):
        if charcterA.get_x_position() == charcterB.get_x_position() and charcterA.get_y_position() == charcterB.get_y_position():
            return True