class Weapon():
    """ Класс для описания оружия """
    
    def __init__(self, name = "Davion's Sword", required_level = 1, damage = 0, price = 0):
        self.name = name
        self.required_level = required_level
        self.damage = damage
        self.price = price