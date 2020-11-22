from ..enemies import enemy
from ..combat import Combat
from ..interface import get_command, generate_readable_list, get_game_command
from time import sleep
import random


def environment_interface(worker, environment, x, y):

    if x > 25 or x < 0 or y > 25 or y < 0:
        raise IndexError

    else:
        env_object = environment[x][y]
        if env_object == "l":
            additional_commands = ["walk over"]
            print("Ant has found a leaf. What will you do?")
            command = get_game_command(worker=worker, environment=environment, additional_commands=additional_commands)

            if command == "walk over":
                print("Ant has walked on top of the leaf.")

        if env_object == "n":
            additional_commands = ["eat"]
            print("Ant has found some nectar! What will you do?")
            command = get_game_command(worker=worker, environment=environment, additional_commands=additional_commands)

            if command == "eat":
                print("Ant has eaten the nectar.")
                print("His hunger has subsided!")
                print()
                worker.hunger = 0
                environment[x][y] = "x"
                print(f" Hunger: {worker.hunger}%")
                print()

        if env_object == "p":
            additional_commands = ["eat"]
            print("Ant has found some nectar! What will you do?")
            command = get_game_command(worker=worker, environment=environment, additional_commands=additional_commands)

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
            additional_commands = ["walk over"]
            print("Ant has found a stick. What will you do?")
            command = get_game_command(worker=worker, environment=environment,
                                       additional_commands=additional_commands)

            if command == "walk over":
                print("Ant has walked on top of the leaf.")

        if env_object == "e":
            commands = ["run away", "attack"]
            print("You have encountered an enemy!")
            first_attacker = random.choice(["Ant", "Enemy"])

            if first_attacker == "Ant":
                sleep(1)
                print("What will you do?")
                command = get_command(commands, list_options=True)
                if command == "run away":
                    worker.run_away()
                elif command == "attack":
                    combat = Combat(worker, enemy(), environment)
                    combat.start_combat(first_attacker)
            else:
                sleep(1)
                print("The other ant has noticed you!")
                sleep(1)
                print("It rushes towards you with murderous intent!")
                sleep(1)
                combat = Combat(worker, enemy(), environment)
                combat.start_combat(first_attacker)
