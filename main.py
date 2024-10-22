import pandas as pd  # Data base
import json    # Arquivos .json
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


def panda_db():

    # Write the file path to the city_db.json on db directory
    FILE_PATH = os.path.join("db", "city_db.json")

    db = pd.read_json(FILE_PATH)  # Fills Panda's data base from json

    # Expandir a coluna 'cities' em linhas do DataFrame
    db_expanded = pd.json_normalize(db['cities'])

    print(db_expanded)


def main_menu():
    panda_db()
    user_menu_input = input("Escolha uma opção: ")

    if user_menu_input.lower() == "s":
        print(f"Até mais!")
        exit(0)


# Main -------------------------------------------------------------

LOOP_FLAG = True

while LOOP_FLAG:
    tools.clear()  # Clear the screen
    main_menu()
