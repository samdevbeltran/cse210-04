from game.character.character import Character
""" This inherits from Character class and its gunction is to create a new character for the game
        Attributes: 
            _groupName (str): The name of the character
        Author:Yami
"""
class Actor(Character):

    def __init__(self,appearance,groupName,x,y,fontSize,scale,color= ""):
        self._groupName = groupName
        Character.__init__(self,appearance,x,y,fontSize,scale,color)

    def get_group_name(self):
        """ Gets the name of the group of characters
            return: Str
        """
        return self._groupName

