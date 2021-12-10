from dataclasses import dataclass
from source.interfaces.details import PrintDetails


@dataclass
class GameCharacter(PrintDetails):
    """Models a GameCharacter object"""
    name: str = ""
    __current_health: int = 50
    attack: int = 10
    defence: int = 5

    def take_damage(self, amount: int):
        """Handles the damage taken
        if there is a negative amount it sets the damage to 0
        :param amount: amount of damage taken
        i.e take_damage(10)"""
        if isinstance(amount, (int, float)):
            damage = amount - self.defence
            if damage < 0:
                damage = 0
            self.current_health -= damage
        else:
            raise TypeError("Only numbers are allowed.")

    def check_is_dead(self) -> bool:
        """Checks  a game character is dead
        :return: a boolean value when the character is dead"""
        return self.current_health <= 0

    def print_details(self):
        """Prints the game character properties"""
        print(self.name, "Stats")
        print("Current health:", self.current_health)
        print("Current attack:", self.attack)
        print("Current defence:", self.defence)

    @property
    def current_health(self):
        return self.__current_health

    @current_health.setter
    def current_health(self, c_h):
        self.__current_health = c_h

    @current_health.getter
    def current_health(self):
        return self.__current_health
