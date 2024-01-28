class Player():
    """ Класс для описания главного героя """

    def __init__(self, name = "", health = 100, level = 1, money = 0, weapons = [], armors = [], inventory = [], keys = []):
        self.name = name
        self.health = health
        self.level = level
        self.money = money
        self.weapons = weapons
        self.armors = armors
        self.inventory = inventory
        self.keys = keys
        self.equipped_weapon = None
        self.equipped_armor = None
    
    def say(self, text):
        return f"{self.name}: {text}"
    
    def equip_weapon(self, weapon_index):
        if weapon_index >= len(self.weapons) or weapon_index < 0:
            print("Game Error:\nweapon_index is out of inventory length")
            print("If you want to help me and game, please tell me about this error. You can find my contacts in GitHub profile. Thank You!")
            return False
        
        weapon = self.weapons[weapon_index]

        if self.level >= weapon.level:
            self.equiped_weapon = weapon
            print(f"{self.name} взял в руки {weapon.name}.")
            return True
        else:
            print(f"{self.name}у нужно достичь {weapon.level} уровня, чтобы управиться с '{weapon.name}'.")
            return False
    
    def equip_armor(self, armor_index):
        if armor_index >= len(self.armors) or armor_index < 0:
            print("Game Error:\narmor_index is out of inventory length")
            print("If you want to help me and game, please tell me about this error. You can find my contacts in GitHub profile. Thank You!")
            return False
        
        armor = self.armors[armor_index]

        if self.level >= armor.level:
            self.equipped_armor = armor
            print(f"{self.name} надел {armor.name}.")
            return True
        else:
            print(f"{self.name}у нужно достичь {armor.level} уровня, чтобы надеть '{armor.name}'.")
            return False