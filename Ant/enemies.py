from .char_stats import CharStats
from .attacks import Attacks


BITE_ATTACK = Attacks(name="Bite", damage_amount=15, description="Bite the enemy with your mandibles.",
                      endurance_cost=10)

HEADBUTT_ATTACK = Attacks(name="Headbutt", damage_amount=20, description="Headbutt the enemy.", endurance_cost=20)

ENEMY = CharStats(display_name="Rival", attacks=[BITE_ATTACK], maximum_health=100, maximum_endurance=100, health=100,
                  endurance=100)


def enemy():
    return ENEMY