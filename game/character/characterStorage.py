class CharacterStorage:

    def __init__(self):
        self._characters = {}
    
    def add_new_character(self,group,character):
        if not group in self._characters.keys():
            self._characters[character.get_group_name()] = []

        if not character in self._characters[group]:
            self._characters[group].append(character)

    def get_all_characters(self):
        return self._characters

    def get_character(self,group):
        if group in self._characters.keys():
            return self._characters[group]
    
    # def set_character(self,group):
    #     if group in self._characters.keys():
            