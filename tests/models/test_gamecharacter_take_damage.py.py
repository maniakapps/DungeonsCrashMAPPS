import unittest

from models.game_character import GameCharacter


class GameCharacterTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.gc = GameCharacter()

    def test_take_damage(self):
        self.gc.take_damage(20)
        self.assertEqual(35, self.gc.current_health)

    def test_take_damage_exception(self):
        self.assertRaises(TypeError, self.gc.take_damage, bool)

    def test_take_damage_negative(self):
        self.gc.take_damage(-700)
        self.assertEqual(50, self.gc.current_health)