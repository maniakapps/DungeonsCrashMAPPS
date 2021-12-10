from unittest import TestCase
from source.models.game_character import GameCharacter


class TestGameCharacterClass(TestCase):
    """Suite to test the Game Character class"""
    def setUp(self) -> None:
        """ Sets the gc object with a few parameters"""
        self.gc = GameCharacter("Angel", 120, 54, 89)

    def test_object_name(self):
        """tests the gc object name"""
        self.assertEqual("Angel", self.gc.name)

    def test_object_attack(self):
        """Tests the gc object attack"""
        self.assertEqual(54, self.gc.attack)

    def test_object_current_health(self):
        """Tests the gc object current health"""
        self.assertEqual(120, self.gc.current_health)

    def test_object_defence(self):
        """tests the gc defence"""
        self.assertEqual(89, self.gc.defence)
