from .. import interface
from time import sleep

def rest(worker):
    for i in range(3):
        print("Ant is resting...")
        sleep(2)
    print("""Ant has fully recovered his endurance!        
            """)
    worker.endurance = 100