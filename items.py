class Item:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.max_stack = 1
    def use(self,player):
        pass
    def show_info(self):
        return(f'====={self.name} INFO=====\nPrice : {self.price}\nWeight : {self.weight}')

class Weapon(Item):
    def __init__(self, name, price, weight,damage_bonus,critical_chance):
        super().__init__(name, price, weight)
        self.damage_bonus = damage_bonus
        self.weight = weight
        self.max_stack = 1
        self.critical_chance = critical_chance
    def use(self, player):
        player.equipment.equip_weapon(self)
    def show_info(self):
        return (f'{super().show_info()}\nDamage Bonus : {self.damage_bonus}\ncritical_chance : {self.critical_chance}%')

class Shield(Item):
    def __init__(self, name, price, weight,defence_bonus):
        super().__init__(name, price, weight)
        self.defence_bonus = defence_bonus
        self.weight = weight
        self.max_stack = 1
    def use(self, player):
        player.equipment.equip_shield(self)
    def show_info(self):
        return (f'{super().show_info()}\nDefence Bonus : {self.defence_bonus}')

class Potion(Item):
    def __init__(self, name, price, weight,heal_amount):
        super().__init__(name, price, weight)
        self.heal_amount =  heal_amount
        self.weight = weight
        self.max_stack = 2
    def use(self, player):
        player.hp += self.heal_amount
    def show_info(self):
        return (f'{super().show_info()}\nHeal Amount : {self.heal_amount}')