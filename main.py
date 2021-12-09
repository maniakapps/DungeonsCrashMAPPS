from game_character import GameCharacter
from item import Item
from player import Player


def main(*args, **kwargs):
    espada = Item()
    zombie = GameCharacter("Zombie")
    zombie.print_details()
    player = Player("Manuel", 100)
    player.print_details()


if __name__ == '__main__':
    main()
