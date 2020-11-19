from .get_command import get_command
from .print_multiple_lines import print_multiple_lines

WALK = "walk"
TURN_LEFT = "turn left"
TURN_RIGHT = "turn right"
REST = "rest"
LOCATION = "location"
STATUS = "status"

BASE_COMMANDS = [WALK, TURN_LEFT, TURN_RIGHT, REST, LOCATION, STATUS]

def get_game_command(worker, environment, additional_commands=[], default=True):
    if default:
        commands = additional_commands.copy()
        commands.extend(BASE_COMMANDS)

    else:
        commands = additional_commands

    while True:
        print()
        command = get_command(commands)

        if command in additional_commands:
            return command

        if command == "walk":
            worker.walk(environment)

        if command == "turn left":
            worker.turn_interface("left")

        if command == "turn right":
            worker.turn_interface("right")

        if command == "rest":
            worker.rest()

        if command == "location":
            worker.location()

        if command == "status":
            worker.status()
