from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import datetime

def exportar_para_xml(caixa, nome_arquivo="relatorio_vendas.xml"):

    # Criar elemento raiz
    raiz = Element('relatorio_vendas')
    raiz.set('data_geracao', datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    
    # Adicionar seção de resumo
    resumo = SubElement(raiz, 'resumo')
    SubElement(resumo, 'total_bruto').text = f"{caixa.total_bruto():.2f}"
    SubElement(resumo, 'total_liquido').text = f"{caixa.total_liquido():.2f}"
    SubElement(resumo, 'total_chargebacks').text = f"{caixa.total_chargebacks():.2f}"
    
    # Adicionar seção de operadoras
    operadoras = SubElement(raiz, 'operadoras')
    for i, operadora in enumerate(caixa.operadoras, 1):
        op_elem = SubElement(operadoras, 'operadora')
        op_elem.set('id', str(i))
        SubElement(op_elem, 'nome').text = operadora.nome
        SubElement(op_elem, 'taxa').text = f"{operadora.taxa:.2f}"
    
    # Adicionar seção de vendas
    vendas = SubElement(raiz, 'vendas')
    for i, venda in enumerate(caixa.vendas, 1):
        venda_elem = SubElement(vendas, 'venda')
        venda_elem.set('id', str(i))
        SubElement(venda_elem, 'operadora').text = venda.nome
        SubElement(venda_elem, 'valor_bruto').text = f"{venda.valor_bruto:.2f}"
        SubElement(venda_elem, 'taxa').text = f"{venda.taxa:.2f}"
        SubElement(venda_elem, 'valor_liquido').text = f"{venda.valor_liquido:.2f}"
    
    # Adicionar seção de chargebacks
    chargebacks = SubElement(raiz, 'chargebacks')
    for i, chargeback in enumerate(caixa.chargebacks, 1):
        cb_elem = SubElement(chargebacks, 'chargeback')
        cb_elem.set('id', str(i))
        SubElement(cb_elem, 'valor').text = f"{chargeback.valor:.2f}"
        if hasattr(chargeback, 'nsu') and chargeback.nsu:
            SubElement(cb_elem, 'nsu').text = chargeback.nsu
        SubElement(cb_elem, 'motivo').text = chargeback.motivo
        SubElement(cb_elem, 'data').text = chargeback.data.strftime('%d/%m/%Y')
    
    # Criar a string XML com formatação adequada
    xmlstr = minidom.parseString(tostring(raiz, 'utf-8')).toprettyxml(indent="    ")
    
    # Escrever no arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(xmlstr)
    
    return nome_arquivo
