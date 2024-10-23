import pandas as pd  # Data base
import localPackage as tools  # tools.py
import os      # Operations system package
# import json    # Arquivos .json

ASCII_ART = """
                                                                                                    
                                                                                                    
                                                                                                    
                       .                                                                            
                       ~                                                                            
                       ~                                                      .                     
                       7                                                      ^                     
                      .G^                                                     !^                    
                      ^??                                                    .J!                    
                     .5Y5^                                                   ?5Y.                   
                     !~:^7                                                  .P7J!                   
                    .Y~^??:                                                 :P!~5                   
                    ^J^~?!!                                                .~57!5.                  
                    75:J!7J                       ..~....     :^~!:   .:.. .Y?7JY^   YY777?J.       
                    ?5~7!7?                       7!~!^7G    ~JYYYJ75.~PBY^^5575Y7:  5J!~!?P.      .
                    ?Y~7!!Y                      ^~^^~^~7^   !~~7JJJ5J~YY!~7P5!?J~^  5^::^^Y.     .G
                    J?~^!!J                     ?7::^~^~^5!::!!~^^^:7!:Y?~JJ5P~?J!!  P::::^Y.     .J
            ?~^7~~! J!~:~^7    57^J             J!!::!.:^J????~^::. !!~GJ!J?J5J77!J~ P~~^^^J^...  .?
            5!!~^:? ??7:!^~    G7^J           !~?!!..~..:?^~!?^^::. !7J57!????J::.7~ P^::^^J7~!5. :?
     ::.    B!7~!^J ?J!:!^:    P~.?~!:~...    J?P!7.:?.:.7^~~7!!~^: 7!Y5Y?JJ?7J^:.!5~G!^:^^J7::577P?
  ...!^!.^:^G^!^~^5 ?~^.~7J77~^5~:J^...::57^  J!P?7^:J:::!~77?~!~:: !?55GJ?YJ!J^..75JP~::::?7^:J7J5Y
  7~~?^:!?~~^!7^!~P!Y~~^P!~!7!^P7^Y:.:.:.YYY!.!777~J!J::JY7YY^^~~^: ~Y7Y5J?Y?!J^:.7J~Y^::..?7^~!!?!!
  !^:!^.:!~~^!?!!7577~Y!P:..^~^G?^Y:...:.7YJY5!~^^:!??^^J?~!Y?7:^Y^:~7^!???Y7!?::^7Y!5~^^^^J7??^!7!!
7Y5~~^. .~^^^?!7!7P!7:7~7~..!^^P?^Y:...:.7JJJ?77~~^~P!:^!J^^7J~..5Y!77^~7!!Y!!?.:~JY~57~~~~J?!!.!!~!
"""

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
        """Handle the sort options avaiable at "Visualizar Base de Dados" section

        Args:
            current_option (int): The section between "Todas cidades/ metrópoles / área"

        Returns:
            function: If user_option == 0 returns visualize_db()
        """

        print("\nOrganizar por: ")
        print("[1] A-Z [2] Área (km²) [3] População [4] Índice [0] 0 para voltar")
        user_input = input("Digite a opção desejada: ")

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
            return display_data_menu()
        else:
            tools.input_error(user_input)

    def find_city_menu(self):
        tools.clear()
        search_string = input("Digite o nome da cidade que deseja buscar: ")
        result = self.expand_db[self.expand_db['Cidade'].str.contains(
            search_string, case=False, na=False)]

        # Checking if result is empty
        if result.empty:
            print(Color.BOLD, Color.RED,
                  f"Não foi possível encontrar '{
                      search_string}' na base de dados",
                  Color.END, sep="")
        else:
            print()  # New line
            tools.session_header(
                "Resultado ==============================")
            print("\n", result, sep="")

            # Len of string
            print("\n", Color.BOLD, 45 * "=", Color.END, sep="")


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


def display_data_menu():
    """ Open a menu for visualize_db options, uses ShowDB class
    """
    tools.clear()
    DataBase = ShowDB(panda_db())

    tools.session_header("Base de Dados")

    options_display = """
[1] Visualizar todos as cidades
[2] Visualizar apenas metrópoles
[3] Visualizar apenas cidades com área > 1000 km²
[4] Buscar cidade pelo nome
[5] Alterar dados de uma cidade
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

    elif user_input == '4':
        tools.clear()
        tools.session_header("Buscador")
        DataBase.find_city_menu()
        while True:
            print("\n[1] Fazer nova busca [0] voltar")
            user_input = input("Digite a opção desejada: ")
            if user_input == '1':
                DataBase.find_city_menu()
            elif user_input == '0':
                display_data_menu()
            else:
                tools.input_error(user_input)

    elif user_input == '0':  # Voltar
        main_menu()

    elif user_input.lower() == 's':  # Sair
        print("Até mais!")
        exit(0)

    else:
        tools.input_error(user_input)

def add_cidade_menu():
    cidade = ""
    area = ""
    populacao = ""

while True:
    tools.clear()
    tools.session_header("add_cidade_menu")
    
    print(f"""
[1] Cidade: {cidade}
[2] Área: {area}
[3] População: {populacao}
[4] Confirma
[0] Volta         
""")
    user_input=input("Selecione uma opção: ")
    
    if user_input== "1":
        cidade = input("Digite o nome da cidade: ")
        
    elif user_input== "2":
        area = input("Digite a área da cidade: ")
    
    elif user_input== "3":
        populacao = input("Digite a população da cidade: ")
    
    elif user_input== "4":
        ...
    elif user_input== "0":
        exit(0)
        if cidade.empty:
            print("Campo cidade está vazio.")
        if area.empty:
            print("Campo área está vazio.")
        if  populacao.empty:
            print("Campo população está vazio. ")
    else:
        tools.input_error(user_input)
def main_menu():
    tools.clear()  # Clear the screen
    # A header to identify the current section
    print(ASCII_ART)

    tools.session_header("Menu Principal")

    options_display = """
[1] Acessar base de dados
[2] Inserir uma nova cidade
[3] Cálculos estatísticos
[s] Sair
"""

    print(options_display)
    user_menu_input = input("Escolha uma opção: ")

    if user_menu_input == '1':
        display_data_menu()
    elif user_menu_input == '2':
        ...
    elif user_menu_input == '3':
        ...
    elif user_menu_input.lower() == "s":
        print(f"Até mais!")
        exit(0)
    else:
        tools.input_error(user_menu_input)


# Main -------------------------------------------------------------

while True:
    panda_db()
    main_menu()
