import unittest
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, 1)

    def test_backstage_passes_increase_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 10)

    def test_regular_item_decreases_in_quality(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)
        self.assertEqual(items[0].sell_in, 4)

if __name__ == '__main__':
    unittest.main()
