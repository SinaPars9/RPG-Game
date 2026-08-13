class Effects:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
    def apply(self,target):
        pass
    def tick(self):
        self.duration -= 1
    @property
    def expierd(self):
        return self.duration <=0
    def on_expierd(self,target):
        pass
class Posion(Effects):
    def __init__(self,):
        super().__init__('poison', duration = 4)
        self.damage = 3
    def apply(self, target):
        target.poisoned = True
        target.take_damage(self.damage)
        print(f'{target.name} takes {self.damage} poison damage')
    def on_expierd(self,target):
        target.poisoned = False
        

class Stun(Effects):
    def __init__(self,):
        super().__init__('stun', duration = 2)
        self.damage = 3
    def apply(self, target):
        target.take_damage(self.damage)
        target.stunned = True
        print(f'{target.name} takes {self.damage} stun damage')
    def on_expierd(self,target):
        target.stunned = False

class Burn(Effects):
    def __init__(self):
        super().__init__('burn', duration=2)
        self.damage = 7
    def apply(self, target):
        target.take_damage(self.damage)
        target.burned = True
        print(f'{target.name} takes {self.damage} burn damage')
    def on_expierd(self, target):
        target.burned = False
        