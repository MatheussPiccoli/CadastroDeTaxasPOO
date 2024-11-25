import os
import datetime
from time import sleep
from caixa import Caixa
from funcoes import limpar_tela

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

#Menu Principal
while True:
    menu = input(f''' Bem vindo(a) {nome_do_usuario}!
[1] Cadastrar taxas
[2] Incluir nova venda
[3]Atualizar taxas
[4]Excluir operadora
[5]Excluir venda
[6]Fechar caixa
Selecione uma opção''')
    os.system('cls')
    #cadastro taxas - 1
    if menu == '1':
        print("Você selecionou a opção CADASTRAR TAXAS")
        sleep(1)
        numero_de_operadoras = (input('Digite o número de operadoras que você que cadastrar: '))
        validar_numero_de_operadoras = numero_de_operadoras.isdigit()
        if validar_numero_de_operadoras:
            numero_de_operadoras = int(numero_de_operadoras)
            contador_de_taxas = 0
            while contador_de_taxas<numero_de_operadoras:
                operadora_nova = input(f'Digite o nome da operadora {contador_de_taxas + 1}: ').upper()
                taxa_operadora = float(input('Digite a porcentagem da taxa (apenas numeros): '))
                caixa.cadastrar_operadora(operadora_nova, taxa_operadora)
                contador_de_taxas += 1
                print(f'Operadora {operadora_nova} cadastrada! Taxa de {taxa_operadora}%')
                sleep(2)
                limpar_tela()
            print('Todas as operadoras foram cadastradas.')
            sleep(1)
            limpar_tela()
        else:
            print('Opção inválida.')
            sleep(2)
            limpar_tela()







