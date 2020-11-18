from .. import interface, util
from time import sleep

def rest(worker):
    for i in range(3):
        print("Ant is resting...")
        sleep(2)
    amount_to_recover = util.provide_random_value()
    setattr(worker.char_stats, endurance, amount_to_recover)
    print(f"Ant has recovered {amount_to_recover}pts. of endurance!")
    print()
    print(f"Current endurance is now {getattr(worker.char_stats, endurance)}.")
    sleep(2)
