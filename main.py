import os
import datetime

class Operadora:
    def __init__(self, nome, taxa):
        self.nome = nome
        self.taxa = taxa
        
    def __repr__(self):
        return f'Operadora(nome={self.nome}, taxa={self.taxa}%)'

class Venda:
    def __init__(self, valor_bruto, operadora):
        self.valor_bruto = valor_bruto
        self.operadora = operadora
        self.taxa = operadora.taxa if operadora else 0
        self.valor_liquido = self.valor_bruto - (self.valor_bruto) * ((operadora.taxa) / 100)
        
    def __repr__(self):
        return (f"Venda(valor_bruto=R${self.valor_bruto:.2f},"
                f"taxa={self.taxa}%, valor_liquido=R${self.valor_liquido:.2f})")

class Caixa:
    def __init__(self):
        self.operadoras = []
        self.vendas = []
    
    def cadastrar_operadora(self, nome, taxa):
        operadora = Operadora(nome, taxa)
        self.operadoras.append(operadora)
        return operadora
    
    def registrador_vendas(self, valor_bruto, operadora):
        venda = Venda(valor_bruto, operadora)
        self.vendas.append(venda)
        return venda
    
    def total_bruto(self):
        return sum(venda.valor_bruto for venda in self.vendas)
    
    def total_liquido(self):
        return sum(venda.valor_liquido for venda in self.vendas)
    
    def listar_vendas(self):
        for i in range(0, len(self.vendas)):
            venda = self.vendas[i]
            print(f"Venda {i + 1}: ")
            print(f"Valor bruto: R$ {venda.valor_bruto:.2f}")
            print(f"Taxa: {venda.taxa} %")
            print(f"Valor Líquido: R$ {venda.valor_liquido:.2f}")
            print("=-" * 30)
    
    def listar_operadoras(self):
        print("Operadoras cadastradas:")
        for i in range(0, len(self.operadoras)):
            operadoras = self.operadoras[i]
            print(f"{i + 1} - {operadoras.nome}, {operadoras.taxa} % de taxa")

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

# Entrada do usuário
nome_do_usuario = input(f'''{saudacao}! Qual o seu nome?
Digite seu nome: ''').capitalize()
limpar_tela()

caixa = Caixa()
pix = "Pix/Dinheiro"
taxa_pix = 0
caixa.cadastrar_operadora(pix, taxa_pix)







