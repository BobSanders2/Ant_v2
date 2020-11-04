from .walk import walk

class Worker:
    def __init__(self):
        self.current_location = []
        self.facing = []

    walk = walk.walk

