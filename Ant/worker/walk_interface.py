from Ant.interface.environment_interface import environment_interface


def walk_process(worker, environment):
    x, y = worker.current_location

    if worker.facing == "north":
        try:
            environment_interface(worker=worker, environment=environment, x=x - 1, y=y)
            worker.current_location[0] -= 1
        except IndexError:
            return False
    elif worker.facing == "south":
        try:
            environment_interface(worker=worker, environment=environment, x=x + 1, y=y)
            worker.current_location[0] += 1
        except IndexError:
            return False
    elif worker.facing == "west":
        try:
            environment_interface(worker=worker, environment=environment, x=x, y=y - 1)
            worker.current_location[1] -= 1
        except IndexError:
            return False
    elif worker.facing == "east":
        try:
            environment_interface(worker=worker, environment=environment, x=x, y=y + 1)
            worker.current_location[1] += 1
        except IndexError:
            return False


def walk_interface(worker, environment):
    walk = walk_process(worker, environment)

    if getattr(worker.char_stats, 'endurance') == 0:
        print("Ant is tired and must rest!!")
        return None
    else:
        if walk is False:
            print("Ant can't go that way")
        else:
            setattr(worker.char_stats, 'endurance', getattr(worker.char_stats, 'endurance') - 10)
            print("Ant has moved forward.")


def run_away(worker):
    x, y = worker.current_location

    if worker.facing == "north":
        worker.facing = "south"
        worker.current_location[0] += 1
        print(f"Ant has run away and is now facing the {worker.facing}.")
    elif worker.facing == "south":
        worker.facing = "north"
        worker.current_location[0] -= 1
        print(f"Ant has run away and is now facing the {worker.facing}.")
    elif worker.facing == "west":
        worker.facing = "east"
        worker.current_location[1] += 1
        print(f"Ant has run away and is now facing the {worker.facing}.")
    elif worker.facing == "east":
        worker.facing = "west"
        worker.current_location[1] -= 1
        print(f"Ant has run away and is now facing the {worker.facing}.")

