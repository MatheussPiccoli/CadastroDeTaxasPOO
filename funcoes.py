import os
import datetime

# Função para limpar a tela do terminal em Linux e Windows
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

def saudacao_horario():
    horario = datetime.datetime.now().hour
    if 4 <= horario and 12 > horario:
        return 'Bom dia'
    elif 12 <= horario and 18 > horario:
        return "Boa tarde"
    else:
        return "Boa noite"
        

def obter_inteiro(limite=100):
    while True:
        numero = input("Digite um número inteiro: ")
        try:
            numero = int(numero)
            if numero <= limite and numero >= 0:
                return numero
            else:
                print(f"Valor inválido. Por favor, entre com um número entre 1 e {limite}")
        
        except ValueError:
            print("Entrada inválida. A entrada não é um número inteiro")
            

def obter_real(limite=100):
    while True:
        numero = input("Digite um número (Use '.' para separar a parte decimal): ")
        try:
            numero = float(numero)
            if numero >= 0 and numero <= limite:
                return numero
            else:
                print("Valor inválido. Por favor, entre com um número entre 0 e 100.")
        
        except ValueError:
            print("Entrada inválida. A entrada não é um Número real.")

