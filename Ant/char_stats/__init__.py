from . import entity_value_properties


class CharStats:
    def __init__(self, display_name, attacks, **stats):
        for stat, value in stats.items():
            setattr(self, stat, value)

        self.display_name = display_name
        self.attacks = attacks


for value_name in ["health", "endurance", "hunger"]:
    setattr(CharStats, value_name, entity_value_properties.generate_value_property(value_name))

    setattr(CharStats, "maximum_" + value_name, entity_value_properties.generate_maximum_value_stat_property(value_name))

