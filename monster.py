from thing import Thing
from chatlog import ChatLog
from element import Element
import random

monster_type = ["Dragon"]



class Monster(Thing):
    def monster_select(self):
        monster = random.choice(monster_type)
        return monster
    


    def __init__(self, name):
        super().__init__(name)
        self.type = self.monster_select()
        elem = Element()
        self.ele = elem.ele


        
        text = f"A {self.ele} {self.type} named {self.name} spawned in the dungeon"
        chat_instance = ChatLog()
        chat_instance.speak(text)

    def __str__(self):
            return f"{self.name}, a {self.race} {self.type}"




