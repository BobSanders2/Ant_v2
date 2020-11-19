from . import walk_interface, turn_interface, rest, get_location, get_status

class Worker:
    def __init__(self, char_stats):
        self.current_location = [0, 12]
        self.facing = "north"
        self.char_stats = char_stats

    run_away = walk_interface.run_away
    walk = walk_interface.walk_interface
    turn_interface = turn_interface.turn_interface
    location = get_location.get_location
    status = get_status.get_status
    rest = rest.rest

