from .get_command import get_command
from .print_multiple_lines import print_multiple_lines

WALK = "walk"
TURN_LEFT = "turn left"
TURN_RIGHT = "turn right"
REST = "rest"
LOCATION = "location"
STATUS = "status"

BASE_COMMANDS = [WALK, TURN_LEFT, TURN_RIGHT, REST, LOCATION, STATUS]

def get_game_command(worker, location, additional_commands=[]):
    commands = additional_commands.copy()
    commands.extend(BASE_COMMANDS)

    while True:
        print()
        command = get_command(commands, True)

        if command in additional_commands:
            return command

        if command == WALK:
            worker.