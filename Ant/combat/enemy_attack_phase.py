from time import sleep
import random
from ..util import NotEnoughEndurance


def enemy_attack_phase(combat):
    print(" ")
    print("The enemy will now attack!")
    sleep(3)
    print(" ")

    attack = random.choice(combat.enemy.attacks)

    try:
        combat.attack(combat.enemy, combat.worker.char_stats, attack)
    except NotEnoughEndurance:
        pass
