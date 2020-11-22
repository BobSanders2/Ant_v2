from time import sleep
import random
from ..char_stats import attacking
from ..util import NotEnoughEndurance


def enemy_attack_phase(combat):
    print("The enemy will now attack!")
    sleep(1)

    attack = random.choice(combat.enemy.attacks)

    try:
        attacking.attacking(combat.enemy, combat.worker, attack)
    except NotEnoughEndurance:
        pass
