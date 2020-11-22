from Ant import interface
from .util import delay_print
from Ant.start_game import start_game
from time import sleep

PLAY = "play"
HELP = "help"
QUIT = "quit"
COMMANDS = [PLAY, HELP, QUIT]

YES = "yes"
NO = "no"
CONTINUE_COMMANDS = [YES, NO]

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
            # delay_print("Your eyes have opened and you find yourself in a forest.\n")
            # sleep(1)
            # delay_print("You look around, but notice your body feels unusual.\n")
            # sleep(1)
            # delay_print("You try to move your hand to your face, but something is wrong.\n")
            # sleep(1)
            # delay_print("You look towards your body and realize you are no longer human!\n")
            # sleep(2)
            # print("")
            # print("YOU")
            # sleep(0.4)
            # print("ARE")
            # sleep(0.4)
            # print("AN")
            # sleep(0.4)
            # print("ANT!")
            # sleep(2)
            # print("")
            start_game()
            title = False
            print(f"Continue? {interface.generate_readable_list(CONTINUE_COMMANDS)}")
            command = interface.get_command(CONTINUE_COMMANDS)

            if command == YES:
                pass
            if command == NO:
                break

        elif command == HELP:
            print(f"Available Commands:\n{interface.generate_readable_list(COMMANDS)}")

        elif command == QUIT:
            break
