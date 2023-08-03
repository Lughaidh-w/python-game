from thing import Thing

class Bug(Thing):
    def __init__(self, name):#, species, legs, can_fly):
        super().__init__(name)
        #self.species = species
        #self.legs = legs
        #self.can_fly = can_fly