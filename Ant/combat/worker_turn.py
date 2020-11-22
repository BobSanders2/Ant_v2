from .. import interface
ATTACK = "initiate attack"
RUN_AWAY = "run away"
REST = "rest"
COMMANDS = [ATTACK, REST, RUN_AWAY]


def worker_turn(combat):
    while True:
        combat.current_attacker = "Ant"
        combat.display_stats()
        print(f"What will you do?: {interface.generate_readable_list(COMMANDS)}")
        command = interface.get_game_command(combat.worker, combat.environment, additional_commands=COMMANDS, default=False)

        if command == REST:
            combat.rest()
            break

        if command == RUN_AWAY:
            combat.worker.run_away()
            combat.run_away = True
            break

        if command == ATTACK:
            combat.worker_attacks()
            break
