from characters import Player
from shop import Shop
from fight import Fight
from stat_points import Stat
class main:
    stat = Stat()
    shop = Shop()
    fight = Fight()
    player = Player('Sina',1000,10,1000)
    def main_menu(self):
        return ('1.Show status\n2.Show inventory\n3.Use item\n4.Level up\n5.Shop\n6.Fight\n7.Exit')
    def choose_menu(self):
        while True:
            try:
                choose = int(input(f'{self.main_menu()}\nchoose one : '))
                if not (1<= choose <= 7):
                    raise ValueError
                return choose
            except ValueError:
                print('enter number on the menu')
                continue
    def run(self):
        while True:
            choose = self.choose_menu()
            if choose == 7 :
                print('Buy')
                break
            if choose == 1 :
                print(self.player.show_status())
            if choose == 2:
                if not self.player.inventory.is_empty:
                    self.player.inventory.show_inventory()
                    continue
                print('Inventory is empty')
                continue
            if choose == 3:
                if not self.player.inventory.is_empty:
                    self.player.inventory.use_item(self.player)
                    continue
                print('Inventory is empty')
                continue
            if choose == 4:
                self.stat.main_menu(self.player)
            if choose == 5:
                self.shop.main_buy(self.player)
            if choose == 6:
                self.fight.start_battle(self.player)


if __name__ == "__main__":
    game = main()
    game.run()
