from .worker import Worker
from .char_stats import CharStats
from .attacks import Attacks

BITE_ATTACK = Attacks(name="Bite", damage_amount=15, description="Bite the enemy with your mandibles.",
                      endurance_cost=10)


ANT = CharStats(display_name="Ant",
                attacks=[BITE_ATTACK],
                maximum_health=100,
                maximum_endurance=100,
                maximum_hunger=100,
                health=100,
                endurance=100,
                hunger=0)


def create_worker():
    return Worker(ANT)