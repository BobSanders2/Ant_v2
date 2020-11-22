from ..util import NotEnoughEndurance

def attacking(attacker, defender, attack):
    print(dir(attacker))
    if attack.endurance_cost > attacker.endurance:
        raise NotEnoughEndurance
    else:
        attacker.endurance -= attack.endurance_cost

        damage_dealt = getattr(attacker, 'damage_amount')

        defender.health -= damage_dealt

        print(f"{attacker} has hit {defender} for {damage_dealt}pts. of damage!")
