import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph

def gerar_contrato():
    nome_comprador = nome_entry.get()
    cpf_comprador = cpf_entry.get()
    endereco_imovel = endereco_entry.get()
    valor_operacao = valor_entry.get()
    tipo_operacao = operacao_var.get()
    nome_vendedor = vendedor_entry.get()
    cpf_vendedor = cpf_vendedor_entry.get()
    endereco_vendedor = endereco_vendedor_entry.get()
    testemunha1_nome = testemunha1_nome_entry.get()
    testemunha1_cpf = testemunha1_cpf_entry.get()
    testemunha2_nome = testemunha2_nome_entry.get()
    testemunha2_cpf = testemunha2_cpf_entry.get()

    if not nome_comprador or not cpf_comprador or not endereco_imovel or not valor_operacao or not nome_vendedor or not cpf_vendedor or not endereco_vendedor or not testemunha1_nome or not testemunha1_cpf or not testemunha2_nome or not testemunha2_cpf:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    try:
        pdf_gerado = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        arquivo_pdf = os.path.join(pdf_gerado, 'contrato_gerado.pdf')

        c = canvas.Canvas(arquivo_pdf, pagesize=letter)
        largura, altura = letter
        
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, altura - 100, "CONTRATO DE COMPRA E VENDA")
        c.setFont("Helvetica", 10)
        
        c.setStrokeColor(colors.black)
        c.line(100, altura - 105, largura - 100, altura - 105)
        
        y_position = altura - 130
        espaco_entre_linhas = 20
        
        def draw_text(texto):
            nonlocal y_position
            c.drawString(100, y_position, texto)
            y_position -= espaco_entre_linhas

        draw_text(f"Comprador: {nome_comprador}")
        draw_text(f"CPF do Comprador: {cpf_comprador}")
        draw_text(f"Endereço do Imóvel: {endereco_imovel}")
        draw_text(f"Valor da Operação: {valor_operacao}")
        draw_text(f"Tipo de Operação: {tipo_operacao}")
        draw_text(f"Vendedor: {nome_vendedor}")
        draw_text(f"CPF do Vendedor: {cpf_vendedor}")
        draw_text(f"Endereço do Vendedor: {endereco_vendedor}")
        draw_text(f"Testemunha 1: {testemunha1_nome} (CPF: {testemunha1_cpf})")
        draw_text(f"Testemunha 2: {testemunha2_nome} (CPF: {testemunha2_cpf})")
        
        c.drawString(100, y_position, "Assinatura do Comprador: ____________________________")
        y_position -= espaco_entre_linhas
        c.drawString(100, y_position, "Assinatura do Vendedor: ____________________________")
        y_position -= espaco_entre_linhas
        c.drawString(100, y_position, "Assinatura das Testemunhas: ________________________")

        c.setFont("Helvetica", 8)
        c.drawString(100, 60, "Este contrato foi gerado automaticamente pelo sistema.")
        
        c.save()

        messagebox.showinfo("Sucesso", f"Contrato gerado com sucesso!")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar contrato: {str(e)}")

root = tk.Tk()
root.title("Gerador de Contratos")
root.geometry("700x950")

root.config(bg="#f0f0f0")

font = ("Arial", 10)

title_label = tk.Label(root, text="Gerador de Contratos", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

tk.Label(root, text="Nome do Comprador:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
nome_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
nome_entry.pack(pady=5)

tk.Label(root, text="CPF do Comprador:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
cpf_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
cpf_entry.pack(pady=5)

tk.Label(root, text="Endereço do Imóvel:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
endereco_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
endereco_entry.pack(pady=5)

tk.Label(root, text="Valor da Operação:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
valor_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
valor_entry.pack(pady=5)

tk.Label(root, text="Tipo de Operação:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
operacao_var = tk.StringVar(value="Compra à Vista")
tk.OptionMenu(root, operacao_var, "Compra à Vista", "Financiamento Bancário").pack(pady=5)

tk.Label(root, text="Nome do Vendedor:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
vendedor_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
vendedor_entry.pack(pady=5)

tk.Label(root, text="CPF do Vendedor:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
cpf_vendedor_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
cpf_vendedor_entry.pack(pady=5)

tk.Label(root, text="Endereço do Vendedor:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
endereco_vendedor_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
endereco_vendedor_entry.pack(pady=5)

tk.Label(root, text="Nome da Testemunha 1:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
testemunha1_nome_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
testemunha1_nome_entry.pack(pady=5)

tk.Label(root, text="CPF da Testemunha 1:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
testemunha1_cpf_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
testemunha1_cpf_entry.pack(pady=5)

tk.Label(root, text="Nome da Testemunha 2:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
testemunha2_nome_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
testemunha2_nome_entry.pack(pady=5)

tk.Label(root, text="CPF da Testemunha 2:", font=font, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20, pady=5)
testemunha2_cpf_entry = tk.Entry(root, font=font, width=40, bd=2, relief="solid")
testemunha2_cpf_entry.pack(pady=5)

gerar_btn = tk.Button(root, text="Gerar Contrato", command=gerar_contrato, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=5)
gerar_btn.pack(pady=20)

root.mainloop()
