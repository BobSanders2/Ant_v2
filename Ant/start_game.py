from . import interface
from .create_environment import create_environment
from .create_worker import create_worker
from .util import GameOver

def start_game():
    environment = create_environment()
    worker = create_worker()

    try:
        
    except GameOver as exception:
        if isinstance(exception):
            interface.print_multiple_lines(lines=["=" * 20, "", "", "", "You have died", "", "", "", "=" * 20], delay=1)
        else:
            pass