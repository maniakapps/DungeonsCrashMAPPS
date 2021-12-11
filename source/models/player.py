from dataclasses import dataclass, field
from source.interfaces.details import PrintDetails
from source.models.item import Item
from source.models.game_character import GameCharacter
from source.models.room import Room


@dataclass
class Player(GameCharacter, PrintDetails):
    """ A player class model"""
    name: str = ""
    __current_health: int = 50
    attack: int = 10
    defence: int = 5
    inventory: list[Item] = field(default_factory=list)
    daga: Item = Item("Daga", 0, 10, 0)
    current_room: Room = field(init=False, repr=False)
    previous_room: Room = field(init=False, repr=False)

    def __post_init__(self):
        """This method initializes the first item in the player inventory"""
        self.inventory.append(self.daga)

    def increase_stats(self, health: int | float, attack: int | float, defence: int | float):
        """Increases the player stats
        :param health the health to increase
        :param attack the attck to increase
        :param defence the defence to increase """
        self.current_health += health
        self.attack += attack
        self.defence += defence

    def add_item(self, item: Item):
        """Adds a new item to the player inventory
        :param item the item to add to the inventory"""
        self.inventory.append(item)
        self.increase_stats(item.health, item.attack, item.defence)

    def loot_room(self, room: Room):
        """add the items in the room to the player's inventory
        :param room the room you are in"""
        items = room.get_items()
        for item in items:
            self.add_item(item)

    def change_room(self, new_room: Room):
        """ puts the player in a new room
        :param new_room the room to move to"""
        self.previous_room = self.current_room
        self.current_room = new_room

    def print_details(self):
        """ prins the player details"""
        super(Player, self).print_details()

    @property
    def name(self) -> str:
        """ Player's name getter
        :return player's name"""
        return self.__name

    @name.setter
    def name(self, nm: str):
        """player's name setter
        :param nm the player's name to be set"""
        self.__name = nm

    def read_name(self):
        """Ask the user for a name"""
        self.name = input("Enter your name: ")
