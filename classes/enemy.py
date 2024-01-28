class Enemy():
    """ Класс для описания врагов """

    def __init__(self, name = "", level = 1, damage = 0, block = 0, loot = []):
        self.name = name
        self.level = level
        self.damage = damage
        self.block = block
        self.loot = loot