import unittest

from source.models.game_character import GameCharacter


class TestSetter(unittest.TestCase):
    def setUp(self) -> None:
        self.gc = GameCharacter()

    def test_current_health_setter(self):
        self.gc.current_health = 300
        self.assertEqual(300, self.gc.current_health)

