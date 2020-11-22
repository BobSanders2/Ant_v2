from . import worker_turn, enemy_turn
from .. import util
from time import sleep


def start_combat(combat, first_attacker):
    print("""
    
=============================
    
      BEGIN BUG BATTLE
    
==============================
   
    """)
    sleep(1)
    print(f"{first_attacker} attacks first!")

    while True:
        if first_attacker == "Ant":
            combat.worker_turn()
            combat.enemy_turn()
        else:
            combat.enemy_turn()
            combat.worker_turn()

        if combat.run_away:
            break

        if combat.worker.health == 0:
            raise util.AntHasDied

        if combat.enemy.health == 0:
            util.delay_print("The enemy Ant has died!", time=0.5)
            sleep(1)
            print("Congrats!")
            sleep(1)
            combat.environment[combat.worker.current_location[0]][combat.worker.current_location[1]] = "x"
            break



