from .util import set_attributes

class Attacks:
    def __init__(self, name, damage_amount, description, endurance_cost):
        self.name = name
        self.damage_amount = damage_amount
        self.description = description
        self.endurance_cost = endurance_cost

        set_attributes(self, name=name, damage_amount=damage_amount, description=description, endurance_cost=endurance_cost)


