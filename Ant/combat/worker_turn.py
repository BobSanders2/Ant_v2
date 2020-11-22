from .. import interface

ATTACK = "attack"
RUN_AWAY = "run_away"
REST = "rest"
COMMANDS = [ATTACK, REST, RUN_AWAY]


def worker_turn(combat):
    while True:
        print(f"What will you do?: {interface.generate_readable_list(COMMANDS)}")
        command = interface.get_game_command(combat.worker, combat.environment, additional_commands=COMMANDS, default=False)

        if command == REST:
            combat.worker.rest()

        if command == RUN_AWAY:
            combat.worker.run_away()

        if command == ATTACK:
            combat.worker_attacks()
