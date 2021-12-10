from unittest import TestCase
from source.models.item import Item


class TestItemClassRaise(TestCase):
    """A suite to test the exceptions in Item class"""
    def setUp(self) -> None:
        """Sets up an object for testing"""
        self.item = Item()

    def test_raise_name(self):
        """Tests the raise exception with the name"""
        self.item = Item(34, 4, 6, 6)
        self.assertRaises(TypeError, self.item)

    def test_raise_health(self):
        """Tests the raise exception with the health"""
        self.item = Item("Espada", "4", 6, 6)
        self.assertRaises(TypeError, self.item)

    def test_raise_attack(self):
        """Tests the raise exception with the attack"""
        self.item = Item("Espada", 4, "6", 6)
        self.assertRaises(TypeError, self.item)

    def test_raise_defence(self):
        """Tests the raise exception with the defence"""
        self.item = Item("Espada", 4, 6, "6")
        self.assertRaises(TypeError, self.item)