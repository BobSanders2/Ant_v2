from .. import interface
from . import worker_turn
from ..char_stats import attacking
from ..util import NotEnoughEndurance

RUN_AWAY = worker_turn.RUN_AWAY


def worker_attack_phase(combat):
    combat.generate_readable_attack_list()
    print("")
    print("What should Ant do?")
    additional_commands = [attack.name.lower() for attack in combat.worker.char_stats.attacks]
    additional_commands.append(RUN_AWAY)

    command = interface.get_game_command(combat.worker, combat.environment, additional_commands, default=False)

    if command == RUN_AWAY:
        return command

    if command != RUN_AWAY and command in additional_commands:
        for attack in combat.worker.char_stats.attacks:
            if attack.name.lower() == command:
                try:
                    attacking.attacking(combat.worker, combat.enemy, attack)
                except NotEnoughEndurance:
                    print("Ant is too tired to attack!")
