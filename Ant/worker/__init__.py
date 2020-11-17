from . import walk_interface, turn_interface, rest, get_location, get_status

class Worker:
    def __init__(self):
        self.current_location = [15, 12]
        self.facing = "north"
        self.endurance = 100
        self.hunger = 0
        self.health = 100

    walk_interface = walk_interface.walk_interface
    turn_interface = turn_interface.turn_interface
    rest = rest.rest
    location = get_location.get_location
    status = get_status.get_status

