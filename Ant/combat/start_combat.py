from ..util import AntHasDied, delay_print
from time import sleep


def start_combat(combat, first_attacker):
    print("""
    
=============================
    
      BEGIN BUG BATTLE
    
==============================
   
    """)
    sleep(1)
    print(f"{first_attacker} attacks first!")

    combat.enemy.health = 100
    combat.enemy.endurance = 100

    while True:
        if first_attacker == "Ant":
            combat.worker_turn()
            if combat.enemy.health == 0:
                pass
            else:
                combat.enemy_turn()
        else:
            combat.enemy_turn()
            if combat.worker.char_stats.health == 0:
                pass
            else:
                combat.worker_turn()
        if combat.run_away:
            break
        if combat.worker.char_stats.health == 0:
            raise AntHasDied
        if combat.enemy.health == 0:
            print(" ")
            delay_print(f"{combat.enemy.display_name} has died!\n", time=0.2)
            sleep(1)
            print("Congrats!")
            print(" ")
            print("""

            =============================

                    END BUG BATTLE

            ==============================

                """)
            sleep(3)
            print(" ")
            combat.environment[combat.worker.current_location[0]][combat.worker.current_location[1]] = "x"
            break



