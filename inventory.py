class Inventory:
    def __init__(self):
        self.inventory = []
        self.max_item = 5
        self.max_weight = 10
    def add_item(self,item):
        if self.is_full:
            return False ,'inventory is full'
        if self.count_item(item) >= item.max_stack:
            return False ,(f'cant have more than {item.max_stack} of {item.name}')
        if self.current_weight + item.weight > self.max_weight:
            return False ,'inventory is too heavy'
        self.inventory.append(item)
        return True , 'Add loot successful'
    def add_loot(self,enemy):
        result , msg = self.add_item(enemy)
        if not result:
            return result,msg
        if result:
            return result ,'loot added'
    def remove_item(self,item):
        if self.has_item(item):
            self.inventory.remove(item)
            return True
        return False
    def count_item(self,item):
        same_item = [i for i in self.inventory if i.name == item.name]
        return len(same_item)
    @property
    def is_empty(self):
        return len(self.inventory) == 0
    @property
    def is_full(self):
        return len(self.inventory) >= self.max_item
    def has_item(self,item):
        return item in self.inventory
    @property
    def current_weight(self):
        weight = 0
        for item in self.inventory:
            weight += item.weight
        return weight
    def get_item(self,index :int):     
        return self.inventory[index - 1 ]
    def choose_item(self):
        while True:
            self.show_inventory()
            try:
                choose = int(input(f'{len(self.inventory) +1}. Back\nchoose one : '))
                if not (1<= choose <= len(self.inventory)):
                    raise ValueError
                return choose
            except ValueError:
                print('enter number on the menu')
                continue               
    def use_item(self,player):
        choose = self.choose_item()
        if choose == len(self.inventory) + 1:
            return        
        item = self.get_item(choose)
        player.use_item(item)
    def show_inventory(self):
        count = 1        
        for count ,item in enumerate(self.inventory,1):
            print(f'{count}. {item.name}')

