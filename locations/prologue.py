class Prologue():
    """ Класс для локации Пролог """

    def __init__(self, player, location_name):
        self.player = player
        self.location_name = location_name
    
    def start(self, start_text):
        print(start_text + "\n")