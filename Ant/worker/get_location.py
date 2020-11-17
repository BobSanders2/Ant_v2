from .. import interface

def get_location(worker):
    print(f"Ant is currently located at x:{worker.current_location[0]} y:{worker.current_location[1]}")
