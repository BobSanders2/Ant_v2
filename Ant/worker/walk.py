def walk(worker):
    if worker.facing == "north":
        try:
            worker.current_location[0][0] -= 1
        except IndexError:
            print("Can't move that way!")
    elif worker.facing == "south":
        try:
            worker.current_location[0][0] += 1
        except IndexError:
            print("Can't move that way!")
    elif worker.facing == "west":
        try:
            worker.current_location[0][1] -= 1
        except IndexError:
            print("Can't move that way!")

