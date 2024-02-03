from classes.settings import Settings
from classes.davion import Davion
from levels.prologue import Prologue

class Game():
    """ Класс для создания игры """

    def __init__(self):
        """ Последовательно воссоздаем игровой процесс """
        self.settings = Settings()
        self.davion = Davion(self)

        self.level_1 = Prologue(self)
    
    def run_game(self):
        self.level_1.start_level()

if __name__ == "__main__":
    game = Game()
    game.run_game()