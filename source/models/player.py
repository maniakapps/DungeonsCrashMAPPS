from dataclasses import dataclass, field
from source.interfaces.details import PrintDetails
from source.models.item import Item
from source.models.game_character import GameCharacter
from source.models.room import Room


@dataclass
class Player(GameCharacter, PrintDetails):
    name: str = ""
    __current_health: int = 50
    attack: int = 10
    defence: int = 5
    inventory: list[Item] = field(default_factory=list)
    daga: Item = Item("Daga", 0, 10, 0)
    current_room: Room = field(init=False, repr=False)
    previous_room: Room = field(init=False, repr=False)

    def __post_init__(self):
        self.inventory.append(self.daga)

    def increase_stats(self, health, attack, defence):
        self.current_health += health
        self.attack += attack
        self.defence += defence

    def add_item(self, item):
        self.inventory.append(item)
        self.increase_stats(item.health, item.attack, item.defence)

    def loot_room(self, room):
        items = room.get_items()
        for item in items:
            self.add_item(item)

    def change_room(self, new_room):
        self.previous_room = self.current_room
        self.current_room = new_room

    def print_details(self):
        super(Player, self).print_details()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nm):
        self.__name = nm


    def read_name(self):
        self.name = input("Enter your name: ")