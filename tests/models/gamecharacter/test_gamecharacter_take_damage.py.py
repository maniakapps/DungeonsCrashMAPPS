import unittest

from source.models.game_character import GameCharacter


class GameCharacterTestSuite(unittest.TestCase):
    """Suite to test the Game Character take_damage() method"""
    def setUp(self) -> None:
        """Sets up an object for testing"""
        self.gc = GameCharacter()

    def test_take_damage(self):
        """Test the take damage with a positive value"""
        self.gc.take_damage(20)
        self.assertEqual(35, self.gc.current_health)

    def test_take_damage_exception(self):
        """Tests the exception when a number is not entered"""
        self.assertRaises(TypeError, self.gc.take_damage, bool)

    def test_take_damage_negative(self):
        """Test the take damage with negative numbers"""
        self.gc.take_damage(-700)
        self.assertEqual(50, self.gc.current_health)