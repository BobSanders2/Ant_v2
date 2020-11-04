from Ant import interface
from Ant.start_game import start_game
from time import sleep

PLAY = "play"
HELP = "help"
QUIT = "quit"
COMMANDS = [PLAY, HELP, QUIT]

def play():
    title = False
    while True:
        if not title:
            title = True
            print("""
            ===================================================
            ===================================================
            ===================================================
        
                        Welcome to the Ant Game!
        
            ===================================================
            ===================================================
            ===================================================
        
            """)
            sleep(1)
            print(f"Please choose either: {interface.generate_readable_list(COMMANDS)}")


        else:
            pass

        command = interface.get_command(COMMANDS)

        if command == PLAY:
            start_game()

        elif command == HELP:
            print(f"Available Commands:\n{interface.generate_readable_list(COMMANDS)}")

        elif command == QUIT:
            break
