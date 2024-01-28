class Armor():
    """ Класс для описания брони """
    
    def __init__(self, name = "Davion's Armor", required_level = 1, block = 0, price = 0):
        self.name = name
        self.required_level = required_level
        self.block = block
        self.price = price