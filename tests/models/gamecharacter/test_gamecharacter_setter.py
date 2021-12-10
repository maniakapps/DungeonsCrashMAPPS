import unittest

from source.models.game_character import GameCharacter


class TestSetter(unittest.TestCase):
    """Suite to test the Game Character setter and getter methods"""
    def setUp(self) -> None:
        """Sets up an object for testing"""
        self.gc = GameCharacter()

    def test_current_health_setter(self):
        """Tests the current health using the setter and getter"""
        self.gc.current_health = 300
        self.assertEqual(300, self.gc.current_health)

