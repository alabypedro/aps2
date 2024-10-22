import json    # Arquivos .json
import pandas  # Data base
import os      # Operations system package
import tools   # tools.py

# Class ------------------------------------------------------------


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


# Main -------------------------------------------------------------
tools.clear()

# Write the file path to the city_db.json on db directory
FILE_PATH = os.path.join("db", "city_db.json")

with open(FILE_PATH, 'r', encoding='utf8') as db_file:
    city_dict = json.load(db_file)
    city_db = pandas.DataFrame(city_dict)

print(city_db)
