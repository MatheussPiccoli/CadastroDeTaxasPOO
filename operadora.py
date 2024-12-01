from operadora import Operadora

class Venda(Operadora):
    def __init__(self, valor_bruto, operadora_nome, operadora_taxa):
        super().__init__(operadora_nome, operadora_taxa)
        self.valor_bruto = valor_bruto
        self.valor_liquido = self.valor_bruto - (self.valor_bruto) * ((self.taxa) / 100)
        
    def __str__(self):
        return (f"valor_bruto=R${self.valor_bruto:.2f}, taxa={self.taxa}%, valor_liquido=R${self.valor_liquido:.2f}")
    
