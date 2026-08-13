import random
class Stat:
    def __init__(self):
        self.damage_upgrade = random.randint(1,2)
        self.hp_upgrade = random.randint(10,13)
        self.crit_chance_upgrade = round(random.uniform(1,2),1)
        self.stat_usage = 1
    def menu(self,player):
        return (f'''======LEVEL UP======\nStat Points = {player.progress.stat_points}
1. +{self.damage_upgrade} Damage\n2. +{self.hp_upgrade} Hp\n3. +{self.crit_chance_upgrade}% Critical Chance
4.Exit''')
    def choose_upgrade(self,player):
        while True:
            try:
                choose = int(input(f'{self.menu(player)}\nchoose one : '))
                if not (1<= choose <= 4):
                    raise ValueError
                return choose
            except ValueError:
                print('Enter number on the menu!')
                continue
    def stat_check(self,player):
        return player.progress.stat_points >= self.stat_usage
    def stat_use(self,player):
        player.progress.stat_points -= self.stat_usage 
    def damage_increase(self,player):
        if self.stat_check(player):
            player.base_damage += self.damage_upgrade
            self.stat_use(player)
            return True
        return False
    def hp_increase(self,player):
        if self.stat_check(player):
            player.hp += self.hp_upgrade
            self.stat_use(player)
            return True
        return False
    def crit_chance_increase(self,player):
        if self.stat_check(player):
            player.base_critical_chance += self.crit_chance_upgrade / 100
            self.stat_use(player)
            return True
        return False
    
    def main_menu(self,player):
        while True :
            choose = self.choose_upgrade(player)
            if choose == 4:
                return
            elif choose == 1:
                if self.damage_increase(player):
                    print(f'+{self.damage_upgrade} Damage')
                    continue
                else:
                    print('not enough stat points')
                    continue
            elif choose == 2 :
                if self.hp_increase(player):
                    print(f'+{self.hp_upgrade} Hp')
                    continue
                else:
                    print('not enough stat points')
                    continue
            elif choose == 3:
                if self.crit_chance_increase(player):
                    print(f'+{self.crit_chance_upgrade}% Critical Chance')
                    continue
                else:
                    print('not enough stat points')
                    continue