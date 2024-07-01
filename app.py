import os


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


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: ")) #Retornando uma String e convertendo para inteiro usando apenas uma linha
    #opcao_escolhida = int(opcao_escolhida) # Convertendo para um valor int

    print(f"Você escolheu a opção :{opcao_escolhida}")

    if opcao_escolhida == 1:
        print("Cadastrar restaurante")

    elif opcao_escolhida == 2:
        print("Listar restaurantes")

    elif opcao_escolhida == 3:
        print("Ativar restaurante")

    elif opcao_escolhida == 4:
        finalizar_app()

    else:
        print("Opção invalida!")




def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()