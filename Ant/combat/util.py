from ..util import provide_random_value, NotEnoughEndurance, AntHasDied
from time import sleep
from ..combat.enemy_status import enemy_status


def rest(combat):
    if combat.current_attacker == "Ant":
        for i in range(3):
            print("Ant is resting...")
            sleep(2)
        health_to_recover = provide_random_value(possibility="medium")
        endurance_to_recover = provide_random_value(possibility="medium")

        new_health = combat.worker.char_stats.health + health_to_recover
        new_endurance = combat.worker.char_stats.endurance + endurance_to_recover

        if new_health >= 100:
            combat.worker.char_stats.health = 100
        else:
            combat.worker.char_stats.health = new_health

        if new_endurance >= 100:
            combat.worker.char_stats.endurance = 100
        else:
            combat.worker.char_stats.endurance = new_endurance

        print(" ")
        print(f"Ant has recovered {health_to_recover}pts. of health!")
        print(f"Current health is now {getattr(combat.worker.char_stats, 'health')}%.")
        print(" ")
        print(f"Ant has recovered {endurance_to_recover}pts. of endurance!")
        print(f"Current endurance is now {getattr(combat.worker.char_stats, 'endurance')}%.")
        sleep(2)

    else:
        for i in range(3):
            print(f"{combat.enemy.display_name} is resting...")
            sleep(1)
        amount_to_recover = provide_random_value()

        new_health = combat.enemy.health + amount_to_recover

        if new_health >= 100:
            combat.enemy.health = 100
        else:
            combat.enemy.health = new_health

        print(f"{combat.enemy.display_name} has recovered {amount_to_recover}pts. of health!")
        sleep(2)


def attacking(combat, attacker, defender, attack):
    if attack.endurance_cost > attacker.endurance:
        raise NotEnoughEndurance
    else:
        attacker.endurance -= attack.endurance_cost
        damage_dealt = getattr(attack, 'damage_amount')
        print(f"{attacker.display_name} has hit {defender.display_name} for {damage_dealt}pts. of damage!")
        if (defender.health - damage_dealt) > 0:
            defender.health -= damage_dealt
        else:
            defender.health = 0


