from thing import Thing
from chatlog import ChatLog
import random

race_list = ["Human", "Elf", "Dwarf"]

class_list = ["Warrior", "Rogue", "Duelist"]


class Humanoid(Thing):
    def race_select(self):
        race = random.choice(race_list)
        return race
    
    def class_select(self):
        type = random.choice(class_list)
        return type


    def __init__(self, name):
        super().__init__(name)
        self.race = self.race_select()
        self.type = self.class_select()
        
        text = f"A {self.race} {self.type} named {self.name} joined the party"
        chat_instance = ChatLog()
        chat_instance.speak(text)

    def __str__(self):
            return f"{self.name}, a {self.race} {self.type}"




