# Importação das bibliotecas necessárias
from Interações import Mensagem 
from DataManagement import GerenciadorDados
import json
from time import sleep

# Lista de tipos de dados
Pessoa = ['Estudantes','Professores','Disciplinas','Turmas','Matriculas']

# Função para obter código com validação e verificação
def obter_codigo(esc1, Pessoa):
    while True:
        try:
            codigo = input(f'Me informe o código do(a) {Pessoa[esc1]}: ').strip()
            if not codigo.isdigit():
                print(Mensagem.error(1))
                continue
                
            validador = GerenciadorDados(esc1, Pessoa)
            if validador.existe(codigo):
                Mensagem.error(3)
                continue
            return codigo
        except Exception as e:
            print(f'Erro inesperado: {str(e)}')
            continue

class Operation:

    @staticmethod
    # Função para incluir novos registros
    def incluir(esc1, gerenciador):
            match esc1:
                case 0:  # Incluir Estudante
                    while True:
                        codigo = obter_codigo(esc1, Pessoa)
                        nome = input('Digite o nome do novo estudante: ').strip()
                        cpf = input('Me infome o CPF do estudante (somente números): ').strip()
                        gerenciador.adicionar(codigo, {'Nome': nome, 'CPF': cpf})
                        Mensagem.operacao(0)
                        if input('Deseja incluir outro registro (s/n): ').strip().lower() == "n":
                            break
                case 1:  # Incluir Professor
                    while True:
                            codigo = obter_codigo(esc1,Pessoa)
                            nome = input('Digite o nome do Professor: ').strip()
                            cpf = input('Digite o cpf do Professor: ').strip()
                            gerenciador.adicionar(codigo, {'Nome': nome, 'CPF': cpf})
                            Mensagem.operacao(0)
                            if input('Deseja incluir outro registro (s/n): ').strip().lower() == "n":
                                break 
                case 2:  # Incluir Disciplina
                    while True:
                        codigo = obter_codigo(esc1,Pessoa)
                        nome = input('Me informe o nome da disciplina: ')
                        gerenciador.adicionar(codigo, {'Nome': nome})
                        Mensagem.operacao(0)
                        if input('Deseja incluir outro registro (s/n): ').strip().lower() == "n":
                            break
                case 3:  # Incluir Turma
                    professores = GerenciadorDados(1, Pessoa)  # Índice 1 = Professores
                    disciplina = GerenciadorDados(2, Pessoa)  # Índice 2 = Disciplinas
                    while True:
                        codigo = obter_codigo(esc1,Pessoa)
                        try:
                            cod_Prof = int(input('Informe o Codígo do professor: ').strip())
                            cod_disc = int(input('Me informe o codígo da disciplina: ').strip())
                            if not professores.existe(cod_Prof):
                                print('Não encontrei o cadastro do professor.')
                            elif not disciplina.existe(cod_disc):
                                print('Não encontrei o cadastro da disciplina')
                            else:
                                print('Codigos Verificados!')
                                gerenciador.adicionar(codigo, {'Codigo do Professor': cod_Prof, 'Codigo da Diciplina': cod_disc})
                                Mensagem.operacao(0)
                        except ValueError:
                            print(Mensagem.error(1))
        
                        if input('Deseja incluir outro registro (s/n): ').strip().lower() == "n":
                            break 
                case 4:  # Incluir Matrícula
                    turmas = GerenciadorDados(3, Pessoa)  # Índice 3 = Turmas
                    estudantes = GerenciadorDados(0, Pessoa)  # Índice 0 = Estudantes
                    while True:
                        try:
                            cod_turma = int(input('Me informe o código da turma: ').strip())
                            cod_estudante = int(input('Me informe o código do estudante: ').strip())
                            if not turmas.existe(cod_turma):
                                print('Não encontrei o cadastro do turma.')
                                break
                            elif not estudantes.existe(cod_estudante):
                                print('Não encontrei o cadastro desse estudante')
                                break
                            else:
                                print('Codígos verificados!')
                                with open('Matriculas.json', 'r', encoding='utf-8') as f:
                                    codigo = len(json.load(f)) + 1
                                    gerenciador.adicionar(str(codigo), {'Codigo de Turma': cod_turma, 'Codigo do Estudante': cod_estudante})
                                    Mensagem.operacao(0)
                        except ValueError:
                            print(Mensagem.error(1))

                        if input('Deseja incluir outro registro (s/n): ').strip().lower() == "n":
                            break   

    @staticmethod
    # Função para listar registros
    def listar(esc1, gerenciador):
        sleep(0.5)
        dados = gerenciador.listar()

        if not dados:
            print(f'\nNão há {Pessoa[esc1]} cadastrados.\n')
        else:
            Mensagem.cabecalho(f'Listagem de {Pessoa[esc1]}')
            for codigo, dados in dados.items():
                print(f'Código: {codigo}')
                match esc1:
                    case 0 | 1:  # Estudante ou Professor
                        print(f"Nome: {dados['Nome']}")
                        print(f"CPF: {dados['CPF']}")
                    case 2:  # Disciplina
                        print(f"Nome: {dados['Nome']}")  
                    case 3:  # Turma
                        print(f"Código do Professor: {dados['Codigo do Professor']}")
                        print(f"Código da Disciplina: {dados['Codigo da Disciplina']}")
                    case 4:  # Matrícula
                        print(f"Código da Turma: {dados['Codigo de Turma']}")
                        print(f"Código do Estudante: {dados['Codigo do Estudante']}")
                print(Mensagem.linha()) 
        sleep(0.3)
                
    @staticmethod
        # Função para atualizar registros
    def atualizar(esc1, gerenciador):
        Mensagem.cabecalho(f"Atualizando dados do(a) {Pessoa[esc1]}")
        att = input(f"Me informe o codigo do(a) {Pessoa[esc1]}: ").strip()
        sleep(0.3)
        if gerenciador.existe(att):
            match esc1:
                case 0 | 1:  # Atualizar Estudante ou Professor
                    att_nome = input('Me informe o novo nome: ').strip()
                    att_cpf = input(f'Me informe o CPF do(a) estudante: ').strip()
                    gerenciador.atualizar(att, {'Nome': att_nome, 'CPF': att_cpf})
                    Mensagem.operacao(1)
                case 2:  # Atualizar Disciplina
                    att_nome = input('Me informe o novo nome: ').strip()
                    gerenciador.atualizar(att, {'Nome': att_nome})
                    Mensagem.operacao(1)
                case 3:  # Atualizar Turma
                    cod_professores = GerenciadorDados(1, Pessoa)  # Índice 1 = Professores
                    cod_disciplina = GerenciadorDados(2, Pessoa)  # Índice 2 = Disciplinas
                    try:
                        att_cod_Prof = int(input('Informe o Codígo do professor: ').strip())
                        att_cod_disc = int(input('Me informe o codígo da disciplina: ').strip())
                        if not cod_professores.existe(att_cod_Prof):
                            print('Não encontrei o cadastro do professor.')
                        elif not cod_disciplina.existe(att_cod_disc):
                            print('Não encontrei o cadastro da disciplina')
                        else:
                            print('Codigos Verificados!')
                            gerenciador.atualizar(att, {'Codigo do Professor': att_cod_Prof, 'Codigo da Disciplina': att_cod_disc})
                            Mensagem.operacao(1)
                    except ValueError:
                        print(Mensagem.error(1))

                case 4:  # Atualizar Matrícula
                    cod_turmas = GerenciadorDados(3, Pessoa)  # Índice 3 = Turmas
                    cod_estudantes = GerenciadorDados(0, Pessoa)  # Índice 0 = Estudantes

                    try:
                        att_cod_turma = int(input('Me informe o código da turma: ').strip())
                        att_cod_estudante = int(input('Me informe o código do estudante: ').strip())
                        if not cod_turmas.existe(att_cod_turma):
                            print('Não encontrei o cadastro do turma.')
                        elif not cod_estudantes.existe(att_cod_estudante):
                            print('Não encontrei o cadastro desse estudante')
                        else:
                            print('Codígos verificados!')
                            gerenciador.atualizar(att, {'Codigo de Turma': att_cod_turma, 'Codigo do Estudante': att_cod_estudante})
                            Mensagem.operacao(1)
                    except ValueError:
                        print(Mensagem.error(1))
        else:
            Mensagem.error(0)

    @staticmethod
        # Função para excluir registros
    def excluir(esc1, gerenciador):
        delete = input(f'Me informe o código do(a) {Pessoa[esc1]} que deseja excluir: ').strip()
        if gerenciador.existe(delete):
            confirmacao = input(f'Você tem certeza que deseja excluir o(a) {Pessoa[esc1]} de código {delete}:\n(s/n): ').strip().lower()
            if confirmacao == 's':
                gerenciador.remover(delete)
                Mensagem.operacao(2)
            else:
                Mensagem.error(2)
        else:
            Mensagem.error(0)
