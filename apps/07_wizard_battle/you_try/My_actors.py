

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    #  Create the behaviour methods:
    def attack(self, other_creature):
        pass


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level
    # Definition of representation of the created creatures. print()-cmd will return it:
    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )





