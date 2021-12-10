from unittest import TestCase
from source.models.item import Item


class TestItemClass(TestCase):
    def setUp(self) -> None:
        self.item = Item()

    def test_default_constructor(self):
        self.assertEqual("Espada", self.item.name)
        self.assertEqual(0, self.item.health)
        self.assertEqual(10, self.item.attack)
        self.assertEqual(0, self.item.defence)

    def test_parameterized_constructor(self):
        self.item = Item("Martillo", 0, 15, 0)
        self.assertEqual("Martillo", self.item.name)
        self.assertEqual(0, self.item.health)
        self.assertEqual(15, self.item.attack)
        self.assertEqual(0, self.item.defence)

