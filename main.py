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


# Functions --------------------------------------------------------


def panda_db():

    # Write the file path to the city_db.json on db directory
    FILE_PATH = os.path.join("db", "city_db.json")

    DataBase = pd.read_json(FILE_PATH)  # Fills Panda's data base from json

    return DataBase


def visualize_db():
    tools.clear()
    DataBase = panda_db()

    tools.session_header("Base de Dados")

    options_display = """
[1] Visualizar todos as cidades
[2] Buscar por cidades
[3]
[0] Voltar
[s] Sair
"""

    print(options_display)
    user_input = input("Escolha uma opção: ")

    if user_input == '1':
        ...
    elif user_input == '2':
        ...
    elif user_input == '3':
        ...
    elif user_input == '0':
        main_menu()
    elif user_input.lower() == 's':
        exit(0)
        print("Até mais!")

    # # Expand the db and print in collums and row
    # DataBase_expanded = pd.json_normalize(DataBase['Cidades'])
    # print(DataBase_expanded)


def main_menu():
    tools.session_header("Menu Principal")

    options_display = """
[1] Acessar base de dados
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
    tools.clear()  # Clear the screen
    panda_db()
    main_menu()
