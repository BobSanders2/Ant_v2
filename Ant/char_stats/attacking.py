def attacking(attacker, defender, attack):
    if attack.endurance_cost > attacker.endurance:
        return "not enough endurance"

    attacker.endurance -= attack.endurance_cost

    damage_dealt = getattr(attacker, attack.damage_amount)

    defender.health -= damage_dealt