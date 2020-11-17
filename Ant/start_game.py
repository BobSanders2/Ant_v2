from . import interface
from .interface.get_game_command import get_game_command
from .create_environment import create_environment
from .create_worker import create_worker
from .util import GameOver

def start_game():
    environment = create_environment()
    worker = create_worker()
    COMMANDS = interface.get_game_command.BASE_COMMANDS

    try:
        print(f"Please choose either: {interface.generate_readable_list(COMMANDS)}")
        get_game_command(worker, environment)
    except GameOver as exception:
        if isinstance(exception):
            interface.print_multiple_lines(lines=["=" * 20, "", "", "", "You have died", "", "", "", "=" * 20], delay=1)
        else:
            pass