import random

def move(location):
    move_location = location.copy()

def provide_random_value():
    value_list = [30, 40, 50, 60, 70, 80, 85, 86, 87, 88, 90, 95, 96, 97, 98, 99, 100, 100, 100, 100]
    return random.choice(value_list)

class GameOver(Exception):
    pass