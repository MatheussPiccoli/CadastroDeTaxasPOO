import os
# Função para limpar a tela do terminal em Linux e Windows
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')