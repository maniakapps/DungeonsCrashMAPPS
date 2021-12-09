from game_character import GameCharacter
from item import Item
from dataclasses import dataclass


@dataclass
class Room:
    position: int
    is_exit: bool
    items: list
    enemies: list

    def clear_loot(self):
        """ Clear all the loot in the room """
        self.items.clear()

    def clear_enemies(self):
        """ Clear enemies in the room"""
        self.enemies.clear()

    Item = Item

    def add_item(self, item: Item):
        """Adds an intem to the room if the item passed is an Item object, otherwise it raises an exception
        :parameter item an Item object """
        if isinstance(item, Item):
            # agrega el objeto a la lista de objetos
            self.items.append(item)
        else:
            raise ValueError

    GameCharacter = GameCharacter

    def add_enemy(self, enemy: GameCharacter):
        """Adds an enemy into the room only if it is an objet
        otherwise raises an error
        :parameter enemy Game character object
        """
        if isinstance(enemy, GameCharacter):
            self.items.append(enemy)
        else:
            raise ValueError

    def get_items(self) -> list:
        """get items in the objects list
        :return a list of items
        """
        return self.items
