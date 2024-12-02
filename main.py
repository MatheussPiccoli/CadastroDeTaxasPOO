import funcoes
from time import sleep
from caixa import Caixa
import sys

from venda import Venda

# Entrada do usuário
nome_do_usuario = input(f'''{funcoes.saudacao_horario()}! Qual o seu nome?
Digite seu nome: ''').capitalize()
funcoes.limpar_tela()

caixa = Caixa()
pix = "Pix/Dinheiro"
taxa_pix = 0
caixa.cadastrar_operadora(pix, taxa_pix)

menu = '0'
#Menu Principal
while menu != '7':
    menu = input(f'''Bem vindo(a) {nome_do_usuario}!
[1] Cadastrar taxas
[2] Incluir nova venda
[3] Atualizar taxas
[4] Excluir operadora
[5] Excluir venda
[6] Registrar Chargeback
[7] Fechar caixa
Selecione uma opção: ''')
    funcoes.limpar_tela()

    #cadastro taxas - 1
    if menu == '1':
        print("Você selecionou a opção CADASTRAR TAXAS")
        sleep(1)
        print('Escolha o número de operadoras que você quer cadastrar ("0" para voltar ao menu)')
        n_de_operadoras = funcoes.obter_inteiro()
        if n_de_operadoras == 0:
            print("Voltando ao menu principal")
            sleep(2)
            continue
        for i in range(n_de_operadoras):
            operadora_nova = input(f'Digite o nome da operadora {i + 1}: ').upper()
            print('Qual seria a porcentagem da taxa?')
            taxa_operadora = funcoes.obter_real()
            caixa.cadastrar_operadora(operadora_nova, taxa_operadora)
            print(f'Operadora {operadora_nova} cadastrada! Taxa de {taxa_operadora}%')
        print('Todas as operadoras foram cadastradas.') 
        sleep(1)
        funcoes.limpar_tela()
    
    #Incluir venda - 2
    elif menu == '2':
        print('Você selecionou a opção INCLUIR VENDA')
        sleep(1)
        caixa.listar_operadoras()
        print('Selecione a operadora da venda ("0" para voltar ao menu)')
        sleep(1)
        operadora_escolhida = funcoes.obter_inteiro(len(caixa.operadoras))
        if operadora_escolhida == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        operadora_venda = caixa.operadoras[operadora_escolhida - 1]
        taxa_operadora = operadora_venda.taxa
        print(f'Você selecionou a operadora {operadora_escolhida}.')
        sleep(1)
        print('Qual é o valor da venda?')
        valor_bruto_venda = funcoes.obter_real(sys.float_info.max)
        nova_venda = caixa.registrador_vendas(valor_bruto_venda, operadora_venda)
        print(f'Venda de R${valor_bruto_venda} cadastrada!')
        sleep(1)
        print(f'Taxa da maquina: {taxa_operadora}%')
        sleep(1)
        print(f'Valor líquido: R${nova_venda.valor_liquido:.2f}')
        sleep(3)
        funcoes.limpar_tela()

    #Atualizar taxa - 3
    elif menu == '3':
        print("Você selecionou a opção ATUALIZAR TAXAS")
        sleep(1)
        if len(caixa.operadoras) == 1:
            print("Não há operadoras cadastradas. Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue 
        caixa.listar_operadoras(1)
        print("Qual operadora você deseja atualizar? ('0' para voltar ao menu)")
        sleep(1)
        select = funcoes.obter_inteiro(len(caixa.operadoras) - 1)
        if select == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        operadora_escolhida = caixa.operadoras[select - 1]
        print(f"Voce selecionou a operadora {operadora_escolhida.nome} ")
        print("Digite a nova taxa da operadora selecionada")
        nova_taxa = funcoes.obter_real()
        caixa.atualizar_taxa(select, nova_taxa)
        print(f"Operadora {operadora_escolhida.nome} atualizada com sucesso! A taxa nova é de {operadora_escolhida.taxa}%")
        sleep(2)
        funcoes.limpar_tela()
    
    #Excluir operadora - 4
    elif menu == '4':
        print("Você selecionou a opção EXCLUIR OPERADORA")
        sleep(1)
        if len(caixa.operadoras) == 1:
            print("Não há operadoras cadastradas. Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        caixa.listar_operadoras(1)
        print("Escolha o número da operadora a ser excluída ('0' para voltar ao menu)")
        delete_operadora = funcoes.obter_inteiro(len(caixa.operadoras) - 1)
        if delete_operadora == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        operadora_excluida = caixa.excluir_operadora(delete_operadora)
        print(f"Operadora {operadora_excluida.nome} excluída com sucesso!")
        sleep(2)
        funcoes.limpar_tela()
    
    # Excluir Venda - 5
    elif menu == '5':
        print("Você selecionou a opção EXCLUIR VENDA")
        sleep(1)
        if len(caixa.vendas) == 0:
            print("Não há nenhuma venda cadastradas. Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        caixa.listar_vendas()
        print("Escolha o número da venda a ser excluída ('0' para voltar ao menu)")
        delete_venda = funcoes.obter_inteiro(len(caixa.vendas))
        if delete_venda == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        venda_excluida = caixa.excluir_venda(delete_venda)
        print(f"Venda {delete_venda} excluída com sucesso!")
        sleep(2)
        funcoes.limpar_tela()
    
    # Registrar Chargeback - 6
    
    elif menu == '6':
        print("Você selecionou a opção REGISTRAR CHARGEBACK")
        sleep(1)

        print("Qual o valor da venda cancelada? (Digite 0 para voltar ao menu)")
        valor_venda = funcoes.obter_real(sys.float_info.max)
        if valor_venda == 0:
            print("Voltando ao menu principal")
            sleep(2)
            funcoes.limpar_tela()
            continue
        
        print("Digite o NSU (número do comprovante) da venda:")
        nsu = input("NSU: ")

        print("Digite a data da venda (DD/MM/AAAA):")
        data_venda = input("Data: ")

        print("Digite o motivo do chargeback:")
        motivo = input("Motivo: ").capitalize()
        
        # Criamos uma venda temporária para passar ao chargeback
        venda = Venda(valor_venda, "Cancelamento", 0)
        venda.nsu = nsu
        venda.data = data_venda
        
        chargeback = caixa.registrar_chargeback(venda, motivo, data_venda)
        
        print("\nChargeback registrado com sucesso!")
        print(chargeback)
        sleep(3)
        funcoes.limpar_tela()
    
    # Fechar caixa - 7
    elif menu == '7':
        print("=-" * 30)
        print("\n")
        print("LISTA DE VENDAS\n")
        print("=-" * 30)
        caixa.listar_vendas()
        print(f'TOTAL BRUTO: R${caixa.total_bruto():.2f}')
        print(f'LÍQUIDO À RECEBER: R${caixa.total_liquido():.2f}')
        print("\nLISTA DE CHARGEBACKS")
        print("=-" * 30)
        caixa.listar_chargebacks()
        print(f'TOTAL CHARGEBACKS: R${caixa.total_chargebacks():.2f}')

        from exportar_xml import exportar_para_xml
        nome_arquivo = exportar_para_xml(caixa)
        print(f"\nRelatório XML gerado com sucesso: {nome_arquivo}")
        
        input('Pressione enter para sair: ')
        funcoes.limpar_tela()
        break
    
    
    else:
        print("Comando Inválido! por favor , digite um número inteiro entre 1 e 6")
        sleep(2)
        funcoes.limpar_tela()
