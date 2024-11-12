# Sistema de Gestão de Vendas
#### Trabalho de Introdução à Programação Orientada à Objetos

## Desenvolvimentos necessários para cumprimento dos requisitos:
### 1. Classes e Relações
- Classe `Operadora`:
    - Atributos: `nome`, `taxa`
    - Métodos: `cadastrar_operadora()`, `atualizar_taxa()`, `excluir_taxa()`

- Classe `Caixa`:
    - Atributos: `Venda`
    - Métodos: `incluir_venda()`, `fechar_caixa()`, `relatorio_vendas`
        - Subclasse `Venda`:
            - Atributos: `valor_bruto`, `operadora`, `taxa`, `valor_liquido`
            - Métodos: `registrar_venda()`, `excluir_venda`, `calcular_valor_liquido()`

### CRUD
- Create:
    - `Operadora`: Método `cadastrar_operadora()`
    - `Venda`: Método `registrar_venda()`

- Read:
    - `Operadora`: Listar as operadoras cadastradas
    - `Venda`: Listar as vendas realizadas

- Update: 
    - `Operadora`: Método `atualizar_taxa()`

- Delete:
    - `Operadora`: Método `excluir_taxa()`
    - `Venda`: Método `excluir_venda()`

### Estruturas de seleção/repetição

- Utilizaremos if/elif/else para selecionar a operadora e calcular o valor líquido da venda
- Usaremos while para criar um menu principal com as opções de cadastro, vendas e fechamento de caixa

### Estruturas de Dados:

- Lista para guardar informações das taxas cadastradas
- Lista para guardar informações das vendas realizadas

### Polimorfismo:

- Ainda estamos verificando como vamos utilizar o polimorfismo no código.