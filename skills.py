import random
from effects import Poison , Stun , Burn
class Skill:
    def __init__(self,name,cooldown = 0):
        self.name = name
        self.cooldown = cooldown
        self.current_cooldown = 0
    def can_use(self):
        return self.current_cooldown == 0
    def start_cooldown(self):
        self.current_cooldown = self.cooldown
    def reduce_cooldown(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
    def use(self,user,target):
        pass

class Attack(Skill):
    def __init__(self, name, cooldown=0):
        super().__init__(name, cooldown)
    def use(self, user, target):
        damage = user.damage
        dead = target.take_damage(damage)
        return damage , dead , f'{user.name} Attacked'

class Miss(Skill):
    def __init__(self, name, cooldown=0):
        super().__init__(name, cooldown)
    def use(self, user, target):
        target.take_damage(0)
        return 0,False, f'{user.name} Missed'
class Heavyattack(Skill):
    def __init__(self, name, cooldown=4):
        super().__init__(name, cooldown)
    def use(self, user, target):
        damage = int(user.damage * 1.5)
        dead = target.take_damage(damage)
        return damage , dead , f'{user.name} used Heavy Attacked'

class Heal(Skill):
    def __init__(self, name, cooldown=3):
        super().__init__(name, cooldown)
        self.heal_amount = 15
    def use(self, user, target):
        old_hp = user.hp
        user.hp = min(user.max_hp, user.hp + self.heal_amount)
        healed = user.hp - old_hp
        return 0,False, f'{user.name} healed {healed}'  

class CriticalAttack(Skill):
    def __init__(self, name, cooldown=2):
        super().__init__(name, cooldown)
        self.critical_chance = 0.2
    def use(self, user, target):
        damage = user.damage
        if random.random() < self.critical_chance:
            damage += random.randint(5,10)
        dead =  target.take_damage(damage)
        return damage , dead , f'{user.name} did ciritical Attack '

class DoubleAttack(Skill):
    def __init__(self, name, cooldown=3):
        super().__init__(name, cooldown)
    def use(self, user, target):
        total_damage = 0
        for _ in range(2):
            damage , dead , msg = Attack('Normal Attack').use(user,target)
            total_damage += damage
            if dead:
                break
        return total_damage , dead , msg

class PoisonAttack(Skill):
    def __init__(self, name, cooldown=3):
        super().__init__(name, cooldown)
    def use(self, user, target):
        damage = user.damage
        dead = target.take_damage(damage)
        target.add_effect(Poison())
        return damage , dead , (f'{user.name} poisoned {target.name} for {damage} Damage')

class StunAttack(Skill):
    def __init__(self, name, cooldown=2):
        super().__init__(name, cooldown)
    def use(self, user, target):
        damage = user.damage
        dead = target.take_damage(damage)
        target.add_effect(Stun())
        return damage , dead , (f'{user.name} Stunned {target.name} and did {damage} Damage')

class BurnAttack(Skill):
    def __init__(self, name, cooldown=3):
        super().__init__(name, cooldown)
    def use(self, user, target):
        damage = user.damage
        dead = target.take_damage(damage)
        target.add_effect(Burn())
        return damage , dead , (f'{user.name} Burned {target.name} and did {damage} Damage')
         

          

