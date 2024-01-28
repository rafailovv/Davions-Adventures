class Item():
    """ Класс для описания предметов """

    def __init__(self, name = "", description = "", health_boost = 0, damage_boost = 0, block_boost = 0):
        self.name = name
        self.description = description
        self.health_boost = health_boost
        self.damage_boost = damage_boost
        self.block_boost = block_boost