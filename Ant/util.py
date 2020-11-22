import random
from time import sleep
from sys import stdout

def set_attributes(object, **attributes):
    for k, v in attributes.items():
        setattr(object, k, v)

def move(location):
    move_location = location.copy()

def provide_random_value(possibility="high"):
    if possibility == "high":
        value_list = [20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99, 100, 100, 100]
        return random.choice(value_list)
    elif possibility == "medium":
        value_list = [10, 20, 30, 40, 45, 48, 49, 50, 51, 52, 55, 60, 70, 80, 90, 100 ]
        return random.choice(value_list)
    elif possibility == "low":
        value_list = [5, 10, 15, 16, 20, 21, 22, 23, 24, 30, 31, 32, 34, 35, 40, 45, 50, 60, 70, 80, 90, 100]
        return random.choice(value_list)

def delay_print(text, time=0.05):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(time)

class GameOver(Exception):
    pass

class AntHasDied(Exception):
    pass

class NotEnoughEndurance(Exception):
    pass