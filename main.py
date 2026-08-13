from characters import Player
from shop import Shop
from fight import Fight
from stat_points import Stat
from save_system import save_game,load_game,delete_save
class main:
    stat = Stat()
    shop = Shop()
    fight = Fight()
    player = None
    def __init__(self):
        self.player = load_game()
        if self.player is None:
            self.player = Player('Sina',100,15,100)
            print('new player created')
        else:
            print('welcome back')
    def main_menu(self):
        return ('1.Show status\n2.Show inventory\n3.Use item\n4.Level up\n5.Shop\n6.Fight\n'
        '7.save game\n8.Load game\n9.exit')
    def choose_menu(self):
        while True:
            try:
                choose = int(input(f'{self.main_menu()}\nchoose one : '))
                if not (1<= choose <= 9):
                    raise ValueError
                return choose
            except ValueError:
                print('enter number on the menu')
                continue
    def run(self):
        while True:
            choose = self.choose_menu()
            if choose == 9 :
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
                if self.player.is_alive:
                    save_game(self.player)
            if choose == 7:
                save_game(self.player)
            if choose == 8:
                new_player = load_game()
                if new_player:
                    self.player = new_player
                    print('game loaded')   


if __name__ == "__main__":
    game = main()
    game.run()
