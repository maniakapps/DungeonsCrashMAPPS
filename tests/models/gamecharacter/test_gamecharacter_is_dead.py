import unittest

from source.models.game_character import GameCharacter


class GameCharacterTestSuite(unittest.TestCase):
    """Suite to test the Game Character check_is_dead() method"""
    def setUp(self) -> None:
        """Sets up an object for testing"""
        self.gc = GameCharacter()

    def test_check_is_dead(self):
        """Checks if the gm character is dead"""
        self.gc.take_damage(200)
        self.assertEqual(True, self.gc.check_is_dead())

    def test_check_is_dead_false(self):
        """tests if the game character is not dead"""
        self.gc.take_damage(0)
        self.assertEqual(False, self.gc.check_is_dead())

