from .. import interface


def turn_interface(worker, string):
    direction_list_left = ["north", "west", "south", "east"]
    direction_list_right = ["north", "east", "south", "west"]

    new_direction = ""

    if string == "left":
        try:
            for direction in direction_list_left:
                if worker.facing == direction:
                    new_direction = direction_list_left[direction_list_left.index(direction) + 1]
                    print(f"Ant has turned left and is facing the {new_direction}.")
            worker.facing = new_direction
        except IndexError:
            worker.facing = "north"
            print(f"Ant has turned left and is facing the {worker.facing}.")
    elif string == "right":
        try:
            for direction in direction_list_right:
                if worker.facing == direction:
                    new_direction = direction_list_right[direction_list_right.index(direction) + 1]
                    print(f"Ant has turned right and is facing the {new_direction}.")
            worker.facing = new_direction
        except IndexError:
            worker.facing = "north"
            print(f"Ant has turned right and is facing the {worker.facing}.")



