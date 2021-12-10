from unittest import TestCase
from source.models.item import Item


class TestItemClassRaise(TestCase):
    def setUp(self) -> None:
        self.item = Item()

    def test_raise_name(self):
        self.item = Item(34, 4, 6, 6)
        self.assertRaises(TypeError, self.item)

    def test_raise_health(self):
        self.item = Item("Espada", "4", 6, 6)
        self.assertRaises(TypeError, self.item)

    def test_raise_attack(self):
        self.item = Item("Espada", 4, "6", 6)
        self.assertRaises(TypeError, self.item)

    def test_raise_defence(self):
        self.item = Item("Espada", 4, 6, "6")
        self.assertRaises(TypeError, self.item)