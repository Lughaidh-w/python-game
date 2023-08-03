from thing import Thing
from chatlog import ChatLog
from home import Home
from areaselection import AreaSelection
from monster import Monster
from monsterselection import MonsterSelection
from party import Party
import random


biome_list = ["forest", "mountain", "grassland", "swamp", "wasteland"]
# desert, canyon, cave, meadow, snowy plain etc.

camp_type = ["tent", "wagon"]

# make home
random_biome = random.choice(biome_list)
random_camp = random.choice(camp_type)
home = Home(random_biome, random_camp)






while True: 
    # Select Dungeon
    #print("SYS MSG: Select Dungeon Entrance")
    print("\n\n")
    areaInput = input()
    area = AreaSelection.type_cave(areaInput)
    msg = f"Arrived at {area} Dungeon area, there is noone around."

    # Select monsters
    #print("SYS MSG: Select Monsters")
    monster = Monster("Krug")
    #monsters = MonsterSelection.type_monster(monsterInput)

    # Select Incoming party
    #print("SYS MSG: Select Party")
    print("Party Size = 3")
    party = Party("New Party")
    print("Party Members:")
    for member in party.members:
        print(member)

    # Select Items
    print("Crafted Items:")
    items = ["Fire Ward", "Air Ward", "Earth Ward", "Water Ward"]
    print(items)
    
    # Sell/Give items
    print("The party approaches, they would like to buy some of your stocks for the encounter")
    soldItem = input("Which item to give them: ")

    # Encounter
    print("The party has accepted your offering")
    print(f"{party.members[0].name} the {party.members[0].type} thanks you.")
    print("The party enters the dungeon and the encounter begins")
    if monster.ele == soldItem.split()[0]:
        print(f"{monster.name} the ferocious {monster.type} blasts the party with its {monster.ele} attack")
        print(f"The party uses the fake {soldItem}, the blast engulfs the party.")
        print("There are no survivors")
    else:
        print(f"{monster.name} the ferocious {monster.type} blasts the party with its {monster.ele} attack")
        print("The party focuses on defence and strategy")
        print("The battle continues")

    # Outcome


