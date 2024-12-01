from operadora import Operadora
from datetime import datetime

class Chargeback(Operadora):
    def __init__(self, venda_original, motivo=None, data=None):
        super().__init__('Chargeback', 0)  # Taxa zero por padrão
        self.venda_original = venda_original
        self.valor = venda_original.valor_bruto
        self.nsu = venda_original.nsu if hasattr(venda_original, 'nsu') else None
        self.motivo = motivo
        self.data = datetime.strptime(data, '%d/%m/%Y') if data else datetime.now()

    def __str__(self):
        return (f"Chargeback - Valor: R${self.valor:.2f}, "
                f"NSU: {self.nsu}, "
                f"Motivo: {self.motivo}, "
                f"Data: {self.data.strftime('%d/%m/%Y')}")
