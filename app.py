import os

restaurantes = []

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
          ''')


def exibir_opcoes():
    print("[01] Cadastrar Restaurante")
    print("[02] Listar Restaurantes")
    print("[03] Ativar Restaurante")
    print("[04] Sair\n")

def finalizar_app():
    os.system('cls')
    print("Finalizando o APP")
    os._exit(0)

def opcao_invalida():
    print("Opção invalida!")
    input("Digite uma tecla para voltar ao menu principal")
    main()

def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("Digite uma tecla para voltar ao menu principal")
    main()

def listar_restaurantes(restaurantes):
    for restaurante in restaurantes:
        print(restaurante)

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: ")) #Retornando uma String e convertendo para inteiro usando apenas uma linha
        #opcao_escolhida = int(opcao_escolhida) # Convertendo para um valor int

        print(f"Você escolheu a opção :{opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes(restaurantes)

        elif opcao_escolhida == 3:
            print("Ativar restaurante")

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            
            opcao_invalida()
    except:
        opcao_invalida()



def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()