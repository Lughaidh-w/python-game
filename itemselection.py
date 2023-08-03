import random
from item import Item


class itemselection(Item):
    def __init__(self):
        pass

    def random_item(self):
        test = input()
        randomItem = Item(test)
   