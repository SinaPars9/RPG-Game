# RPG Battle Game

A command-line RPG battle game built with Python, focused on Object-Oriented Programming, modular system design, and game mechanics.

The player takes the role of an adventurer who fights different enemies, earns experience and gold, upgrades their character, manages equipment, and progresses through increasingly difficult battles.

## Features

* **Turn-Based Combat** — Player and enemies take turns attacking
* **11 Enemy Types** — Slime, Goblin, Wolf, Skeleton, Bandit, Orc, Dark Mage, Troll, Vampire, Demon, and Dragon
* **Enemy Skills** — Heavy attacks, critical attacks, healing, poison attacks, stun attacks, fire attacks, and more
* **Status Effects** — Poison, stun, and burn with periodic damage
* **Cooldown System** — Special abilities have cooldowns
* **Leveling System** — Gain experience and level up
* **Stat Points** — Earn upgrade points when leveling up
* **Inventory System** — Manage items with weight and quantity limits
* **Equipment System** — Equip and switch between different weapons and shields
* **Shop System** — Buy weapons, shields, and potions
* **Loot System** — Enemies can drop valuable items
* **Random Rewards** — Battles can provide different rewards
* **Command-Line Interface** — The entire game runs directly in the terminal

## Gameplay

The player can perform actions such as:

```text
1. Show status
2. Show inventory
3. Use item
4. Level up
5. Shop
6. Fight
7. Exit
```

During combat, the player and enemy attack each other in turns.

Enemies can use different abilities depending on their type, while the player can use items, manage equipment, and improve their character through the progression system.

After defeating an enemy, the player receives experience and gold, and may also receive loot.

## Game Systems

### Combat

The combat system is turn-based. Each battle involves the player and an enemy taking actions in sequence.

Enemies can perform different types of attacks and abilities, including:

* Normal attacks
* Heavy attacks
* Critical attacks
* Healing
* Poison attacks
* Stun attacks
* Fire attacks

### Status Effects

Some abilities can apply status effects to the player.

Currently supported effects include:

* Poison
* Stun
* Burn

These effects can cause additional damage or affect the player's actions during combat.

### Character Progression

Players gain experience from battles.

When enough experience is collected, the character can level up and receive stat points that can be used for further progression.

### Inventory

The inventory system manages the player's items.

Items are limited by:

* Weight
* Quantity

This adds resource management to the gameplay.

### Equipment

Players can obtain and equip different weapons and shields.

Equipment affects the character's combat capabilities and can be purchased from the shop.

### Shop

The shop allows players to purchase:

* Weapons
* Shields
* Potions

Gold earned from battles can be used to improve the player's equipment and resources.

### Loot

Enemies can drop valuable items after being defeated.

Loot and battle rewards introduce an element of randomness to progression.

## Project Structure

```text
RPG-Game/
│
├── main.py
├── characters.py
├── items.py
├── inventory.py
├── equipments.py
├── shop.py
├── fight.py
├── skills.py
├── effects.py
├── enemy_data.py
├── stat_points.py
└── todo.md
```

### Main Components

**`main.py`**

Entry point of the game and main menu.

**`characters.py`**

Contains character-related classes, including the player, enemies, and progression logic.

**`items.py`**

Defines item-related classes such as weapons, shields, and potions.

**`inventory.py`**

Handles the player's inventory and its limitations.

**`equipments.py`**

Manages equipped weapons and shields.

**`shop.py`**

Implements the in-game shop and purchasing system.

**`fight.py`**

Contains the main combat logic.

**`skills.py`**

Defines enemy skills and special abilities.

**`effects.py`**

Handles status effects such as poison, stun, and burn.

**`enemy_data.py`**

Contains data for the game's different enemy types.

**`stat_points.py`**

Handles character upgrades and stat points received through leveling.

## Requirements

* Python 3.8+
* No external Python packages are required

The game uses only Python's standard library.

## Installation

Clone the repository:

```bash
git clone https://github.com/SinaPars9/RPG-Game.git
cd RPG-Game
```

## Running the Game

Run the main file:

```bash
python main.py
```

The game will start in the terminal and display the main menu.

## Project Goals

This project was built as a hands-on Python project to practice:

* Python fundamentals
* Object-Oriented Programming
* Classes and inheritance
* Modular application design
* Managing interactions between multiple systems
* Data structures
* Game logic
* State management
* Randomized game mechanics
* Designing larger Python projects

The project gradually evolved from a simple RPG concept into a multi-module system containing combat, inventory, equipment, skills, status effects, progression, shops, and loot.

## Future Improvements

Possible future improvements include:

* Expanding the combat system
* Adding more enemies and abilities
* Improving game balance
* Expanding the equipment and item systems
* Improving the progression system
* Adding save/load functionality
* Adding more gameplay events and mechanics
* Further refactoring and modularization

## License

This project is licensed under the MIT License.

```
```
