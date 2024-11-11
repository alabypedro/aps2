import pandas as pd  # Banco de dados
import localPackage as tools  # tools.py
import os      # Pacote de operações do sistema
import json    # Arquivos .json
import time


class Color:
    # Apenas adiciona cores para strings.
    
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


def print_cities_DB_title():
    tools.clear()
    ASCII_TITLE = f"""{Color.CYAN}

                 ██████╗██╗████████╗██╗███████╗███████╗    ██████╗ ██████╗
                ██╔════╝██║╚══██╔══╝██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗
                ██║     ██║   ██║   ██║█████╗  ███████╗    ██║  ██║██████╔╝
                ██║     ██║   ██║   ██║██╔══╝  ╚════██║    ██║  ██║██╔══██╗
                ╚██████╗██║   ██║   ██║███████╗███████║    ██████╔╝██████╔╝
                 ╚═════╝╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═════╝{Color.END}{Color.BOLD}

                             Database para estudos demográficos
                                            by
                        Gabriel Morais, Graziela Lopes, Pedro Alaby{Color.END}
"""
    print("\033[?25l", end='', flush=True)  # Oculta o cursor
    print(ASCII_TITLE)
    time.sleep(1.75)
    print("\033[?25h", end='', flush=True)  # Restaura o cursor


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


class DbHandler:
    # Classe usada para lidar com a opção "Visualizar Base de Dados" no menu principal
    
    def __init__(self, data):
        self.expand_db = pd.json_normalize(data['Cidades'])
        self.metropolis = self.expand_db[self.expand_db['População'] > 1000000]
        self.largeCities = self.expand_db[self.expand_db['Área'] > 1000]

    # Funções de impressão
    def print_cities(self):
        print(self.expand_db)

    def print_metropolis(self):
        print(self.metropolis)

    def print_largeCities(self):
        print(self.largeCities)

    def print_average_statistics(self, current_option):
        """
        Calcula e imprime estatísticas médias das cidades com base em "opção_atual"
            opção_atual == 1: Todo o banco de dados
            opção_atual == 2: Somente metrópoles
            opção_atual == 3: Somente grandes cidades

        Args:
            Args: número correspondente à opção atual do menu "exibir_dados"
        """

        if current_option == 1:  # Todas as cidades
            # Usado na saída para identificar o tipo de cidade para a opção atual
            city_string = "cidades"

            average_pop = self.expand_db["População"].mean()
            average_area = self.expand_db["Área"].mean()
            average_demographic_density = average_pop / average_area

            av_pop_text = f"{Color.BOLD}{average_pop:,.2f}{Color.END}"
            av_area_text = f"{Color.BOLD}{average_area:,.2f}{Color.END}"
            av_dem_text = f"{Color.BOLD}{
                average_demographic_density:,.2f}{Color.END}"

        elif current_option == 2:  # Metrópoles
            city_string = "metrópoles"

            average_pop = self.metropolis["População"].mean()
            average_area = self.metropolis["Área"].mean()
            average_demographic_density = average_pop / average_area

            av_pop_text = f"{Color.BOLD}{average_pop:,.2f}{Color.END}"
            av_area_text = f"{Color.BOLD}{average_area:,.2f}{Color.END}"
            av_dem_text = f"{Color.BOLD}{
                average_demographic_density:,.2f}{Color.END}"

        elif current_option == 3:  # Grandes cidades
            city_string = "grandes cidades"

            average_pop = self.largeCities["População"].mean()
            average_area = self.largeCities["Área"].mean()
            average_demographic_density = average_pop / average_area

            av_pop_text = f"{Color.BOLD}{average_pop:,.2f}{Color.END}"
            av_area_text = f"{Color.BOLD}{average_area:,.2f}{Color.END}"
            av_dem_text = f"{Color.BOLD}{
                average_demographic_density:,.2f}{Color.END}"

        print()  # Quebra de linha
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

    # Opções de ordenação
    # user_input usa argumento padrão
    def handle_sort_options(self, current_option, user_input='4'):
        """
        Lida com as opções de ordenação disponíveis na seção "Visualizar Base de Dados"

        Args:
            a seção entre "Todas as cidades / metrópoles / área"

        Returns:
            function: If user_option == 0 returns visualize_db()
        """

        # Manipula as opções de "Visualizar todas as cidades"
        if current_option == 1:
            # Variáveis que lidam com o resultado ordenado
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

        print("\nOrganizar por: ")
        print("[1] A-Z [2] Área (km²) [3] População [4] Índice [0] 0 para voltar")
        user_cache = input("Digite a opção desejada: ")

        # Precisamos verificar uma entrada válida
        if user_cache.isdigit() and int(user_cache) in range(0, 5):  # range 0,5 because range(i,j) = (i, j-1)
            user_input = user_cache  # if user_cache is valid user_input = user_cache

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
        else:  # else, chamada recursiva com a última opção válida
            tools.input_error(user_cache)
            display_data_menu(previous_input=current_option)

    def find_city(self, search_string):
        result = self.expand_db[self.expand_db['Cidade'].str.contains(
            search_string, case=False, na=False)]

        return result

    def find_city_menu(self):
        tools.clear()
        search_string = input("Digite o nome da cidade que deseja buscar: ")
        result = self.find_city(search_string)

        # Verifica se o resultado está vazio
        if result.empty:
            print(Color.BOLD, Color.RED,
                  f"Não foi possível encontrar '{
                      search_string}' na base de dados",
                  Color.END, sep="")
        else:
            print()  # Nova linha
            tools.session_header(
                "Resultado ==============================")
            print("\n", result, sep="")

            # Comprimento da string
            print("\n", Color.BOLD, 45 * "=", Color.END, sep="")


# Functions -----------------------------------------------------------
# ------------------------------------- Funções de manipulação do banco de dados

def read_json_to_panda():
    """
    Lê o arquivo city_db.json e preenche o banco de dados do Panda

    Returns:
        Data: DataBase
    """

    # Escreva o caminho do arquivo para o city_db.json no diretório db
    FILE_PATH = os.path.join("db", "city_db.json")

    DataBase = pd.read_json(FILE_PATH)  # Preenche o banco de dados do Panda a partir do JSON
    return DataBase


def update_json_from_panda(data):
    """
    Atualiza o arquivo json a partir do banco de dados do Panda

    Args:
        data (data): Panda's Data Frame
    """
    FILE_PATH = os.path.join("db", "city_db.json")

    # update Panda Data_base
    DataBase = pd.DataFrame(data)
    # Update .json file
    DataBase.to_json(FILE_PATH, orient='records', indent=4)


def Clean_DB():
    #Limpa o arquivo .json e o banco de dados do Panda
    FILE_PATH = os.path.join("db", "city_db.json")
    default_layout = {
        "Cidades": [
            {
                "Cidade": None,
                "Área": None,
                "População": None
            }
        ]
    }

    print(Color.BOLD, Color.RED,
          100 * "=",
          Color.END, sep="")

    user_input = input(f"{Color.BOLD}{Color.RED}[!] Atenção, você está prestes a apagar TODOS os dados da base de dados, deseja continuar? [y/n] [!]{Color.END}\n")
    if user_input.lower() == 'y':
        DataBase = read_json_to_panda()
        # Reiniciliza o Banco de Dados com estas colunas
        DataBase = pd.DataFrame(columns=["Cidade", "Área", "População"])
        update_json_from_panda(DataBase)
        read_json_to_panda()
        print("Base de dados apagada.")
        tools.confirm()

        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(default_layout, file, indent=4)
    else:
        return


def add_city(name, area, pop):
    """
    Adiciona uma cidade no arquivo .json

    Args:
        name (str): nome da cidade
        area (str): sua área
        pop (str): sua população
    """
    FILE_PATH = os.path.join("db", "city_db.json")

    new_city = {
        "Cidade": name,
        "Área": int(area),
        "População": int(pop)
    }

    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        try:
            # Carrega os dados JSON em um dicionário Python
            data = json.load(file)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio ou não for um JSON válido, inicializa com uma lista "Cidades" vazia
            data = {"Cidades": []}

        # Adicionando nova_cidade na matriz "Cidades" (array)
        data["Cidades"].append(new_city)

        # Atualizando o arquivo .json
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        read_json_to_panda()  # Atualiza o banco de dados do Panda

        print(Color.GREEN, Color.BOLD,
              "[>>] Cidade adicionada com sucesso!",
              Color.END, sep="")
        tools.confirm()


def is_json_empty():
    # Verifica se o arquivo JSON está vazio
    
    # Caminho para os arquivos .json que serão verificados
    FILE_PATH = os.path.join("db", "city_db.json")


def default_json_layout():
    FILE_PATH = os.path.join("db", "city_db.json")


# ------------------------------------------------------ Menu Functions


def display_data_menu(previous_input=False):
    """ 
    Menu para visualizar opções do banco de dados, usa a classe ShowDB

    Args:
        previous_input=False (boolean): argumento configurado como False por padrão,
        usado para chamar a função na mesma opção em que o usuário estava anteriormente.
        (usado para corrigir bug) em DbHandler.sortHandler().
    """
    tools.clear()
    DataBase = DbHandler(read_json_to_panda())

    if previous_input == False:

        tools.session_header("Base de Dados")

        options_display = """
[1] Visualizar todas as cidades
[2] Visualizar apenas metrópoles
[3] Visualizar apenas cidades com área > 1000 km²
[4] Buscar cidade pelo nome
[0] Voltar
[s] Sair
    """

        print(options_display)
        user_input = input("Escolha uma opção: ")
    else:
        user_input = str(previous_input)

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
        display_data_menu()  # Função chamada recursivamente - evita o retorno ao menu principal


def add_cidade_menu():
    
    # Abre um menu para adicionar cidades
    
    DataBase = DbHandler(read_json_to_panda())

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

            # Verifica se uma cidade já existe no banco de dados
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

            # Impede que o usuário insira um campo vazio
            if cidade == "":
                tools.empty_error("cidade")  # exibe mensagem de erro
                ERROR_FLAG = 1
            if area == "":
                tools.empty_error("área")
                ERROR_FLAG = 1
            if populacao == "":
                tools.empty_error("população")
                ERROR_FLAG = 1

            if ERROR_FLAG == 0:
                add_city(cidade, area, populacao)  # Adiciona cidade
            else:
                tools.confirm()

        elif user_input == "0":  # Voltar
            main_menu()
        else:
            tools.input_error(user_input)


def main_menu():
    tools.clear()  # Limpa a tela
    print(ASCII_ART)
    # print(ASCII_TITLE)

    # Cabeçalho para identificar a seção atual
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
        # tools.print_in_development()
        Clean_DB()
    elif user_menu_input.lower() == "s":
        print(f"Até mais!")
        exit(0)
    else:
        tools.input_error(user_menu_input)


# Main -------------------------------------------------------------
print_cities_DB_title()

while True:
    DataBase = read_json_to_panda()
    main_menu()
