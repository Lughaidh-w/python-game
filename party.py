from partymember import PartyMember
from humanoid import Humanoid
import random


name_list = ["Aqulieus", "Erogon", "Faelora", "Draven", "Lysandra", "Thalgrim",
             "Seraphina", "Grimwald", "Aurelius", "Lythalia", "Zephyrion", "Thorn",
             "Valeria", "Mordred", "Elowen", "Aurelia", "Thundar", "Nyxia", "Gareth",
             "Lorelei", "Xander", "Ravenna", "Cassius", "Isolde", "Aranthir", "Zara",
             "Cedric", "Evangeline", "Vaelin", "Anastasia", "Gideon", "Elara", "Caelum",
             "Zariah", "Kaelan", "Astrid", "Vesper", "Ishtar", "Eldric", "Aurora",
             "Vaelora", "Zephyra", "Kieran", "Esmeralda", "Eamon", "Selene", "Isolde",
             "Zephyrus", "Thalia", "Oberon", "Vivienne", "Luna", "Sylvan", "Sorcha",
             "Cyrus", "Rowena", "Elowyn", "Vance", "Myrina", "Celestia", "Cassian",
             "Thalia", "Evander", "Maeve", "Aurora", "Caelan", "Lyanna", "Cedric",
             "Valeria", "Thorn", "Eowyn", "Aurelius", "Seraphina", "Zephyrion",
             "Cassandra", "Lysander", "Gwyneth", "Eamon", "Isolde", "Ravenna", "Caelum",
             "Aranthir", "Lorelei", "Thundar", "Evangeline", "Vaelin", "Elara", "Cedric",
             "Anastasia", "Gideon", "Zara", "Vesper", "Ishtar", "Eldric", "Aurora",
             "Vaelora", "Zephyra", "Kieran", "Esmeralda", "Eamon", "Selene", "Isolde",
             "Zephyrus", "Thalia", "Oberon", "Vivienne", "Luna", "Sylvan", "Sorcha",
             "Cyrus", "Rowena", "Elowyn", "Vance", "Myrina", "Celestia", "Cassian"]


class Party:
    def party_size(self):
        return 3
    
    def party_populate(self, partySize):
        party_members = []
        for _ in range(partySize):
            name = random.choice(name_list) 
            party_members.append(Humanoid(name))
        return party_members

    
    def __init__(self, name):
        self.name = name
        self.partySize = self.party_size()
        self.members = self.party_populate(self.partySize)










    
    