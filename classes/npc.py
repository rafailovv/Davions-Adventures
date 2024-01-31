class npc():
    """ Класс для описания NPC """

    def __init__(self, name = ""):
        self.name = name
    
    def say(self, text):
        return f"{self.name}: {text}"