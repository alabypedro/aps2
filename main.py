import json    # Arquivos .json
import pandas  # Data base
import os      # Operations system package
import tools   # tools.py

# Class ----------------------------------------------------------


class Color:
    """Just add colors for strings.
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class PreMadeMessages:
    """Just like the name says, print a text if premaded design
    """

    def __init__(self, text):
        self.text = text

    def error(self):
        print(
            Color.BOLD, Color.RED,
            self.text,
            Color.END, sep="", end=2*"\n"
        )


# Functions --------------------------------------------------------


def panda_db_update():
    """Opens json data base file, and update the Panda's data base
    """

    # Write the file path to the city_db.json on db directory
    FILE_PATH = os.path.join("db", "city_db.json")

    # Read the file and transfer to the pandas Data Base
    with open(FILE_PATH, 'r', encoding='utf8') as db_file:
        city_dict = json.load(db_file)
        city_db = pandas.DataFrame(city_dict)

    print(city_db)


def main_menu():
    panda_db_update()
    user_menu_input = input("Escolha uma opção: ")

    if user_menu_input.lower() == "s":
        print(f"Até mais!")
        exit(0)


# Main -------------------------------------------------------------

LOOP_FLAG = True

while LOOP_FLAG:
    tools.clear()  # Clear the screen
    main_menu()
