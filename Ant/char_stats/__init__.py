class CharStats:
    def __init__(self, **stats):
        for stat, value in stats.items():
            setattr(self, stat, value)

