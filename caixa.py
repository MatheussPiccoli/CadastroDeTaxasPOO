from operadora import Operadora
from venda import Venda

class Caixa:
    def __init__(self):
        self.operadoras = []
        self.vendas = []
        self.chargebacks = []
    
    def cadastrar_operadora(self, nome, taxa):
        operadora = Operadora(nome, taxa)
        self.operadoras.insert(0, operadora)
        return operadora
    
    def registrador_vendas(self, valor_bruto, operadora):
        venda = Venda(valor_bruto, operadora.nome, operadora.taxa)
        self.vendas.append(venda)
        return venda

    def atualizar_taxa(self, num_operadora, taxa):
        operadora_atualizada = self.operadoras[num_operadora - 1]
        operadora_atualizada.taxa = taxa
        return operadora_atualizada

    def excluir_operadora(self, operadora):
        self.num_operadora = int(operadora)
        deleted_operadora = self.operadoras[self.num_operadora - 1]
        del self.operadoras[self.num_operadora - 1]
        return deleted_operadora
    
    def excluir_venda(self, num_venda):
        self.num_venda = int(num_venda)
        deleted_venda = self.vendas[self.num_venda - 1]
        del self.vendas[self.num_venda - 1]
        return deleted_venda
    
    def registrar_chargeback(self, venda, motivo, data=None):
        from chargeback import Chargeback
        chargeback = Chargeback(venda, motivo, data)
        self.chargebacks.append(chargeback)
        return chargeback
    
    def listar_chargebacks(self):
        if not self.chargebacks:
            print("Não há chargebacks registrados.")
            return
        
        for i, chargeback in enumerate(self.chargebacks, 1):
            print(f"Chargeback {i}: {chargeback}")
    
    def total_bruto(self):
        return sum(venda.valor_bruto for venda in self.vendas)
    
    def total_liquido(self):
        return sum(venda.valor_liquido for venda in self.vendas)
    
    def total_chargebacks(self):
        return sum(chargeback.valor for chargeback in self.chargebacks)
    
    def listar_vendas(self):
        for i in range(0, len(self.vendas)):
            venda = self.vendas[i]
            print(f"Venda {i + 1}: ")
            print(f"Valor bruto: R$ {venda.valor_bruto:.2f}")
            print(f"Taxa: {venda.taxa} %")
            print(f"Valor Líquido: R$ {venda.valor_liquido:.2f}")
            print("=-" * 30)
    
    def listar_operadoras(self, fim=0):
        print("Operadoras cadastradas:")
        for i in range(len(self.operadoras) - fim):
            operadoras = self.operadoras[i]
            print(f"{i + 1} - {operadoras.nome}, {operadoras.taxa} % de taxa")
   
