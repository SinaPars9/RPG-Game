from items import Weapon,Shield,Potion
from characters import Player
class Shop:
    weapon_shop_items = [    
    Weapon('Sword',50,2,10,0.01),
    Weapon('Bow',80,3,15,0.02),
    Weapon('Axe',120,4,25,0.03)
    ]
    Potion_shop_items = [
        Potion('Small_potion',20,2,30),
        Potion('Medium Potion',45,3,70),
        Potion('Mega Potion',100,4,150)
        ]
    shield_shop_items=[
        Shield('light shield',10,2,7),
        Shield('normal shield',15,3,10),
        Shield('heavy shield',22,1,15)
    ]  
    def main_menu(self):
        while True:
            try:
                choose = int(input('1.weapon\n2.potion\n3.shield\n4.Back\nchoose one : '))
                if not (1<= choose <= 4):
                    raise ValueError
                return choose
            except ValueError:
                print('enter number on the menu')
                continue
    def weapon_shop_menu(self):
        for count , item in enumerate(self.weapon_shop_items,1):
            print(f'{count}. {item.show_info()}')
        print(f'{count + 1}. Back')
    def potion_shop_menu(self):
        for count , item in enumerate(self.Potion_shop_items,1):
            print(f'{count}. {item.show_info()}')
        print(f'{count + 1}. Back')
    def shield_shop_menu(self):
        for count , item in enumerate(self.shield_shop_items,1):
            print(f'{count}. {item.show_info()}')
        print(f'{count + 1}. Back')
    def buy_weapon(self):
        while True:
            self.weapon_shop_menu()
            try:
                choose = int(input('choose one : '))
                if not (1<= choose <= len(self.weapon_shop_items) + 1):
                    raise ValueError
            except ValueError:
                print('enter number on the menu')
                continue
            if choose == len(self.weapon_shop_items) + 1:
                return
            return choose
    def buy_potion(self):
        while True:
            self.potion_shop_menu()
            try:
                choose = int(input('choose one : '))
                if not (1<= choose <= len(self.Potion_shop_items) + 1):
                    raise ValueError
            except ValueError:
                print('enter number on the menu')
                continue
            if choose == len(self.Potion_shop_items) + 1:
                return
            return choose
    def buy_shield(self):
        while True:
            self.shield_shop_menu()
            try:
                choose = int(input('choose one : '))
                if not (1<= choose <= len(self.shield_shop_items) + 1):
                    raise ValueError
            except ValueError:
                print('enter number on the menu')
                continue
            if choose == len(self.shield_shop_items) + 1:
                return
            return choose
    def buy(self,player,item):
        if player.gold < item.price:
            return 'not enough gold'
        result , message = player.inventory.add_item(item)
        if not result:
            return message
        player.gold -= item.price
        return 'Purchase successful' 
        
    def main_buy(self,player):
        while True:
            choose = self.main_menu()
            if choose == 4 :
                return
            if choose == 1:
                result = self.buy_weapon()
                get_item = self.weapon_shop_items[result - 1]
                buy_result = self.buy(player,get_item)
                print(buy_result)
            if choose == 2:
                result = self.buy_potion()
                get_item = self.Potion_shop_items[result - 1]
                buy_result = self.buy(player,get_item)
                print(buy_result)
            if choose == 3:
                result = self.buy_shield()
                get_item = self.shield_shop_items[result - 1]
                buy_result = self.buy(player,get_item)
                print(buy_result)



