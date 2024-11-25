import os
import datetime
import funcoes
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
        numero_de_operadoras = (input('Digite o número de operadoras que você que cadastrar: ("0" para voltar ao menu)'))
        validar_numero_de_operadoras = numero_de_operadoras.isdigit()
        if validar_numero_de_operadoras:
            numero_de_operadoras = int(numero_de_operadoras)
            contador_de_taxas = 0
            if numero_de_operadoras == 0:
                print("Voltando ao menu prinicpal")
                sleep(2)
                continue
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
    
    #Incluir venda - 2
    elif menu == '2':
        print('Você selecionou a opção INCLUIR VENDA')
        sleep(1)
        caixa.listar_operadoras()
        print('Selecione a operadora da venda ("0" para voltar ao menu)')
        sleep(1)
        operadora_escolhida = int(input(caixa.operadoras))
        if operadora_escolhida == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        operadora_venda = caixa.operadoras[operadora_escolhida - 1]
        taxa_operadora = operadora_venda.taxa
        print(f'Você selecionou a operadora {operadora_venda}.')
        sleep(1)
        print('Qual é o valor da venda?')
        valor_bruto_venda = float(input("Digite o valor da venda: "))
        nova_venda = caixa.registrador_vendas(valor_bruto_venda, operadora_venda)
        print(f'Venda de R${valor_bruto_venda} cadastrada!')
        sleep(1)
        print(f'Taxa da maquina: {taxa_operadora}%')
        sleep(1)
        print(f'Valor líquido: R${nova_venda.valor_liquido:.2f}')
        sleep(2)
        funcoes.limpar_tela

    #Atualizar taxa - 3
    elif menu == '3':
        print("Você selecionou a opção ATUALIZAR TAXAS")
        sleep(1)
        caixa.listar_operadoras()
        print("Qual operadora você deseja atualizar? ('0' para voltar ao menu)")
        select = int(input(caixa.operadoras))
        if select == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        operadora_escolhida = caixa.operadoras[select - 1]
        print(f"Você selecionou a operadora {operadora_escolhida} ")
        nova_taxa =  input("Digite a nova taxa da operadora selecionada: ")
        caixa.atualizar_taxa(select, nova_taxa)
        print(f"Operadora {operadora_escolhida.nome} atualizada com sucesso! A taxa nova é de {operadora_escolhida.taxa}%")
        sleep(2)
        funcoes.limpar_tela()

    else:
        print('Opção inválida.')
        sleep(2)
        limpar_tela()







