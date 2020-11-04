from time import sleep

def print_multiple_lines(lines, delay=None):
    for one_line in lines:
        print(one_line)

        if delay:
            sleep(delay)