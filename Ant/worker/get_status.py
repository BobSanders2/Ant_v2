from .. import interface

def get_status(worker):
    LOCATION = f"Location: {worker.current_location}"
    ENDURANCE = f"Endurance: {getattr(worker.char_stats, endurance)} / {getattr(worker.char_stats, maximum_endurance)}%"
    HUNGER = f"Hunger: {getattr(worker.char_stats, hunger)} / {getattr(worker.char_stats, maximum_hunger)}%"
    HEALTH = f"Health: {getattr(worker.char_stats, health)} / {getattr(worker.char_stats, maximum_health)}"

    STATUS = [LOCATION, ENDURANCE, HUNGER, HEALTH]

    print(interface.generate_readable_list(STATUS))