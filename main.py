import os
import datetime

# Função para limpar a tela do terminal em Linux e Windows
def limpar_tela():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')

# Saudação por horário
horario = datetime.datetime.now().hour
manha = -1 < horario < 12
tarde = 11 < horario < 18
noite = 18 < horario < 24
if manha:
    saudacao = 'Bom dia'
elif tarde:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'




