---

# Sabor Express

Sabor Express é um aplicativo de terminal para gerenciar restaurantes, permitindo cadastrar, listar e ativar restaurantes. Este projeto é desenvolvido em Python.

## Funcionalidades

- **Cadastrar Restaurante**: Permite o cadastro de novos restaurantes.
- **Listar Restaurantes**: Exibe uma lista de restaurantes cadastrados.
- **Ativar Restaurante**: Permite ativar restaurantes específicos.
- **Sair**: Finaliza o aplicativo.

## Estrutura do Projeto

- `exibir_nome_do_programa()`: Exibe o nome do programa com uma arte ASCII.
- `exibir_opcoes()`: Exibe as opções disponíveis no menu.
- `finalizar_app()`: Limpa o terminal e finaliza o aplicativo.
- `escolher_opcao()`: Lê a opção escolhida pelo usuário e chama a função correspondente.
- `main()`: Função principal que orquestra a execução do programa.

## Pré-requisitos

- Python 3.6 ou superior

## Como Executar

1. Clone o repositório:

   ```sh
   git clone https://github.com/seuusuario/sabor-express.git
   cd sabor-express
   ```

2. Execute o programa:

   ```sh
   python app.py
   ```

## Exemplo de Uso

```sh
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
          
[01] Cadastrar Restaurante
[02] Listar Restaurantes
[03] Ativar Restaurante
[04] Sair

Escolha uma opção: 1
Você escolheu a opção :1
Cadastrar restaurante
```
