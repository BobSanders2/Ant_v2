from . import start_combat, worker_attack_phase

class Combat:
    def __init__(self, worker, enemy, environment):
        self.worker = worker
        self.enemy = enemy
        self.entities = [worker, enemy]
        self.run_away = False
        self.environment = environment


    start_combat = start_combat.start_combat
    worker_attacks = worker_attack_phase.worker_attack_phase

