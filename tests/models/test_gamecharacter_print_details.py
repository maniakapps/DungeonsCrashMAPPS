import unittest

import pytest as pytest

from models.game_character import GameCharacter


class GameCharacterTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.gc = GameCharacter(name="Manuel")

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_print_details(self):
        self.gc.print_details()
        captured = self.capsys.readouterr()
        self.assertEqual("Manuel Stats\nCurrent health: 50\nCurrent attack: 10\nCurrent defence: 5\n", captured.out)