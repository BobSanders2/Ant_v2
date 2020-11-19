import random
from time import sleep
from sys import stdout

def move(location):
    move_location = location.copy()

def provide_random_value():
    value_list = [30, 40, 50, 60, 70, 80, 85, 86, 87, 88, 90, 95, 96, 97, 98, 99, 100, 100, 100, 100]
    return random.choice(value_list)

def delay_print(text, time=0.05):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(time)

class GameOver(Exception):
    pass