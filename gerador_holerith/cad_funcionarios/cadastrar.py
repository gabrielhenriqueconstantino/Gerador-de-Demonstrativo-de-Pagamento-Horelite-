import customtkinter
import os
import sqlite3
import tkinter as tk
from tkinter import ttk

# Variável para controle de visibilidade
tabela_visivel = True

# Função para fechar janela
def fechar():
    janela.destroy()
    os.system("python menu.py")

# Função para alternar entre exibir tabela e frame de adicionar funcionários
def alternar_exibicao():
    global tabela_visivel

    if tabela_visivel:
        tree.pack_forget()  # Oculta a Treeview
        frame_adicionar.pack(padx=20, pady=20, fill="both", expand=True)  # Mostra o frame de adicionar funcionários
        tabela_visivel = False
    else:
        frame_adicionar.pack_forget()  # Oculta o frame de adicionar funcionários
        tree.pack(padx=20, pady=20, fill="both", expand=True)  # Mostra a Treeview
        tabela_visivel = True

# Criar a janela principal
janela = customtkinter.CTk()
janela.title("Cadastro Funcional")
janela.geometry("1000x550")

# Texto no topo
texto = customtkinter.CTkLabel(janela, font=("Helvetica", 18), text="Cadastro funcional")
texto.pack(padx=10, pady=10)

# Frame para os botões de voltar, adicionar, editar e excluir
frame_botoes = customtkinter.CTkFrame(janela, border_width=1, border_color="white", fg_color="#1C1C1C")
frame_botoes.pack(padx=20, pady=10, fill="both")

# Botão de voltar
botao_voltar = customtkinter.CTkButton(frame_botoes, text="⭠", font=("Arial", 40), command=fechar)
botao_voltar.pack(side="left", padx=10, pady=10)

# Botão de adicionar, editar e excluir
botao_adicionar = customtkinter.CTkButton(frame_botoes, text="➕", font=("Arial", 30), width=10, corner_radius=8, command=alternar_exibicao)
botao_adicionar.pack(side="right", padx=10, pady=10)

edit = customtkinter.CTkButton(frame_botoes, text="✏", font=("Arial", 29.5), width=10, corner_radius=8)
edit.pack(side="right", padx=10, pady=10)

delete = customtkinter.CTkButton(frame_botoes, text="⌫", font=("Arial", 30), width=10, corner_radius=8, command=lambda: excluir_funcionario())
delete.pack(side="right", padx=10, pady=10)

# Frame para a barra de pesquisa
frame_pesquisa = customtkinter.CTkFrame(janela, border_width=1, border_color="white", corner_radius=10, fg_color="#1C1C1C")
frame_pesquisa.pack(padx=20, pady=10, fill='x')

search_entry = customtkinter.CTkEntry(frame_pesquisa, corner_radius=14, border_width=1, placeholder_text="Pesquisar por nome, código, cargo...", width=500, height=35, fg_color="#2E2E2E", text_color="white", border_color="white")
search_entry.pack(side="left", padx=10, pady=10)

search_button = customtkinter.CTkButton(frame_pesquisa, text="🔍", font=("Arial", 15), width=30, fg_color="#2E86C1", text_color="white", hover_color="#1B4F72", command=lambda: pesquisar(search_entry.get()))
search_button.pack(side="right", padx=10, pady=10)

# Adicionar evento para atualizar a pesquisa conforme o usuário digita
search_entry.bind("<KeyRelease>", lambda event: pesquisar(search_entry.get()))

# Adicionar evento para realizar a pesquisa ao pressionar a tecla Enter
search_entry.bind("<Return>", lambda event: pesquisar(search_entry.get()))

# Verificar e criar/popular o banco de dados se necessário
def verificar_bd():
    caminho_bd = './cad_funcionarios/funcionarios.db'
    if not os.path.exists(caminho_bd):
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()

        # Ler o conteúdo do arquivo SQL de criação e inserção de dados
        with open('./cad_funcionarios/funcionarios.sql', 'r') as f:
            sql_script = f.read()

        # Executar o script SQL
        cursor.executescript(sql_script)

        # Commit e fechar conexão com o banco de dados
        conn.commit()
        conn.close()

# Função para carregar dados do banco de dados e exibir na Treeview
def carregar_dados(filtro=None):
    conn = sqlite3.connect('./cad_funcionarios/funcionarios.db')
    cursor = conn.cursor()

    # Limpar dados existentes na Treeview
    for row in tree.get_children():
        tree.delete(row)

    if filtro:
        # Executar consulta para recuperar os dados filtrados
        query = "SELECT codigo, nome, cargo, salario, data_admissao FROM funcionarios WHERE "
        query += "nome LIKE ? OR codigo LIKE ? OR cargo LIKE ?"
        cursor.execute(query, ('%' + filtro + '%', '%' + filtro + '%', '%' + filtro + '%'))
    else:
        # Executar consulta para recuperar todos os dados
        cursor.execute("SELECT codigo, nome, cargo, salario, data_admissao FROM funcionarios")

    rows = cursor.fetchall()

    # Inserir dados na Treeview
    for row in rows:
        tree.insert("", "end", values=row)

    # Fechar conexão com o banco de dados
    conn.close()

# Função para pesquisar funcionários
def pesquisar(filtro):
    carregar_dados(filtro)

# Função para excluir um funcionário do banco de dados
def excluir_funcionario():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        codigo = item['values'][0]

        conn = sqlite3.connect('./cad_funcionarios/funcionarios.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE codigo=?", (codigo,))
        conn.commit()
        conn.close()

        # Remover a linha da Treeview
        tree.delete(selected_item)

        # Atualizar o arquivo .sql (se necessário)
        # Não é necessário atualizar o arquivo .sql aqui, pois ele é gerado na criação do banco de dados

    else:
        print("Nenhum funcionário selecionado para exclusão.")


# Frame para exibir os funcionários
tree = ttk.Treeview(janela, columns=("codigo", "nome", "cargo", "salario", "data_admissao"), show="headings")
tree.heading("codigo", text="Código")
tree.heading("nome", text="Nome")
tree.heading("cargo", text="Cargo")
tree.heading("salario", text="Salário")
tree.heading("data_admissao", text="Data de Admissão")

tree.column("codigo", anchor="center", width=10)
tree.column("nome", anchor="center", width=100)
tree.column("cargo", anchor="center", width=150)
tree.column("salario", anchor="center", width=80)
tree.column("data_admissao", anchor="center", width=100)

tree.pack(padx=20, pady=20, fill="both", expand=True)

# Frame para adicionar funcionários
frame_adicionar = customtkinter.CTkFrame(janela, border_width=1, border_color="white", fg_color="#1C1C1C")

# Simular um formulário para adicionar funcionários
entry_nome = customtkinter.CTkEntry(frame_adicionar, placeholder_text="Nome", font=("Helvetica", 14))
entry_nome.pack(padx=10, pady=10)

entry_cargo = customtkinter.CTkEntry(frame_adicionar, placeholder_text="Cargo", font=("Helvetica", 14))
entry_cargo.pack(padx=10, pady=10)

entry_salario = customtkinter.CTkEntry(frame_adicionar, placeholder_text="Salario", font=("Helvetica", 14))
entry_salario.pack(padx=10, pady=10)

entry_data_admissao = customtkinter.CTkEntry(frame_adicionar, placeholder_text="Data de Admissão", font=("Helvetica", 14))
entry_data_admissao.pack(padx=10, pady=10)

button_salvar = customtkinter.CTkButton(frame_adicionar, text="Salvar", corner_radius=8, command=lambda: salvar_funcionario(entry_nome.get(), entry_cargo.get(), entry_salario.get(), entry_data_admissao.get()))
button_salvar.pack(padx=10, pady=10)

# Função para salvar novo funcionário
def salvar_funcionario(nome, cargo, salario, data_admissao):
    conn = sqlite3.connect('./cad_funcionarios/funcionarios.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario, data_admissao) VALUES (?, ?, ?, ?)", (nome, cargo, salario, data_admissao))
    conn.commit()
    conn.close()

    # Limpar campos após salvar
    entry_nome.delete(0, 'end')
    entry_cargo.delete(0, 'end')
    entry_salario.delete(0, 'end')
    entry_data_admissao.delete(0, 'end')

# Verificar e criar/popular o banco de dados se necessário
verificar_bd()

# Carregar os dados do banco de dados e inserir na Treeview
carregar_dados()

# Iniciar loop da janela
janela.mainloop()
