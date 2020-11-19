from .. import interface

BITE = "bite"
RUN_AWAY = "run_away"
REST = "rest"
COMMANDS = [BITE, REST, RUN_AWAY]


def worker_turn(combat):
    while True:
        interface.generate_readable_list(COMMANDS)
        command = interface.get_command(COMMANDS)

        if command == REST:
            combat.worker.rest()

        if command == RUN_AWAY:
            combat.worker.run_away()

        if command == BITE:
            combat.