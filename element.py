import random

element_list = ["Fire", "Water", "Air", "Earth"]

class Element:
    def __init__(self):
        self.ele = random.choice(element_list)

