import unittest

from models.game_character import GameCharacter


class GameCharacterTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.gc = GameCharacter()

    def test_check_is_dead(self):
        self.gc.take_damage(200)
        self.assertEqual(True, self.gc.check_is_dead())

    def test_check_is_dead_false(self):
        self.gc.take_damage(0)
        self.assertEqual(False, self.gc.check_is_dead())

