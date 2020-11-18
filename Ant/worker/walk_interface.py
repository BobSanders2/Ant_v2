from Ant.interface.environment_interface import environment_interface


def walk_interface(worker, environment):
    x, y = worker.current_location

    try:
        if getattr(worker.char_stats, endurance) == 0:
            print("Ant is tired and must rest!!")
            return None
        elif worker.facing == "north":
            print("Ant moved forward.")
            environment_interface(worker=worker, environment=environment, x=x - 1, y=y)
            worker.current_location[0] -= 1
        elif worker.facing == "south":
            print("Ant moved forward.")
            environment_interface(worker=worker, environment=environment, x=x + 1, y=y)
            worker.current_location[0] += 1
        elif worker.facing == "west":
            print("Ant moved forward.")
            environment_interface(worker=worker, environment=environment, x=x, y=y - 1)
            worker.current_location[1] -= 1
        elif worker.facing == "east":
            print("Ant moved forward.")
            environment_interface(worker=worker, environment=environment, x=x, y=y + 1)
            worker.current_location[1] -= 1

        setattr(worker.char_stats, endurance, getattr(worker.char_stats, endurance) - 10)
    except IndexError:
        print("Ant can't go that way!")
