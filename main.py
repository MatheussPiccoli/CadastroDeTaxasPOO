import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from tkinter import simpledialog
from caixa import Caixa
from venda import Venda
from exportar_xml import exportar_para_xml

class SistemaVendasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas")
        self.root.geometry("800x600")
        
        self.caixa = Caixa()
        # Cadastrar Pix/Dinheiro por padrão
        self.caixa.cadastrar_operadora("Pix/Dinheiro", 0)
        
        # Criar notebook (abas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Criar abas
        self.criar_aba_operadoras()
        self.criar_aba_vendas()
        self.criar_aba_chargebacks()
        self.criar_aba_relatorios()
        
    def criar_aba_operadoras(self):
        frame_operadoras = ttk.Frame(self.notebook)
        self.notebook.add(frame_operadoras, text='Operadoras')
        
        # Frame para cadastro
        frame_cadastro = ttk.LabelFrame(frame_operadoras, text="Cadastrar Operadora")
        frame_cadastro.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(frame_cadastro, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = ttk.Entry(frame_cadastro)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_cadastro, text="Taxa (%):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_taxa = ttk.Entry(frame_cadastro)
        self.entry_taxa.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(frame_cadastro, text="Cadastrar", command=self.cadastrar_operadora).grid(row=0, column=4, padx=5, pady=5)
        
        # Lista de operadoras
        frame_lista = ttk.LabelFrame(frame_operadoras, text="Operadoras Cadastradas")
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.tree_operadoras = ttk.Treeview(frame_lista, columns=('Nome', 'Taxa'), show='headings')
        self.tree_operadoras.heading('Nome', text='Nome')
        self.tree_operadoras.heading('Taxa', text='Taxa (%)')
        self.tree_operadoras.pack(fill='both', expand=True, padx=5, pady=5)
        
        frame_acoes = ttk.Frame(frame_operadoras)
        frame_acoes.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(frame_acoes, text="Atualizar Taxa", command=self.atualizar_taxa).pack(side='left', padx=5)
        ttk.Button(frame_acoes, text="Excluir Operadora", command=self.excluir_operadora).pack(side='left', padx=5)
        
        self.atualizar_lista_operadoras()
        
    def criar_aba_vendas(self):
        frame_vendas = ttk.Frame(self.notebook)
        self.notebook.add(frame_vendas, text='Vendas')
        
        # Frame para registro de vendas
        frame_registro = ttk.LabelFrame(frame_vendas, text="Registrar Venda")
        frame_registro.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(frame_registro, text="Operadora:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_operadoras = ttk.Combobox(frame_registro, state='readonly')
        self.combo_operadoras.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_registro, text="Valor (R$):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_valor = ttk.Entry(frame_registro)
        self.entry_valor.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(frame_registro, text="Registrar Venda", command=self.registrar_venda).grid(row=0, column=4, padx=5, pady=5)
        
        # Lista de vendas
        frame_lista = ttk.LabelFrame(frame_vendas, text="Vendas Registradas")
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.tree_vendas = ttk.Treeview(frame_lista, columns=('Operadora', 'Valor Bruto', 'Taxa', 'Valor Líquido'), show='headings')
        self.tree_vendas.heading('Operadora', text='Operadora')
        self.tree_vendas.heading('Valor Bruto', text='Valor Bruto')
        self.tree_vendas.heading('Taxa', text='Taxa (%)')
        self.tree_vendas.heading('Valor Líquido', text='Valor Líquido')
        self.tree_vendas.pack(fill='both', expand=True, padx=5, pady=5)
        
        ttk.Button(frame_vendas, text="Excluir Venda", command=self.excluir_venda).pack(pady=5)
        
    def criar_aba_chargebacks(self):
        frame_chargebacks = ttk.Frame(self.notebook)
        self.notebook.add(frame_chargebacks, text='Chargebacks')
        
        # Frame para registro de chargebacks
        frame_registro = ttk.LabelFrame(frame_chargebacks, text="Registrar Chargeback")
        frame_registro.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(frame_registro, text="Valor:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_valor_cb = ttk.Entry(frame_registro)
        self.entry_valor_cb.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_registro, text="NSU:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_nsu = ttk.Entry(frame_registro)
        self.entry_nsu.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(frame_registro, text="Motivo:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_motivo = ttk.Entry(frame_registro)
        self.entry_motivo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_registro, text="Data:").grid(row=1, column=2, padx=5, pady=5)
        self.entry_data = ttk.Entry(frame_registro)
        self.entry_data.grid(row=1, column=3, padx=5, pady=5)
        self.entry_data.insert(0, datetime.datetime.now().strftime('%d/%m/%Y'))
        
        ttk.Button(frame_registro, text="Registrar Chargeback", 
                  command=self.registrar_chargeback).grid(row=2, column=0, columnspan=4, pady=10)
        
        # Lista de chargebacks
        frame_lista = ttk.LabelFrame(frame_chargebacks, text="Chargebacks Registrados")
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.tree_chargebacks = ttk.Treeview(frame_lista, 
                                            columns=('Valor', 'NSU', 'Motivo', 'Data'),
                                            show='headings')
        self.tree_chargebacks.heading('Valor', text='Valor')
        self.tree_chargebacks.heading('NSU', text='NSU')
        self.tree_chargebacks.heading('Motivo', text='Motivo')
        self.tree_chargebacks.heading('Data', text='Data')
        self.tree_chargebacks.pack(fill='both', expand=True, padx=5, pady=5)
        
    def criar_aba_relatorios(self):
        frame_relatorios = ttk.Frame(self.notebook)
        self.notebook.add(frame_relatorios, text='Relatórios')
        
        # Frame para totais
        frame_totais = ttk.LabelFrame(frame_relatorios, text="Totais")
        frame_totais.pack(fill='x', padx=5, pady=5)
        
        self.label_total_bruto = ttk.Label(frame_totais, text="Total Bruto: R$ 0.00")
        self.label_total_bruto.pack(pady=5)
        
        self.label_total_liquido = ttk.Label(frame_totais, text="Total Líquido: R$ 0.00")
        self.label_total_liquido.pack(pady=5)
        
        self.label_total_chargebacks = ttk.Label(frame_totais, text="Total Chargebacks: R$ 0.00")
        self.label_total_chargebacks.pack(pady=5)
        
        ttk.Button(frame_relatorios, text="Exportar XML", 
                  command=self.exportar_xml).pack(pady=10)
        
    def cadastrar_operadora(self):
        try:
            nome = self.entry_nome.get().strip().upper()
            taxa = float(self.entry_taxa.get().replace(',', '.'))
            
            if not nome:
                messagebox.showerror("Erro", "Nome da operadora não pode estar vazio")
                return
                
            if taxa < 0 or taxa > 100:
                messagebox.showerror("Erro", "Taxa deve estar entre 0 e 100")
                return
                
            self.caixa.cadastrar_operadora(nome, taxa)
            self.atualizar_lista_operadoras()
            self.atualizar_combo_operadoras()
            
            self.entry_nome.delete(0, tk.END)
            self.entry_taxa.delete(0, tk.END)
            
            messagebox.showinfo("Sucesso", f"Operadora {nome} cadastrada com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Taxa inválida")
            
    def atualizar_lista_operadoras(self):
        for item in self.tree_operadoras.get_children():
            self.tree_operadoras.delete(item)
            
        for operadora in self.caixa.operadoras:
            self.tree_operadoras.insert('', 'end', values=(operadora.nome, f"{operadora.taxa:.2f}"))
            
    def atualizar_combo_operadoras(self):
        self.combo_operadoras['values'] = [op.nome for op in self.caixa.operadoras]
        if self.combo_operadoras['values']:
            self.combo_operadoras.current(0)
            
    def atualizar_taxa(self):
        selection = self.tree_operadoras.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma operadora para atualizar")
            return
            
        operadora_index = self.tree_operadoras.index(selection[0])
        if operadora_index == 0:  # Pix/Dinheiro
            messagebox.showwarning("Aviso", "Não é possível alterar a taxa de Pix/Dinheiro")
            return
            
        nova_taxa = simpledialog.askfloat("Nova Taxa", 
                                         "Digite a nova taxa (%):",
                                         minvalue=0,
                                         maxvalue=100)
        
        if nova_taxa is not None:
            self.caixa.atualizar_taxa(operadora_index + 1, nova_taxa)
            self.atualizar_lista_operadoras()
            messagebox.showinfo("Sucesso", "Taxa atualizada com sucesso!")
            
    def excluir_operadora(self):
        selection = self.tree_operadoras.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma operadora para excluir")
            return
            
        operadora_index = self.tree_operadoras.index(selection[0])
        if operadora_index == 0:  # Pix/Dinheiro
            messagebox.showwarning("Aviso", "Não é possível excluir Pix/Dinheiro")
            return
            
        if messagebox.askyesno("Confirmar", "Deseja realmente excluir esta operadora?"):
            self.caixa.excluir_operadora(operadora_index + 1)
            self.atualizar_lista_operadoras()
            self.atualizar_combo_operadoras()
            messagebox.showinfo("Sucesso", "Operadora excluída com sucesso!")
            
    def registrar_venda(self):
        try:
            operadora_nome = self.combo_operadoras.get()
            valor = float(self.entry_valor.get().replace(',', '.'))
            
            if valor <= 0:
                messagebox.showerror("Erro", "Valor deve ser maior que zero")
                return
                
            operadora = next(op for op in self.caixa.operadoras if op.nome == operadora_nome)
            venda = self.caixa.registrador_vendas(valor, operadora)
            
            self.entry_valor.delete(0, tk.END)
            self.atualizar_lista_vendas()
            self.atualizar_totais()
            
            messagebox.showinfo("Sucesso", 
                              f"Venda registrada!\nValor Bruto: R$ {valor:.2f}\n"
                              f"Taxa: {operadora.taxa}%\n"
                              f"Valor Líquido: R$ {venda.valor_liquido:.2f}")
            
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido")
            
    def atualizar_lista_vendas(self):
        for item in self.tree_vendas.get_children():
            self.tree_vendas.delete(item)
            
        for venda in self.caixa.vendas:
            self.tree_vendas.insert('', 'end', 
                                  values=(venda.nome,
                                         f"R$ {venda.valor_bruto:.2f}",
                                         f"{venda.taxa:.2f}%",
                                         f"R$ {venda.valor_liquido:.2f}"))
            
    def excluir_venda(self):
        selection = self.tree_vendas.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma venda para excluir")
            return
            
        if messagebox.askyesno("Confirmar", "Deseja realmente excluir esta venda?"):
            venda_index = self.tree_vendas.index(selection[0])
            self.caixa.excluir_venda(venda_index + 1)
            self.atualizar_lista_vendas()
            self.atualizar_totais()
            messagebox.showinfo("Sucesso", "Venda excluída com sucesso!")
            
    def registrar_chargeback(self):
        try:
            valor = float(self.entry_valor_cb.get().replace(',', '.'))
            nsu = self.entry_nsu.get().strip()
            motivo = self.entry_motivo.get().strip()
            data = self.entry_data.get().strip()
            
            if valor <= 0:
                messagebox.showerror("Erro", "Valor deve ser maior que zero")
                return
                
            if not all([nsu, motivo, data]):
                messagebox.showerror("Erro", "Todos os campos são obrigatórios")
                return
            
            # Criar venda temporária para o chargeback
            venda_temp = Venda(valor, "Cancelamento", 0)
            venda_temp.nsu = nsu
            
            chargeback = self.caixa.registrar_chargeback(venda_temp, motivo, data)
            
            self.entry_valor_cb.delete(0, tk.END)
            self.entry_nsu.delete(0, tk.END)
            self.entry_motivo.delete(0, tk.END)
            self.entry_data.delete(0, tk.END)
            self.entry_data.insert(0, datetime.datetime.now().strftime('%d/%m/%Y'))
            
            self.atualizar_lista_chargebacks()
            self.atualizar_totais()
            
            messagebox.showinfo("Sucesso", "Chargeback registrado com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Dados inválidos")
            
    def atualizar_lista_chargebacks(self):
        for item in self.tree_chargebacks.get_children():
            self.tree_chargebacks.delete(item)
            
        for cb in self.caixa.chargebacks:
            self.tree_chargebacks.insert('', 'end',
                                       values=(f"R$ {cb.valor:.2f}",
                                              cb.nsu,
                                              cb.motivo,
                                              cb.data.strftime('%d/%m/%Y')))
            
    def atualizar_totais(self):
        self.label_total_bruto.config(
            text=f"Total Bruto: R$ {self.caixa.total_bruto():.2f}")
        self.label_total_liquido.config(
            text=f"Total Líquido: R$ {self.caixa.total_liquido():.2f}")
        self.label_total_chargebacks.config(
            text=f"Total Chargebacks: R$ {self.caixa.total_chargebacks():.2f}")
            
    def exportar_xml(self):
        try:
            nome_arquivo = exportar_para_xml(self.caixa)
            messagebox.showinfo("Sucesso", f"Relatório XML gerado com sucesso: {nome_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar XML: {str(e)}")

def main():
    root = tk.Tk()
    from tkinter import simpledialog  # Importação necessária para o diálogo de atualização de taxa
    app = SistemaVendasGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
