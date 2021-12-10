from abc import ABC

from interfaces.details import PrintDetails
from models.game_character import GameCharacter
from models.player import Player
from dataclasses import dataclass, field
from models.room import Room


@dataclass(kw_only=True)
class Dungeon(PrintDetails, ABC):
    player: Player
    number: int
    rooms: []

    def print_actions(self, actions: list):
        print("Seleccione una acccion: ")
        for action in actions:
            print(action)

    def run_dungeon(self):
        print("Bienvenido al dungeon: ", self.number, "! ", self.player.name, "dentro encontrarás tesoros , pero "
                                                                              "tambien enemigos. \n Entra bajo tu "
                                                                              "propio riesgo")
        self.player.print_details()
        self.player.current_room = self.rooms[0]
        self.player.previous_room = self.rooms[0]
        while True:
            self.enter_room(self.player.current_room)
            if self.player.check_is_dead():
                print("El juego ha terminado, ¿intentar de nuevo?")
                return self.perform_end_logic()
            else:
                if self.player.current_room.is_exit:
                    if self.player.current_room.is_empty():
                        print("¡Ganaste! ¿Jugar de nuevo?")
                        return self.perform_end_logic()

            self.handle_movement_actions(self.player.current_room)

    def handle_room_with_enemy(self, room):
        enemy = room.enemies[0]
        print("Entraste a la habitación y ves un ", enemy.name)
        for item in room.items:
            self.player.increase_stats(item.health, item.attack, item.defence)
            print("Abriste un cofre y encontraste:", item.name)
            self.player.print_details()
        room.clear_loot()

    def enter_room(self, room: Room):
        if len(room.enemies) > 0:
            self.handle_room_with_enemy(room)
        elif len(room.items) > 0:
            self.handle_room_with_chest(room)
        else:
            self.handle_empty_room(room)

    def handle_room_with_chest(self, room):
        print("Entraste en una habitación donde hay un cofre en medio de la misma.")
        actions = ["a. Abrir el cofre.", "b. Moverse a otra habitación."]
        while True:
            self.print_actions(actions)
            read = input()
            if read == 'a':
                self.handle_loot_actions(room)
                return
            elif read == 'b':
                return
            else:
                print("Opcion incorrecta")

    def handle_empty_room(self, room):
        print("Entraste a una habitación vacia.")
        actions = list(
            "a. Moverse a otra habitación"
        )
        while True:
            self.print_actions(actions)
            read = input()
            if read == 'a':
                return
            else:
                print("Opcion incorrecta")

    def perform_end_logic(self):
        actions = ["a. Si",
                   "b. No"]
        while True:
            self.print_actions(actions)
            read = input()
            if read == 'a':
                return 1
            elif read == 'b':
                return 0
            else:
                print("Opcion incorrecta.")

    def handle_fight_actions(self, enemy: GameCharacter):
        actions = ["a. Atacar",
                   "b. Escapar"]
        while True:
            self.print_actions(actions)
            read = input()
            if read == 'a':
                damage = enemy.take_damage(self.player.attack)
                print("Tus ataques inflingieron ", damage, " de daño.")
                enemy.print_details()
            elif read == 'b':
                self.player.change_room(self.player.previous_room)
                self.enter_room(self.player.current_room)
                return
            else:
                print("Opcion incorrecta.")
                continue

            if enemy.check_is_dead():
                print("Haz ganado! derrotaste al monstruo ", enemy.name)
                self.player.increase_stats(10, 5, 5)
                self.player.current_room.clear_enemies()
                return

            damage = self.player.take_damage(enemy.attack)
            print(enemy.name, " inflingio ", damage, " de daño.")
            print("Ahora tienes ", self.player.current_health, " puntos de vida.")
            enemy.print_details()
            if self.player.check_is_dead():
                return

    def handle_loot_actions(self, room):
        self.player.loot_room(room)
        for item in room.items:
            self.player.increase_stats(item.health, item.attack, item.defence)
            print("Abriste un cofre y encontraste: ", item.name)
            self.player.print_details()
        room.clear_loot()

    def handle_movement_actions(self, room):
        while True:
            if room.position > 0:
                actions = ["a. Moverse a la derecha",
                           "b. Mover hacia abajo"]
                self.print_actions(actions)

                read = input()
                if read == 'a':
                    self.player.change_room(self.rooms[1])
                    return
                elif read == 'b':
                    self.player.change_room(self.rooms[2])
                    return
                else:
                    print("Opcion incorrecta.")
            elif room.position == 1:
                actions = ["a. Moverse a la izquierda"]
                self.print_actions(actions)
                read = input()
                if read == 'a':
                    self.player.change_room(self.rooms[0])

            elif room.position == 2:
                actions = ["a. Moverse hacia arriba",
                           "b. Mover hacia la derecha"]
                self.print_actions(actions)
                read = input()
                if read == 'a':
                    self.player.change_room(self.rooms[0])
                    return
                elif read == "b":
                    self.player.change_room(self.rooms[3])

                else:
                    print("Opción incorrecta")
            else:
                actions = ["a. Moverse a la izquierda"]
                self.print_actions(actions)
                read = input()
                if read == "a":
                    self.player.change_room(self.rooms[2])
                    return
                else:
                    print("Opcion incorrecta")
