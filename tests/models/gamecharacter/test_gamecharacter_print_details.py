import unittest

import pytest as pytest

from source.models.game_character import GameCharacter


class GameCharacterTestSuite(unittest.TestCase):
    """Suite to test the Game Character print_Details() method"""

    def setUp(self) -> None:
        """Sets up an object for testing
        :return None"""
        self.gc = GameCharacter(name="Manuel")

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        """This method captures the print details output"""
        self.capsys = capsys

    def test_print_details(self):
        """Tests the print_details() game character method"""
        self.gc.print_details()
        captured = self.capsys.readouterr()
        self.assertEqual("Manuel Stats\nCurrent health: 50\nCurrent attack: 10\nCurrent defence: 5\n", captured.out)