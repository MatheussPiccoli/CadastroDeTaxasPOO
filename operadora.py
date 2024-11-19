class Operadora:
    def __init__(self, nome, taxa):
        self.nome = nome
        self.taxa = taxa
        
    def __repr__(self):
        return f'Operadora(nome={self.nome}, taxa={self.taxa}%)'
