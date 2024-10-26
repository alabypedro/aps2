from curses.ascii import isdigit
import pandas as pd  # Data base
import localPackage as tools  # tools.py
import os      # Operations system package
import json    # Arquivos .json

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

    def print_average_statistics(self, current_option):
        """Calculate and print average statistics of cities based on "current_option"
            current_option == 1: All the database
            current_option == 2: Only metropolis
            current_option == 3: Only large cities

        Args:
            current_option (int): respective number of the current "display_data_menu" option
        """

        if current_option == 1:  # All the cities
            # Used on output to identify the city type for the current option
            city_string = "cidades"

            average_pop = self.expand_db["População"].mean()
            average_area = self.expand_db["Área"].mean()
            average_demographic_density = average_pop / average_area

            av_pop_text = f"{Color.BOLD}{average_pop:,.2f}{Color.END}"
            av_area_text = f"{Color.BOLD}{average_area:,.2f}{Color.END}"
            av_dem_text = f"{Color.BOLD}{
                average_demographic_density:,.2f}{Color.END}"

        elif current_option == 2:  # Metropolis
            city_string = "metrópoles"

            average_pop = self.metropolis["População"].mean()
            average_area = self.metropolis["Área"].mean()
            average_demographic_density = average_pop / average_area

            av_pop_text = f"{Color.BOLD}{average_pop:,.2f}{Color.END}"
            av_area_text = f"{Color.BOLD}{average_area:,.2f}{Color.END}"
            av_dem_text = f"{Color.BOLD}{
                average_demographic_density:,.2f}{Color.END}"

        elif current_option == 3:  # Large cities
            city_string = "grandes cidades"

            average_pop = self.largeCities["População"].mean()
            average_area = self.largeCities["Área"].mean()
            average_demographic_density = average_pop / average_area

            av_pop_text = f"{Color.BOLD}{average_pop:,.2f}{Color.END}"
            av_area_text = f"{Color.BOLD}{average_area:,.2f}{Color.END}"
            av_dem_text = f"{Color.BOLD}{
                average_demographic_density:,.2f}{Color.END}"

        print()  # Break line
        tools.print_item(
            f"A média da população entre as {
                city_string} é de {av_pop_text} pessoas"
        )
        tools.print_item(
            f"A média da área entre as {city_string} é {av_area_text} Km²"
        )
        tools.print_item(
            f"A média da densidade demográfica entre as {city_string} é {
                av_dem_text} Pessoas/Km²"
        )

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

    def find_city(self, search_string):
        result = self.expand_db[self.expand_db['Cidade'].str.contains(
            search_string, case=False, na=False)]

        return result

    def find_city_menu(self):
        tools.clear()
        search_string = input("Digite o nome da cidade que deseja buscar: ")
        result = self.find_city(search_string)

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


# Functions -----------------------------------------------------------
# ------------------------------------- DataBase manipulation Functions

def read_json_to_panda():
    """Read city_db.json file and fills the Panda's data base

    Returns:
        Data: DataBase
    """

    # Write the file path to the city_db.json on db directory
    FILE_PATH = os.path.join("db", "city_db.json")

    DataBase = pd.read_json(FILE_PATH)  # Fills Panda's data base from json
    return DataBase


def update_json_from_panda(data):
    """Update .json file from Panda's data abse

    Args:
        data (data): Panda's Data Frame
    """
    FILE_PATH = os.path.join("db", "city_db.json")

    # update Panda Data_base
    DataBase = pd.DataFrame(data)
    # Update .json file
    DataBase.to_json(FILE_PATH, orient='records', indent=4)


def Clean_DB():
    """Clear the .json file and Panda's data base
    """

    print(Color.BOLD, Color.RED,
          100 * "=",
          Color.END, sep="")

    user_input = input(f"{Color.BOLD}{Color.RED}[!] Atenção, você está prestes a apagar TODOS os dados da base de dados, deseja continuar? [y/n] [!]{Color.END}\n"
                       )
    if user_input.lower() == 'y':
        DataBase = read_json_to_panda()
        # Reinitialize the Data Base with these columns
        DataBase = pd.DataFrame(columns=["Cidade", "Área", "População"])
        update_json_from_panda(DataBase)
        read_json_to_panda()
        print("Base de dados apagada.")
        tools.confirm()
    else:
        return


def add_city(name, area, pop):
    """Add a city on the .json file

    Args:
        name (str): name of the city
        area (str): their area
        pop (str): their population
    """
    FILE_PATH = os.path.join("db", "city_db.json")

    new_city = {
        "Cidade": name,
        "Área": int(area),
        "População": int(pop)
    }

    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        try:
            # Load the JSON data into a Python dictionary
            data = json.load(file)
        except json.JSONDecodeError:
            # If the file is empty or not a valid JSON, initialize with an empty "Cidades" list
            data = {"Cidades": []}

        # Appending new_city into "Cidades" array
        data["Cidades"].append(new_city)

        # Updating the .json file.
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        read_json_to_panda()  # Update the Panda's Data base

        print(Color.GREEN, Color.BOLD,
              "[>>] Cidade adicionada com sucesso!",
              Color.END, sep="")
        tools.confirm()


def is_json_object_empty():
    """Verifies if a json file is empty
    """
    # Path to the .json files that will be verified
    FILE_PATH = os.path.join("db", "city_db.json")


def default_json_layout():
    FILE_PATH = os.path.join("db", "city_db.json")


# ------------------------------------------------------ Menu Functions


def display_data_menu():
    """ Open a menu for visualize_db options, uses ShowDB class
    """
    tools.clear()
    DataBase = ShowDB(read_json_to_panda())

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
            DataBase.print_average_statistics(1)
            DataBase.handle_sort_options(1)

    elif user_input == '2':  # Visualizar apenas metrópoles
        tools.clear()
        tools.session_header("Metrópoles")
        DataBase.print_metropolis()
        while True:
            DataBase.print_average_statistics(2)
            DataBase.handle_sort_options(2)

    elif user_input == '3':  # Visualizar apenas cidades com área > 1000 km²
        tools.clear()
        tools.session_header("Grandes cidades")
        DataBase.print_largeCities()
        while True:
            DataBase.print_average_statistics(3)
            DataBase.handle_sort_options(3)

    elif user_input == '4':  # Buscar cidade pelo nome
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
    """" Open a menu for add cities
    """
    DataBase = ShowDB(read_json_to_panda())

    cidade = ""
    area = ""
    populacao = ""

    while True:
        ERROR_FLAG = 0
        tools.clear()
        tools.session_header("Adicionar cidade")

        print(f"""
[1] Cidade: {cidade}
[2] Área: {area}
[3] População: {populacao}
[4] Confirma
[0] Voltar
    """)
        user_input = input("Selecione uma opção: ")

        if user_input == "1":  # Cidade
            cidade_cache = input("Digite o nome da cidade: ")

            # Check if a city already exists on data base
            if not DataBase.find_city(cidade_cache).empty:
                print(Color.RED, Color.BOLD,
                      f"Cidade '{
                          cidade_cache}' ja existe no nosso banco de dados.",
                      Color.END, sep=""
                      )
                tools.confirm()
            else:
                if cidade_cache.isdigit():
                    tools.input_error(cidade_cache)
                else:
                    cidade = cidade_cache

        elif user_input == "2":  # Área
            area_cache = input("Digite a área da cidade: ")
            if not area_cache.isdigit():
                tools.input_error(area_cache)
            else:
                area = area_cache

        elif user_input == "3":  # População
            populacao_cache = input("Digite a população da cidade: ")
            if not populacao_cache.isdigit():
                tools.input_error(populacao_cache)
            else:
                populacao = populacao_cache

        elif user_input == "4":  # Confirma

            # Prevents the user from input empty field
            if cidade == "":
                tools.empty_error("cidade")  # printa mensagem de erro
                ERROR_FLAG = 1
            if area == "":
                tools.empty_error("área")
                ERROR_FLAG = 1
            if populacao == "":
                tools.empty_error("população")
                ERROR_FLAG = 1

            if ERROR_FLAG == 0:
                add_city(cidade, area, populacao)  # add city
            else:
                tools.confirm()

        elif user_input == "0":  # Voltar
            main_menu()
        else:
            tools.input_error(user_input)


def main_menu():
    tools.clear()  # Clear the screen
    print(ASCII_ART)

    # A header to identify the current section
    tools.session_header("Menu Principal")

    options_display = """
[1] Acessar base de dados
[2] Inserir uma nova cidade
[3] Limpar a base de dados
[s] Sair
"""

    print(options_display)
    user_menu_input = input("Escolha uma opção: ")

    if user_menu_input == '1':
        display_data_menu()
    elif user_menu_input == '2':
        add_cidade_menu()
    elif user_menu_input == '3':
        Clean_DB()
    elif user_menu_input.lower() == "s":
        print(f"Até mais!")
        exit(0)
    else:
        tools.input_error(user_menu_input)


# Main -------------------------------------------------------------

while True:
    DataBase = read_json_to_panda()
    main_menu()
