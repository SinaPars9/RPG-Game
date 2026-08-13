class Equipment():
    def __init__(self):
        self.weapon = None
        self.shield = None
    def equip_weapon(self,weapon):
        self.weapon = weapon
    def equip_shield(self,shield):
        self.shield = shield
    def unequip_weapon(self):
        self.weapon = None
    def unequip_shield(self):
        self.shield = None    
    