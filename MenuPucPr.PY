# Importação das bibliotecas necessárias
from Interações import Mensagem #Exibir Mensagens de interações de sucesso ou erro
from DataManagement import GerenciadorDados #Para gerenciar os dados coletados
from Operações import Operation #Para realizar as devidas operações
from time import sleep  # Para adicionar pausas no programa

# Listas de opções do sistema
Pessoa = ['Estudantes','Professores','Disciplinas','Turmas','Matriculas']  # Tipos de dados
Operacao = ['Incluir', 'Listar', 'Atualizar', 'Excluir', 'Sair']  # Operações disponíveis


# Menu principal do sistema
def Menu_Principal():
    while True:
        Mensagem.cabecalho('Menu Principal')
        c = 0
        # Exibe as opções do menu principal
        for c in range(5):
            print(f'{c} - Gerenciar {Pessoa[c]}')
            c += 1
        print('5 - Sair do programa')
        try:
            esc1 = int(input('\nDigite o número do menu que você deseja acessar: ').strip())
            if 0 <= esc1 <= 4:  # Opções de gerenciamento
                Menu_Operacoes(esc1)
            elif esc1 == 5:  # Sair do programa
                sleep(3)
                print(Mensagem.linha())
                print('Você decidiu sair, até breve'.center(42))
                print(Mensagem.linha())
                break
            else:
                Mensagem.error(0)
        except ValueError:
            Mensagem.cabecalho(Mensagem.error(1))

# Menu de operações (CRUD)
def Menu_Operacoes(esc1):
    gerenciador = GerenciadorDados(esc1, Pessoa)
    while True:
        c = 0
        Mensagem.cabecalho(f'Menu de Operações - {Pessoa[esc1]}')
        # Exibe as opções de operações
        for c in range(5):
            print(f'{c} - {Operacao[c]}')
            c += 1
        try:
            esc2 = int(input('\nMe informe o número da operação: '))

            match esc2:
                case 0:  # Incluir
                    Operation.incluir(esc1, gerenciador)
                case 1:  # Listar
                    Operation.listar(esc1, gerenciador)
                case 2:  # Atualizar
                    Operation.atualizar(esc1, gerenciador)
                case 3:  # Excluir
                    Operation.excluir(esc1, gerenciador)
                case 4:  # Voltar ao menu principal
                    print('Voltando ao menu principal...')
                    sleep(1)
                    return
                case _:  # Opção inválida
                    Mensagem.error(0)
        except ValueError:
            Mensagem.cabecalho(Mensagem.error(1))

# Inicialização do programa
Menu_Principal()