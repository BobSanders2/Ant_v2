from ..combat.enemy_attack_phase import enemy_attack_phase
from .. import util
from time import sleep
from ..dev_help import dev_help


def enemy_turn(combat):
    combat.current_attacker = "Enemy"
    current_endurance = combat.enemy.endurance
    available_attacks = [attack for attack in combat.enemy.attacks if attack.endurance_cost < current_endurance]
    if len(available_attacks) > 0:
        combat.enemy_attack_phase()
    else:
        amount_to_recover = util.provide_random_value()
        new_endurance = combat.enemy.endurance + amount_to_recover
        if new_endurance >= 100:
            combat.enemy.endurance = 100
        else:
            combat.enemy.endurance = new_endurance
        print(f"Enemy is resting...")
        sleep(1)
        print(f"Enemy has recovered {amount_to_recover}pts. of endurance!")
        print("")
        sleep(2)
