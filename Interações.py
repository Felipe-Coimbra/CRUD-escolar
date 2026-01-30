from time import sleep
#Classe que Estiliza e envia mensagens de acordo com um indice
class Mensagem:
    @staticmethod
    #Envia mensagens de erro a um codigo
    def error(k):
        match k:
            case 0:  # Número inválido
                print("O número digitado está incorreto, verifique o número e tente novamente") 
            case 1:  # Entrada não numérica
                return 'Digite apenas Números!'
            case 2:  # Operação cancelada
                print('\nOperação cancelada!')
            case 3:  # Erro do código existente
                print('O código já existe, cadastre outro codigo!')

    @staticmethod
    #Envia mensagens de operações sendo realizadas, para melhor interatividade
    def operacao(k):
        match k:
            case 0:  # Inclusão
                print('Incluindo...')
                sleep(2)
                print('\nOperação concluída com êxito!')
                sleep(0.5)
            case 1:  # Atualização
                print('Atualizando...')
                sleep(1)
                print('\nOperação concluída com êxito!')
            case 2:  # Exclusão
                print('Excluindo...')
                sleep(1)
                print('\nOperação concluída com êxito!')

    @staticmethod
    #Função filha da função Cabeçalho
    def linha(tam=42):
        return '=' * tam

    @staticmethod
    #Função para estetica do codigo
    def cabecalho(txt):
        print(Mensagem.linha())
        print(txt.center(42))
        print(Mensagem.linha())


