from .char_stats import CharStats
from . import attacks


BITE_ATTACK = attacks.Attacks(name="Bite", damage_amount=15, description="Bite the enemy with your mandibles.",
                              endurance_cost=10)

ENEMY = CharStats(display_name="Rival", attacks=BITE_ATTACK, maximum_health=100, maximum_endurance=100, health=100,
                  endurance=100)


def enemy():
    return ENEMY
