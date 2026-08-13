import json
import os
from characters import Player
from items import Weapon, Shield, Potion
from inventory import Inventory
from equipments import Equipment

# ========== تبدیل به دیکشنری (برای ذخیره) ==========

def player_to_dict(player):
    """تبدیل وضعیت کامل بازیکن به دیکشنری برای ذخیره در JSON"""
    data = {
        "name": player.name,
        "hp": player.hp,
        "base_damage": player.base_damage,
        "gold": player.gold,
        "base_defence": player.base_defence,
        "base_critical_chance": player.base_critical_chance,
        
        # اطلاعات پیشرفت (Progress)
        "progress": {
            "level": player.progress.level,
            "current_xp": player.progress.current_xp,
            "next_level_xp": player.progress.next_level_xp,
            "stat_points": player.progress.stat_points,
            "level_up_stat_point": player.progress.level_up_stat_point
        },
        
        # موجودی (Inventory)
        "inventory": inventory_to_dict(player.inventory),
        
        # تجهیزات (Equipment)
        "equipment": equipment_to_dict(player.equipment),
        
        # اثرات فعال (Effects)
        "effects": effects_to_dict(player.effects)
    }
    return data


def inventory_to_dict(inventory):
    """تبدیل موجودی به لیست دیکشنری"""
    items_data = []
    for item in inventory.inventory:
        if isinstance(item, Weapon):
            items_data.append({
                "type": "weapon",
                "name": item.name,
                "price": item.price,
                "weight": item.weight,
                "damage_bonus": item.damage_bonus,
                "critical_chance": item.critical_chance
            })
        elif isinstance(item, Shield):
            items_data.append({
                "type": "shield",
                "name": item.name,
                "price": item.price,
                "weight": item.weight,
                "defence_bonus": item.defence_bonus
            })
        elif isinstance(item, Potion):
            items_data.append({
                "type": "potion",
                "name": item.name,
                "price": item.price,
                "weight": item.weight,
                "heal_amount": item.heal_amount
            })
    return items_data


def equipment_to_dict(equipment):
    """تبدیل تجهیزات مجهز به دیکشنری"""
    data = {}
    if equipment.weapon:
        data["weapon"] = {
            "name": equipment.weapon.name,
            "price": equipment.weapon.price,
            "weight": equipment.weapon.weight,
            "damage_bonus": equipment.weapon.damage_bonus,
            "critical_chance": equipment.weapon.critical_chance
        }
    if equipment.shield:
        data["shield"] = {
            "name": equipment.shield.name,
            "price": equipment.shield.price,
            "weight": equipment.shield.weight,
            "defence_bonus": equipment.shield.defence_bonus
        }
    return data


def effects_to_dict(effects):
    """تبدیل اثرات فعال به لیست دیکشنری"""
    effects_data = []
    for effect in effects:
        effects_data.append({
            "name": effect.name,
            "duration": effect.duration
        })
    return effects_data


# ========== ساخت اشیاء از دیکشنری (برای بارگذاری) ==========

def dict_to_player(data):
    """ساخت بازیکن از دیکشنری (برای بارگذاری)"""
    player = Player(
        name=data["name"],
        hp=data["hp"],
        damage=data["base_damage"],
        gold=data["gold"]
    )
    
    # بازگرداندن مقدارهای پایه
    player.base_defence = data.get("base_defence", 0)
    player.base_critical_chance = data.get("base_critical_chance", 0.2)
    
    # بارگذاری پیشرفت (Progress)
    progress_data = data["progress"]
    player.progress.level = progress_data["level"]
    player.progress.current_xp = progress_data["current_xp"]
    player.progress.next_level_xp = progress_data["next_level_xp"]
    player.progress.stat_points = progress_data["stat_points"]
    player.progress.level_up_stat_point = progress_data["level_up_stat_point"]
    
    # بارگذاری موجودی
    dict_to_inventory(player, data["inventory"])
    
    # بارگذاری تجهیزات
    dict_to_equipment(player, data["equipment"])
    
    
    return player


def dict_to_inventory(player, items_data):
    """بارگذاری موجودی از لیست دیکشنری"""
    for item_data in items_data:
        item_type = item_data["type"]
        if item_type == "weapon":
            item = Weapon(
                name=item_data["name"],
                price=item_data["price"],
                weight=item_data["weight"],
                damage_bonus=item_data["damage_bonus"],
                critical_chance=item_data["critical_chance"]
            )
            player.inventory.add_item(item)
        elif item_type == "shield":
            item = Shield(
                name=item_data["name"],
                price=item_data["price"],
                weight=item_data["weight"],
                defence_bonus=item_data["defence_bonus"]
            )
            player.inventory.add_item(item)
        elif item_type == "potion":
            item = Potion(
                name=item_data["name"],
                price=item_data["price"],
                weight=item_data["weight"],
                heal_amount=item_data["heal_amount"]
            )
            player.inventory.add_item(item)


def dict_to_equipment(player, equipment_data):
    """بارگذاری تجهیزات مجهز از دیکشنری"""
    if "weapon" in equipment_data:
        w_data = equipment_data["weapon"]
        weapon = Weapon(
            name=w_data["name"],
            price=w_data["price"],
            weight=w_data["weight"],
            damage_bonus=w_data["damage_bonus"],
            critical_chance=w_data["critical_chance"]
        )
        player.equipment.equip_weapon(weapon)
    
    if "shield" in equipment_data:
        s_data = equipment_data["shield"]
        shield = Shield(
            name=s_data["name"],
            price=s_data["price"],
            weight=s_data["weight"],
            defence_bonus=s_data["defence_bonus"]
        )
        player.equipment.equip_shield(shield)


# ========== توابع اصلی Save و Load ==========

def save_game(player, filename="savegame.json"):
    """ذخیره‌سازی بازی در فایل JSON"""
    try:
        data = player_to_dict(player)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("game saved")
        return True
    except Exception as e:
        print(f" Error while saving : {e}")
        return False


def load_game(filename="savegame.json"):
    """بارگذاری بازی از فایل JSON"""
    if not os.path.exists(filename):
        print("no save file found")
        return None
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        player = dict_to_player(data)
        print("load successful")
        return player
    except Exception as e:
        print(f"loading error : {e}")
        return None


def delete_save(filename="savegame.json"):
    """حذف فایل ذخیره"""
    if os.path.exists(filename):
        os.remove(filename)
        print("save file deleted")
        return True
    print("no save file exist")
    return False


def show_save_info(filename="savegame.json"):
    """نمایش اطلاعات فایل ذخیره (بدون بارگذاری کامل)"""
    if not os.path.exists(filename):
        print("no save file exist")
        return
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        print("save file info:")
        print(f"   player: {data.get('name', 'unknown')}")
        print(f"   progress : {data.get('progress', {}).get('level', 'unknown')}")
        print(f"   Gold : {data.get('gold', 'unknown')}")
        print(f"   items : {len(data.get('inventory', []))}")
        
    except Exception as e:
        print(f"error in reading file : {e}")