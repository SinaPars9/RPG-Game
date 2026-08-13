from inventory import Inventory
from equipments import Equipment
from items import Potion
import random
class Character:
    def __init__(self,name,hp):
        self.name = name
        self.hp= hp
        self.effects = []
        self.stunned = False
        self.poisoned = False
        self.burned = False
    def take_damage(self,damage):
        damage = max(1,damage - self.defence)
        self.hp -= damage
        return self.hp <= 0
    def update_effects(self):
        for effect in self.effects[:]:
            effect.apply(self)
            effect.tick()
            if effect.expierd:
                effect.on_expierd(self)
                self.effects.remove(effect)
    def add_effect(self, effect):
        for current_effect in self.effects:
            if current_effect.name == effect.name:
                current_effect.duration = effect.duration
                return
        self.effects.append(effect)

    @property
    def defence(self):
        return 0
    def show_status(self):
        return (f'======{self.name} INFO======\nHP : {self.hp}')
class Progress:
    def __init__(self):
        self.level = 1
        self.current_xp = 0
        self.next_level_xp = 100
        self.stat_points = 0
        self.level_up_stat_point = 5
    def add_xp(self,enemy):
        self.current_xp += enemy.xp    
    def stat_point_upgrade(self):
        self.stat_points += self.level_up_stat_point
    def level_increase(self):
        self.level += 1
    @property
    def level_up_check(self):
        if self.current_xp >= self.next_level_xp:
            self.current_xp -= self.next_level_xp
            return True
        return False
    def level_up(self):
        if self.level_up_check:
            self.stat_point_upgrade()
            self.level_increase()
            self.next_level_xp += 50
            return True
        return False
    def gain_xp(self,enemy):
        self.add_xp(enemy)
        if self.level_up():
            return True
        return False
class Player(Character):
    def __init__(self, name, hp,damage,gold):
        super().__init__(name, hp)
        self.base_damage = damage
        self.gold = gold
        self.base_defence = 0
        self.base_critical_chance = 0.2
        self.progress = Progress()
        self.inventory = Inventory()
        self.equipment = Equipment()
    def attack(self,target):
        damage , critical = self.calculate_damage()
        dead = target.take_damage(damage)
        return damage , critical , dead    
    @property
    def defence(self):
        defence = self.base_defence
        if self.burned:
            defence -= 5
        if self.equipment.shield:
            defence += self.equipment.shield.defence_bonus
        return max(0,defence) 
    def calculate_damage(self):
        damage = self.base_damage
        if self.equipment.weapon:
            damage += self.equipment.weapon.damage_bonus       
        critical = False
        if random.random() < self.calculate_chance:
            damage += random.randint(8, 12)
            critical = True
        return damage , critical
    @property
    def calculate_chance(self):
        chance = self.base_critical_chance 
        if self.poisoned:
            chance -=  0.1
        if self.equipment.weapon:
            chance += self.equipment.weapon.critical_chance
        return max(0,chance)
    def gain_xp(self,enemy):
        return self.progress.gain_xp(enemy)
    @property
    def stun_check(self):
        return self.stunned
    @property 
    def burn_check(self):
        return self.burned
    @property
    def poison_check(self):
        return self.poisoned
    def buy_item(self,item):
        if self.gold < item.price:
            return False
        self.gold -= item.price
        return True
    def use_item(self,item):
        if isinstance(item,Potion):
            self.inventory.remove_item(item)
        return item.use(self)
    @property
    def is_alive(self):
        return self.hp > 0
    def add_gold(self,enemy):
        self.gold += enemy.gold_drop
    def show_status(self):
        weapon_name = None
        shield_name = None
        if self.equipment.weapon:
            weapon_name = self.equipment.weapon.name
        if self.equipment.shield:
            shield_name = self.equipment.shield.name
        return (f'''{super().show_status()}\nDamage : {self.base_damage}\nWeapon : {weapon_name}\nShield : {shield_name}\n
Level : {self.progress.level}\nstat points : {self.progress.level_up_stat_point}\nXP : {self.progress.current_xp}
Critical Chance: {self.calculate_chance}%''')
class Enemy(Character):
    def __init__(self, name, hp,damage,gold_drop,xp,loot = None,skills = None,skill_chance = 0.2):
        super().__init__(name, hp)
        self.damage = damage
        self.gold_drop = gold_drop
        self.xp = xp
        self.loot = loot if loot else [] 
        self.skills = skills if skills else []
        self.max_hp = hp
        self.skill_chance = skill_chance
    def use_skill(self, skill, target):
        return skill.use(self, target)
    def attack(self,target):
        return target.take_damage(self.damage)
    @property
    def is_alive(self):
        return self.hp > 0
    def show_status(self):
        if self.skills:
            skill_name = ' , '.join(skill.name for skill in self.skills)
        else:
            skill_name = None
        loot_name = self.loot.name if self.loot else None
        return (f'{super().show_status()}\nDamage : {self.damage}\nReward : {self.gold_drop}\nXP : {self.xp}\nLoot : {loot_name}\nSkill : {skill_name}')



