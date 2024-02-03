class NPC():
    """ Инициализирует класс для создания NPC """

    def __init__(self, game, name, phrases = []):
        """ Инициализируем параметры NPC """
        self.settings = game.settings

        self.name = name
        self.phrases = phrases
    
    def _add_phrase(self, phrase):
        if phrase:
            self.phrases.append(phrase)