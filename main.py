from source.models.dungeon import Dungeon
from source.models.game_character import GameCharacter
from source.models.item import Item
from source.models.player import Player
from source.models.room import Room


def main(*args, **kwargs):
    name: str = input("Introduce tu nombre: ")
    player: Player = Player(name, 100, 20, 10)
    room: Room = Room(0, False, [Item], [GameCharacter])
    sword = Item("Espada", 0, 20, 0)
    casco = Item("Casco", 0, 0, 10)
    second_room_items_list = [sword, casco]
    second_room = Room(1, False, second_room_items_list, [GameCharacter])

    first_enemy = GameCharacter("Zombie", 50, 15, 5)
    third_room_enemies = [first_enemy]
    third_room = Room(2, False, [Item], third_room_enemies)

    second_enemy = GameCharacter("Gran Zombie", 100, 20, 10)
    fourth_room_enemies_list = [second_enemy]
    fourth_room = Room(3, False, [Item], fourth_room_enemies_list)

    initial_boss = GameCharacter("Mountruo fuerte inicial", 140, 100, 80);
    fifth_room_enemies = [initial_boss]
    fifth_room = Room(4, False, [Item], fifth_room_enemies)

    final_boss = GameCharacter("Jefe final", 4000, 150, 200)
    sixth_room_enemies = [final_boss]
    sixth_room = Room(5, True, [Item], sixth_room_enemies)

    first_dungeon = Dungeon(player=player, number=1, rooms=[0, 0, 0, 0, 0, 0])
    first_dungeon.rooms[0] = room
    first_dungeon.rooms[1] = second_room
    first_dungeon.rooms[2] = third_room
    first_dungeon.rooms[3] = fourth_room
    first_dungeon.rooms[4] = fifth_room
    first_dungeon.rooms[5] = sixth_room

    second_dungeon = Dungeon(player=player, number=2, rooms=[0, 0, 0, 0, 0, 0])
    second_dungeon.rooms[0] = room
    second_dungeon.rooms[1] = second_room
    second_dungeon.rooms[2] = third_room
    second_dungeon.rooms[3] = fourth_room
    second_dungeon.rooms[4] = fifth_room
    second_dungeon.rooms[5] = sixth_room

    while True:
        print("Eliga una dungueon: 1, 2 o escriba 3 para salir: ")
        result: int = 0
        dung_selection: int = int(input())
        if dung_selection == 1:
            result = first_dungeon.run_dungeon()
            if result == 0:
                print("Adios")
            break
        elif dung_selection == 2:
            result = second_dungeon.run_dungeon()
            if result == 0:
                print("Adios")
                break
        else:
            print("Adios")
            break


if __name__ == '__main__':
    print("Bienvenido a ManiakApps RPG")
    main()
