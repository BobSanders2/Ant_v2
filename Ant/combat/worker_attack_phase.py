from .generate_readable_attack_list import generate_readable_attack_list
from .. import interface
from . import worker_turn

def worker_attack_phase(combat):
    generate_readable_attack_list()
    print("")
    print("Pick your attack:")
    additional_commands = [attack.lower() for attack in combat.worker.char_stats.attacks]

    command = interface.get_game_command(combat.worker, combat.environment, additional_commands, default=False)

    if command == worker_turn.RUN_AWAY:
        return command

    if command ==