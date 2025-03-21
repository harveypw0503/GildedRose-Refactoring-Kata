# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            quality_change = -1  
            
            if item.name == "Aged Brie":
                quality_change = 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0
                    item.sell_in -= 1
                    continue
                elif item.sell_in < 6:
                    quality_change = 3
                elif item.sell_in < 11:
                    quality_change = 2
                else:
                    quality_change = 1

            item.quality = max(0, min(50, item.quality + quality_change))

            item.sell_in -= 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    item.quality = min(50, item.quality + 1)
                elif item.quality > 0:
                    item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
