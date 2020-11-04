from .generate_readable_list import generate_readable_list

def get_command(commands, list_options=False):
    while True:
        if list_options:
            print(f"Available Commands: {generate_readable_list(commands)}")

        received_input = input(">>>")

        if received_input in commands:
            return received_input

        print(f"""I didn't understand that command. 
Available commands are: {generate_readable_list(commands)}""")

