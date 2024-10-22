import os      # OS operations


def clear():
    """ Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')  # clear multiplataform
