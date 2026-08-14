from characters import Enemy
from items import Weapon, Shield, Potion
from skills import Attack , Miss , Heavyattack , Heal , CriticalAttack , PoisonAttack,StunAttack,BurnAttack
import random

def create_slime():
    loot = [
        Potion("Small Potion", 20, 2, 30),
        Potion("Small Potion", 20, 2, 30),
        None
    ]
    skills = [
        Attack('Normal Attack'),
        Miss('Miss'),
    ]
    return Enemy(
        "Slime",
        40,
        5,
        10,
        8,
        random.choice(loot),
        skills,
        0.2
    )


def create_goblin():
    loot = [
        Potion("Small Potion", 20, 2, 30),
        Potion("Medium Potion", 45, 3, 70),
        Shield("Light Shield", 10, 2, 7),
        None
    ]
    skills = [
        Attack('Normal Attack'),
        Miss('Miss'),
    ]
    return Enemy(
        "Goblin",
        80,
        10,
        30,
        20,
        random.choice(loot),
        skills,
        0.25
    )


def create_wolf():
    loot = [
        Potion("Small Potion", 20, 2, 30),
        Weapon("Dagger", 25, 1, 5, 0.01),
        None
    ]
    skills=[
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
    ]
    return Enemy(
        "Wolf",
        70,
        16,
        25,
        18,
        random.choice(loot),
        skills,
        0.3
    )


def create_skeleton():
    loot = [
        Shield("Light Shield", 10, 2, 7),
        Weapon("Old Sword", 35, 2, 7, 0.01),
        None
    ]
    skills=[
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
    ]      
    return Enemy(
        "Skeleton",
        90,
        12,
        40,
        25,
        random.choice(loot),
        skills,
        0.32
    )


def create_bandit():
    loot = [
        Weapon("Sword", 50, 2, 10, 0.01),
        Potion("Medium Potion", 45, 3, 70),
        None
    ]
    skills=[
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heal('self Heal'),
        PoisonAttack('Poison Attack')
    ]    
    return Enemy(
        "Bandit",
        120,
        20,
        100,
        40,
        random.choice(loot),
        skills,
        0.35
    )


def create_orc():
    loot = [
        Weapon("Sword", 50, 2, 10, 0.01),
        Weapon("Bow", 80, 3, 15, 0.02),
        Shield("Normal Shield", 15, 3, 10),
        None
    ]
    skills=[
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heal('self Heal'),
        Heavyattack('heavy Attack'),
        StunAttack('Stun Attack')
    ]    
    return Enemy(
        "Orc",
        140,
        18,
        80,
        45,
        random.choice(loot),
        skills,
        0.25
    )


def create_dark_mage():
    loot = [
        Potion("Mega Potion", 100, 4, 150),
        Weapon("Magic Staff", 120, 3, 20, 0.03),
        None
    ]
    skills=[
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heal('self Heal'),
        StunAttack('Stun Attack'),
        BurnAttack('Burn Attack'),
        PoisonAttack('Poison Attack')
    ]    
    return Enemy(
        "Dark Mage",
        110,
        28,
        130,
        50,
        random.choice(loot),
        skills,
        0.4
    )


def create_troll():
    loot = [
        Shield("Heavy Shield", 22, 4, 15),
        Weapon("War Hammer", 140, 5, 30, 0.02),
        None
    ]
    skills=[
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heavyattack('heavy Attack'),
        StunAttack('Stun Attack')
    ]  
    return Enemy(
        "Troll",
        250,
        25,
        180,
        70,
        random.choice(loot),
        skills,
        0.35
    )


def create_vampire():
    loot = [
        Weapon("Blood Blade", 180, 3, 35, 0.05),
        Potion("Mega Potion", 100, 4, 150),
        None
    ]
    skills =[    
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heal('self Heal'),
        PoisonAttack('Poison Attack'),
        StunAttack('Stun Attack')
    ] 
    return Enemy(
        "Vampire",
        180,
        35,
        250,
        90,
        random.choice(loot),
        skills,
        0.4
    )


def create_demon():
    loot = [
        Weapon("Hell Axe", 220, 5, 40, 0.05),
        Shield("Demon Shield", 80, 4, 20),
        ]
    skills =[    
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heal('self Heal'),
        Heavyattack('heavy Attack'),
        BurnAttack('Burn Attack')
    ] 
    return Enemy(
        "Demon",
        280,
        40,
        400,
        120,
        random.choice(loot),
        skills,
        0.45
    )


def create_dragon():
    loot = [
        Weapon("Dragon Slayer", 350, 6, 55, 0.08),
        Potion("Mega Potion", 100, 4, 150),
        Shield("Dragon Scale Shield", 150, 5, 30)
    ]
    skills =[    
        Attack('Normal Attack'),
        Miss('Miss'),
        CriticalAttack('Crit Attack'),
        Heal('self Heal'),
        Heavyattack('heavy Attack'),
        BurnAttack('Burn Attack'),
        StunAttack('Stun Attack')
    ] 
    return Enemy(
        "Dragon",
        350,
        45,
        500,
        150,
        random.choice(loot),
        skills,
        0.5
    )
enemy_pool = [
    create_slime,
    create_goblin,
    create_wolf,
    create_skeleton,
    create_bandit,
    create_orc,
    create_dark_mage,
    create_troll,
    create_vampire,
    create_demon,
    create_dragon
]
def enemy():
    selected = random.sample(enemy_pool,k=3)
    return [enemy() for enemy in selected]

