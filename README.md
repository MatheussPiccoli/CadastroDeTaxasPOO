# Sistema de Gestão de Vendas
![Status do Projeto](https://img.shields.io/badge/Status-Concluído-green)
![Python Version](https://img.shields.io/badge/Python-3.0+-blue)

## 📋 Descrição do Projeto
Sistema de gestão de vendas desenvolvido como trabalho da disciplina de Introdução à Programação Orientada a Objetos. O sistema permite o gerenciamento de vendas, cadastro de taxas de operadoras (maquininhas) e fechamento de caixa.

## 👥 Equipe
- Matheus Silvano
- Matheus Piccoli
- Matias Drews
- Pedro Marques

## O projeto
```
projeto/
├── main.py           # Interface gráfica completa usando Tkinter
├── caixa.py          # Classe central que gerencia todas as operações do sistema
├── venda.py          # Define a classe Venda e seus cálculos (valor bruto, líquido, taxas)
├── operadora.py      # Define a classe base Operadora (nome e taxa)
├── chargeback.py     # Gerencia os estornos/cancelamentos de vendas
├── funcoes.py        # Funções utilitárias (validações de entrada, limpeza)
└── exportar_xml.py   # Gera o relatório final em formato XML 
```

## 🛠️ Funcionalidades

### 1. Gestão de Operadoras 💳
* Cadastro de novas operadoras de pagamento (cartão, pix, etc.)
* Configuração de taxas personalizadas por operadora
* Atualização e exclusão de operadoras existentes
* Operadora Pix/Dinheiro padrão com taxa 0%
* Visualização em tabela de todas as operadoras cadastradas

### 2. Gestão de Vendas 📊
* Registro de vendas com interface intuitiva
* Seleção simplificada de operadora via menu
* Cálculo automático do valor líquido baseado nas taxas
* Histórico completo de vendas em formato tabular
* Exclusão de vendas com confirmação de segurança
* Visualização de valores brutos e líquidos por venda

### 3. Gestão de Chargebacks (Estornos) ↩️
* Registro detalhado de estornos/cancelamentos
* Histórico completo de chargebacks realizados
* Impacto automático nos totais do caixa

### 4. Relatórios e Exportação 📑
* Visualização em tempo real dos totais:
  - Valor bruto total das vendas
  - Valor líquido após taxas
  - Total de chargebacks
* Exportação completa para XML contendo:
  - Resumo financeiro
  - Lista de operadoras e taxas
  - Detalhamento de vendas
  - Registro de chargebacks

### 5. Interface Gráfica 🖥️
* Design moderno e intuitivo
* Sistema organizado em abas para fácil navegação:
  - Aba de Operadoras
  - Aba de Vendas
  - Aba de Chargebacks
  - Aba de Relatórios
* Validações em tempo real dos dados inseridos
* Mensagens de feedback para todas as operações
* Confirmações de segurança para exclusões
  
### 6. Controles de Segurança 🔒
* Validação de valores numéricos
* Proteção contra exclusão da operadora Pix/Dinheiro
* Confirmação para ações críticas
* Validação de campos obrigatórios
* Verificação de dados em tempo real
* Mensagens de erro claras e informativas

### 7. Recursos Adicionais ⚡
* Cálculos automáticos de valores e taxas
* Atualização em tempo real dos totalizadores
* Persistência de dados durante a sessão
* Possibilidade de desfazer operações
* Suporte a múltiplas operadoras
* Interface responsiva e adaptável

### 8. Armazenamento e Dados 💾
* Gestão de listas de operadoras, vendas e chargebacks
* Cálculos automáticos de totais
* Exportação de dados em formato XML
* Histórico completo de operações
* Relatórios detalhados de movimentação

## 🚀 Instalação e Uso

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-vendas

# Entre no diretório
cd sistema-vendas

# Execute o programa
python main.py
```

## 🔧 Requisitos

* Python 3.x
* Tkinter (geralmente já vem com Python)
* Sistema operacional: Windows, Linux ou macOS

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🔧 Requisitos do Sistema
- Python 3.0 ou superior

## 🤝 Contribuições
Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Requisitos Atendidos

### 1. CRUD (Create, Read, Update, Delete)
O sistema implementa operações CRUD completas para operadoras e vendas. Exemplo do CRUD de operadoras na classe `Caixa`:

```python
class Caixa:
    def __init__(self):
        self.operadoras = []    # Lista de operadoras
        self.vendas = []        # Lista de vendas
        self.chargebacks = []   # Lista de chargebacks
    
    # Create
    def cadastrar_operadora(self, nome, taxa):
        operadora = Operadora(nome, taxa)
        self.operadoras.append(operadora)
        return operadora
    
    # Read (através do listar_operadoras)
    def listar_operadoras(self):
        for i in range(0, len(self.operadoras)):
            operadoras = self.operadoras[i]
            print(f"{i + 1} - {operadoras.nome}, {operadoras.taxa} % de taxa")
    
    # Update
    def atualizar_taxa(self, num_operadora, taxa):
        operadora_atualizada = self.operadoras[num_operadora - 1]
        operadora_atualizada.taxa = taxa
        return operadora_atualizada
    
    # Delete
    def excluir_operadora(self, operadora):
        self.num_operadora = int(operadora)
        deleted_operadora = self.operadoras[self.num_operadora - 1]
        del self.operadoras[self.num_operadora - 1]
        return deleted_operadora
```

### 2. Herança e Polimorfismo
O sistema utiliza herança com as classes `Venda` e `Chargeback` herdando da classe `Operadora`:

```python
# operadora.py
class Operadora:
    def __init__(self, nome, taxa):
        self.nome = nome
        self.taxa = taxa

# venda.py
class Venda(Operadora):
    def __init__(self, valor_bruto, operadora_nome, operadora_taxa):
        super().__init__(operadora_nome, operadora_taxa)
        self.valor_bruto = valor_bruto
        self.valor_liquido = self.valor_bruto - (self.valor_bruto) * ((self.taxa) / 100)

# chargeback.py
class Chargeback(Operadora):
    def __init__(self, venda_original, motivo=None, data=None):
        super().__init__('Chargeback', 0)
        self.venda_original = venda_original
        self.valor = venda_original.valor_bruto
```

### 3. Composição/Agregação
A classe `Caixa` mantém uma relação de composição com `Operadora`, `Venda` e `Chargeback`, gerenciando o ciclo de vida desses objetos:

```python
class Caixa:
    def __init__(self):
        self.operadoras = []    # Composição com Operadora
        self.vendas = []        # Composição com Venda
        self.chargebacks = []   # Composição com Chargeback
```

### 4. Estruturas de Seleção/Repetição
O sistema utiliza diversas estruturas de controle. Exemplo de uso no registro de chargebacks:

```python
def registrar_chargeback(self, venda, motivo, data=None):
    # Seleção
    if not motivo:
        return None
        
    # Repetição ao listar chargebacks
    def listar_chargebacks(self):
        if not self.chargebacks:
            print("Não há chargebacks registrados.")
            return
        
        for i, chargeback in enumerate(self.chargebacks, 1):
            print(f"Chargeback {i}: {chargeback}")
```

### 5. Estruturas de Dados
O sistema utiliza extensivamente listas para gerenciar as coleções de objetos:

```python
class Caixa:
    def __init__(self):
        self.operadoras = []  # Lista de operadoras
        self.vendas = []      # Lista de vendas
        self.chargebacks = [] # Lista de chargebacks
    
    def total_bruto(self):
        return sum(venda.valor_bruto for venda in self.vendas)  # Uso de lista
```

## Problema Resolvido
O sistema resolve um problema real do dia a dia de comerciantes que precisam:
- Gerenciar diferentes formas de pagamento e suas taxas
- Registrar e controlar vendas
- Gerenciar estornos (chargebacks)
- Calcular valores líquidos considerando taxas
- Gerar relatórios de movimentação

A implementação com interface gráfica torna o sistema ainda mais prático e fácil de usar.

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
