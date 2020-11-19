from .worker import Worker
from .char_stats import CharStats


ANT = CharStats(display_name="Ant",
                maximum_health=100,
                maximum_endurance=100,
                maximum_hunger=100,
                health=100,
                endurance=100,
                hunger=0)


def create_worker():
    return Worker(ANT)