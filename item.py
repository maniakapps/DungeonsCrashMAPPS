from dataclasses import dataclass


@dataclass
class Item:
    """Models an Item object Item(name, health, attack, defence)
        example: Item("Sword", 50, 10, 5)"""
    name: str = "Espada"
    health: int = 0
    attack: int = 10
    defence: int = 0
