from ..interface import get_game_command
from time import sleep
import random


def environment_interface(worker, environment, x, y):

    try:
        env_object = environment[x][y]
        if env_object == "l":
            additional_commands = ["walk over", "turn left", "turn right", "location", "status"]
            print("Ant has found a leaf. What will you do?")
            command = get_game_command.get_game_command(worker=worker, environment=environment, additional_commands=additional_commands, default=False)

            if command == "walk over":
                print("Ant has walked on top of the leaf.")

        if env_object == "n":
            additional_commands = ["eat", "turn left", "turn right", "location", "status"]
            print("Ant has found some nectar! What will you do?")
            command = get_game_command.get_game_command(worker=worker, environment=environment, additional_commands=additional_commands, default=False)

            if command == "eat":
                print("Ant has eaten the nectar.")
                print("His hunger has subsided!")
                print()
                worker.hunger = 0
                environment[x][y] = "x"
                print(f" Hunger: {worker.hunger}%")
                print()

        if env_object == "p":
            additional_commands = ["eat", "turn left", "turn right", "location", "status"]
            print("Ant has found some nectar! What will you do?")
            command = get_game_command.get_game_command(worker=worker, environment=environment, additional_commands=additional_commands, default=False)

            if command == "eat":
                print("Ant has eaten the nectar.")
                print("")
                sleep(1)
                print(".", end="")
                sleep(1)
                print(".", end="")
                sleep(1)
                print(".")
                sleep(1)
                print()
                print("Oh no! The nectar was poisonous!")
                damage_num = random.randint(20, 50)
                print(f"Ant was hurt. It takes {damage_num} damage to health.")
                print()
                sleep(1)
                worker.health -= damage_num
                environment[x][y] = "x"

        if env_object == "s":
            additional_commands = ["walk over", "turn left", "turn right", "location", "status"]
            print("Ant has found a stick. What will you do?")
            command = get_game_command.get_game_command(worker=worker, environment=environment, additional_commands=additional_commands)

            if command == "walk over":
                print("Ant has walked on top of the leaf.")

    except IndexError:
        raise IndexError
