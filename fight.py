from characters import Player
from enemy_data import enemy
from skills import Attack
import random
class Fight:
    enemies = enemy()
    @property
    def get_alive_enemies(self):
        alive = [enemy for enemy in self.enemies if enemy.is_alive]
        return alive
    @property
    def random_enemy(self):
        alive = self.get_alive_enemies
        if alive:
            enemy = random.choice(alive)
            return enemy
        return None

    def show_alive_enemies(self):
        alive = self.get_alive_enemies
        for count ,enemy in enumerate(alive,1):
            print(f'{count} : \n{enemy.show_status()}\n')
        print(f'{count + 1}. Back')

    def enemy_turn(self,player,enemy):
        enemy.update_effects()
        if not enemy.is_alive:
            return 0, True, f"{enemy.name} died from effects" 
        available_skill = [skill for skill in enemy.skills if skill.can_use()]
        if available_skill and random.random() < enemy.skill_chance:
            skill = random.choice(available_skill)
            damage , dead , msg = skill.use(enemy,player)
            skill.start_cooldown()
        else:
            damage , dead , msg = Attack(' Normal Attack').use(enemy,player)
        for skill in enemy.skills:
            skill.reduce_cooldown()
        return damage , dead , msg
    def player_turn(self,player,enemy):
        player.update_effects()
        if not player.is_alive:
            return 0 , False , ('you died from effects')          
        if player.stun_check :
           return 0 , False ,('you are stunned you cant Attack')           
        else:
            damage , critical ,dead = player.attack(enemy)
            return damage , critical , dead
 
    def enemy_battle(self,player,enemy):
        while True:
            try :
                choose = int(input(f'{enemy.show_status()}\n{player.show_status()}\n1.Attack\n2.Run away\nchoose one : '))
                if not (1 <= choose <= 2 ):
                    raise IndexError ('number out of range')
                return choose
            except ValueError:
                print('enter number')
            except IndexError as e:
                print (e)
    def start_battle(self,player):
        enemy = self.random_enemy
        if enemy == None:
            print('all enemies are dead!')
            return
        if  not player.is_alive:
            print('you died')
            return
        else:
            while True:
                choose = self.enemy_battle(player,enemy)
                if choose == 1 :
                    damage , critical , dead = self.player_turn(player,enemy)
                    if isinstance (dead,str) :
                        print(dead)
                        continue
                    print(f'you attacked {enemy.name}')
                    if critical:
                        print(f'critical hit {damage} Damage')
                    if dead:
                        player.add_gold(enemy)
                        print(f'you killed {enemy.name}')
                        if  enemy.loot :
                            result , msg =player.inventory.add_loot(enemy.loot)
                            print(msg)
                        else:
                            print('enemy had no loot!')           
                        if player.gain_xp(enemy):
                            print ('you leveled up')
                        print (f'Gained {enemy.gold_drop} gold and {enemy.xp} XP')
                        return 
                    damage , dead , msg = self.enemy_turn(player,enemy)
                    print(f'{msg}')
                    if dead :
                        print('you died')
                        return
                if choose == 2 :
                    return


