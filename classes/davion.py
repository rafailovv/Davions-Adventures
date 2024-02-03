class Davion():
    """ Класс для описания главного героя """

    def __init__(self, game):
        """ Задаем главному герою параметры """
        self.settings = game.settings

        # Настройки Дэвиона
        self.name = self.settings.davion_name
    
    def say(self, text):
        if text:
            return f"{self.name}: {text}"