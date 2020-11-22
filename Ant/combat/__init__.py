from . import start_combat, worker_attack_phase, worker_turn, enemy_turn, enemy_attack_phase, generate_readable_attack_list

class Combat:
    def __init__(self, worker, enemy, environment):
        self.worker = worker
        self.enemy = enemy
        self.entities = [worker, enemy]
        self.run_away = False
        self.environment = environment


    start_combat = start_combat.start_combat
    worker_turn = worker_turn.worker_turn
    worker_attacks = worker_attack_phase.worker_attack_phase
    enemy_turn = enemy_turn.enemy_turn
    enemy_attack_phase = enemy_attack_phase.enemy_attack_phase
    generate_readable_attack_list = generate_readable_attack_list.generate_readable_attack_list


