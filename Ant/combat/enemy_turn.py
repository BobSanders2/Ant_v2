from ..combat.enemy_attack_phase import enemy_attack_phase
from .. import util
from time import sleep


def enemy_turn(combat):
    current_endurance = combat.enemy.endurance
    available_attacks = [attack for attack in combat.enemy.attacks if attack.endurance_cost > current_endurance]

    if len(available_attacks) > 0:
        enemy_attack_phase()
    else:
        amount_to_recover = util.provide_random_value()
        setattr(combat.enemy, 'endurance', amount_to_recover)
        print(f"Enemy is resting...")
        sleep(1)
        print(f"Enemy has recovered {amount_to_recover}pts. of endurance!")
        print("")
