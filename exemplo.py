from numpy import median
import localPackage as tools
cidade = ""
area = ""
populacao = ""

while True:
    tools.clear()
    tools.session_header("exemplo")

    print(f"""
[1] Cidade: {cidade}
[2] Área: {area}
[3] População: {populacao}
[4] Confirma
[0] Voltar 
""")
    user_input = input("Selecione uma opção: ")

    if user_input == "1":
        cidade = input("Digite o nome da cidade: ")

    elif user_input == "2":
        area = input("Digite a área da cidade: ")

    elif user_input == "3":
        populacao = input("Digite a população da cidade: ")

    elif user_input == "4":
        ...

    elif user_input == "0":
        exit(0)

    else:
     tools.input_error(user_input)
 
        # MENU DAS MÉDIAS #
media_populacao = ""
media_tamanhos = ""
 
while True:
    tools.clear()
    tools.session_header("medias")
     
    print(f"""
[1] Média da População: {media_populacao}
[2] Média dos Tamanhos: {media_tamanhos} 
[4] Confirma
[0] Volta          
 """)
    user_input = input("Selecione uma opção: ")
    
    if user_input == "1":
        ...
    elif user_input == "2":
        ...
    elif user_input == "3":
        ...
    elif  user_input == "4":
        ...
    elif user_input == "0":
        ...
