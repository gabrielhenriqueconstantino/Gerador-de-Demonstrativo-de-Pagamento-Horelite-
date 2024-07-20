import sqlite3
import subprocess
import customtkinter

def verificar_login():
    # Conectar ao banco de dados
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Obter o usuário e senha digitados
    usuario_digitado = email.get()
    senha_digitada = senha.get()

    # Verificar se o usuário e senha correspondem aos dados no banco de dados
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (usuario_digitado, senha_digitada))
    usuario = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    conn.close()

    if usuario:
        print("Login bem-sucedido!")
        janela.destroy()  # Fechar a janela de login
        try:
            subprocess.run(["python", "menu.py"], check=True)  # Abrir a nova janela
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao abrir a janela de menu: {e}")
    else:
        print("Usuário ou senha incorretos.")

# Criar a janela
janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("800x400") 

# Textos no topo
texto2 = customtkinter.CTkLabel(janela, font=("Helvetica", 16), text="Faça login para ter acesso ao sistema.")
texto2.pack(padx=10, pady=10)

# Frame para inputs
frame_inputs = customtkinter.CTkFrame(janela, border_width=1, border_color="white")
frame_inputs.pack(padx=20, pady=20, expand=True)

texto1 = customtkinter.CTkLabel(frame_inputs, font=("Helvetica", 18), text="Bem-vindo!")
texto1.pack(padx=10, pady=10)

# Inputs
email = customtkinter.CTkEntry(frame_inputs, placeholder_text="Email", font=("Helvetica", 14))
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(frame_inputs, placeholder_text="Senha", show="•", font=("Helvetica", 14))
senha.pack(padx=10, pady=10)

# Botão de login
botao = customtkinter.CTkButton(frame_inputs, text="Login", font=("Helvetica", 14), command=verificar_login)
botao.pack(padx=10, pady=10)

# Iniciar o loop da janela
janela.mainloop()


