from . import interface

def movement(worker, environment):
    while True:
        additional_commands = ["move forward", "turn left", "turn right"]

        command = interface.get_game_command()