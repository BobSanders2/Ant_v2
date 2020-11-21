from .. import interface

ATTACK = "attack"
RUN_AWAY = "run_away"
REST = "rest"
COMMANDS = [ATTACK, REST, RUN_AWAY]


def worker_turn(combat):
    while True:
        interface.generate_readable_list(COMMANDS)
        command = interface.get_command(COMMANDS)

        if command == REST:
            combat.worker.rest()

        if command == RUN_AWAY:
            combat.worker.run_away()

        if command == ATTACK:
            combat.worker_attacks()
