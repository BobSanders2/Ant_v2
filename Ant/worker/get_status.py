from .. import interface

def get_status(worker):
    LOCATION = f"Location: {worker.current_location}"
    ENDURANCE = f"Endurance: {worker.endurance}%"
    HUNGER = f"Hunger: {worker.hunger}%"
    HEALTH = f"Health: {worker.health} / 100 hp"

    STATUS = [LOCATION, ENDURANCE, HUNGER, HEALTH]

    print(interface.generate_readable_list(STATUS))