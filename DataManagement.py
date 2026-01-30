import json # Para manipulação de arquivos JSON

# Classe responsável por gerenciar os dados (CRUD)
class GerenciadorDados:
    def __init__(self, tipo, Pessoa):
        self.tipo = tipo  # Tipo de dado (Estudante, Professor, etc)
        self.arquivo = f"{Pessoa[tipo]}.json"  # Nome do arquivo JSON
        self.dados = self.carregar_dados()  # Carrega os dados do arquivo

    def carregar_dados(self):
        # Carrega os dados do arquivo JSON
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}  # Retorna dicionário vazio se arquivo não existir

    def salvar_dados(self):
        # Salva os dados no arquivo JSON
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, indent=4)

    def adicionar(self, codigo, dados):
        # Adiciona um novo registro
        self.dados[codigo] = dados
        self.salvar_dados()

    def remover(self, codigo):
        # Remove um registro existente
        if codigo in self.dados:
            del self.dados[codigo]
            self.salvar_dados()
            return True
        return False

    def atualizar(self, codigo, dados):
        # Atualiza um registro existente
        if codigo in self.dados:
            self.dados[codigo].update(dados)
            self.salvar_dados()
            return True
        return False

    def listar(self):
        # Retorna todos os registros
        return self.dados

    def existe(self, codigo):
        # Verifica se um código existe
        return str(codigo) in self.dados