import pandas as pd  # Data base
import localPackage as tools  # tools.py
import os      # Operations system package
# import json    # Arquivos .json

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


class ShowDB:
    """Class used to handle the "Visualizar Base de Dados" Main Menu's option 
    """

    def __init__(self, data):
        self.expand_db = pd.json_normalize(data['Cidades'])
        self.metropolis = self.expand_db[self.expand_db['População'] > 1000000]
        self.largeCities = self.expand_db[self.expand_db['Área'] > 1000]

    # Print functions
    def print_cities(self):
        print(self.expand_db)

    def print_metropolis(self):
        print(self.metropolis)

    def print_largeCities(self):
        print(self.largeCities)

    # Sort Options
    def handle_sort_options(self, current_option):
        """Handle the sort options avaible inside the each of options on "Visualizar Base de Dados" section

        Args:
            current_option (int): The section between "Todas cidades/ metrópoles / área"

        Returns:
            function: If user_option == 0 returns visualize_db()
        """
        print("\nOrganizar por: ")
        print("[1] A-Z [2] Área (km²) [3] População [4] Índice [0] 0 para voltar")
        user_input = input("Digite uma opção: ")

        # Handle the "Visualizar todas cidades" options
        if current_option == 1:
            # Variables that handle the sorted result
            self.sortName = self.expand_db.sort_values(
                by="Cidade", ascending=True)
            self.sortArea = self.expand_db.sort_values(
                by="Área", ascending=False)
            self.sortPop = self.expand_db.sort_values(
                by="População", ascending=False)
            self.sortIndex = self.expand_db.sort_index(ascending=True)

        if current_option == 2:
            self.sortName = self.metropolis.sort_values(
                by="Cidade", ascending=True)
            self.sortArea = self.metropolis.sort_values(
                by="Área", ascending=False)
            self.sortPop = self.metropolis.sort_values(
                by="População", ascending=False)
            self.sortIndex = self.largeCities.sort_index(ascending=True)

        if current_option == 3:
            self.sortName = self.largeCities.sort_values(
                by="Cidade", ascending=True)
            self.sortArea = self.largeCities.sort_values(
                by="Área", ascending=False)
            self.sortPop = self.largeCities.sort_values(
                by="População", ascending=False)
            self.sortIndex = self.largeCities.sort_index(ascending=True)

        if user_input == '1':
            tools.clear()
            print(self.sortName)
        elif user_input == '2':
            tools.clear()
            print(self.sortArea)
        elif user_input == '3':
            tools.clear()
            print(self.sortPop)
        elif user_input == '4':
            tools.clear()
            print(self.sortIndex)
        elif user_input == '0':
            return visualize_db()
        else:
            tools.input_error(user_input)


# Functions --------------------------------------------------------

def panda_db():
    """Read city_db.json file and fills the Panda's data base

    Returns:
        Data: DataBase
    """

    # Write the file path to the city_db.json on db directory
    FILE_PATH = os.path.join("db", "city_db.json")

    DataBase = pd.read_json(FILE_PATH)  # Fills Panda's data base from json

    return DataBase


def visualize_db():
    """ Open a menu for visualize_db options, uses ShowDB class
    """
    tools.clear()
    DataBase = ShowDB(panda_db())

    tools.session_header("Base de Dados")

    options_display = """
[1] Visualizar todos as cidades
[2] Visualizar apenas metrópoles
[3] Visualizar apenas cidades com área > 1000 km²
[0] Voltar
[s] Sair
"""

    print(options_display)
    user_input = input("Escolha uma opção: ")

    if user_input == '1':  # Visualizar todas as cidades
        tools.clear()
        tools.session_header("Todas cidades")
        DataBase.print_cities()
        while True:
            DataBase.handle_sort_options(1)

    elif user_input == '2':  # Visualizar apenas metrópoles
        tools.clear()
        tools.session_header("Metrópoles")
        DataBase.print_metropolis()
        while True:
            DataBase.handle_sort_options(2)

    elif user_input == '3':  # Visualizar apenas cidades com área > 1000 km²
        tools.clear()
        tools.session_header("Grandes cidades")
        DataBase.print_largeCities()
        while True:
            DataBase.handle_sort_options(3)

    elif user_input == '0':  # Voltar
        main_menu()

    elif user_input.lower() == 's':  # Sair
        exit(0)
        print("Até mais!")

    else:
        tools.input_error(user_input)


def main_menu():
    tools.clear()  # Clear the screen
    # A header to identify the current section
    tools.session_header("Menu Principal")

    options_display = """
[1] Visualizar base de dados
[2] Procurar por cidade específica
[3] Inserir uma nova cidade
[4] Alterar dados
[s] Sair
"""

    print(options_display)
    user_menu_input = input("Escolha uma opção: ")

    if user_menu_input == '1':
        visualize_db()
    elif user_menu_input == '2':
        ...
    elif user_menu_input == '3':
        ...
    elif user_menu_input == '4':
        ...
    elif user_menu_input.lower() == "s":
        print(f"Até mais!")
        exit(0)
    else:
        tools.input_error(user_menu_input)

# Main -------------------------------------------------------------


LOOP_FLAG = True

while LOOP_FLAG:
    panda_db()
    main_menu()
