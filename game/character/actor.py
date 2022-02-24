from game.character.character import Character

class Actor(Character):

    def __init__(self,appearance,groupName,x,y,fontSize,scale,color= ""):
        self._groupName = groupName
        Character.__init__(self,appearance,x,y,fontSize,scale,color)

    def get_group_name(self):
        return self._groupName

