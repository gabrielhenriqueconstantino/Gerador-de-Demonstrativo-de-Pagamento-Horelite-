import customtkinter
from PIL import Image, ImageTk, ImageDraw, ImageOps
import os

# Função para arredondar as bordas e adicionar uma borda branca
def add_border_and_rounded_corners(image, border_size, radius):
    # Adicionar uma borda branca ao redor da imagem
    border_image = ImageOps.expand(image, border=border_size, fill="white")
    
    # Criar uma máscara para as bordas arredondadas
    mask = Image.new("L", border_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        [(0, 0), (border_image.size[0], border_image.size[1])],
        radius,
        fill=255
    )
    
    # Aplicar a máscara à imagem com a borda
    rounded_image = border_image.copy()
    rounded_image.putalpha(mask)
    
    return rounded_image

# Função para mudar o cursor para "hand2" quando o mouse passa por cima
def on_enter(event):
    event.widget.configure(cursor="hand2")

# Função para voltar o cursor ao normal quando o mouse sai
def on_leave(event):
    event.widget.configure(cursor="")

# Função para abrir a nova janela ao clicar na imagem
def on_click(event):
    janela.destroy()
    os.system("python cad_funcionarios/cadastrar.py")


# Criar a janela
janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("1000x500")

# Textos no topo
texto2 = customtkinter.CTkLabel(janela, font=("Helvetica", 18), text='Seja bem vindo!')
texto2.pack(padx=10, pady=10)

# Criar um frame para conter as imagens
frame_imagens = customtkinter.CTkFrame(janela)
frame_imagens.pack(pady=20)

# Carregar as imagens usando o PIL
imagem1_pil = Image.open("horelite.png")
imagem2_pil = Image.open("cadastro.png")

# Tamanho da borda e raio das bordas arredondadas
radius = 6
border_size = 3

# Adicionar borda branca e bordas arredondadas às imagens
imagem1_bordered_rounded = add_border_and_rounded_corners(imagem1_pil, border_size, radius)
imagem2_bordered_rounded = add_border_and_rounded_corners(imagem2_pil, border_size, radius)

# Converter as imagens para o formato Tkinter
imagem1_tk = ImageTk.PhotoImage(imagem1_bordered_rounded)
imagem2_tk = ImageTk.PhotoImage(imagem2_bordered_rounded)

# Exibir a primeira imagem
label_imagem1 = customtkinter.CTkLabel(frame_imagens, image=imagem1_tk, text=None)
label_imagem1.pack(side="right", padx=30)

# Exibir a segunda imagem
label_imagem2 = customtkinter.CTkLabel(frame_imagens, image=imagem2_tk, text=None)
label_imagem2.pack(side="left", padx=30)

# Associar os eventos de entrada e saída do mouse às imagens
label_imagem1.bind("<Enter>", on_enter)
label_imagem1.bind("<Leave>", on_leave)
label_imagem2.bind("<Enter>", on_enter)
label_imagem2.bind("<Leave>", on_leave)

# Associar o evento de clique à imagem cadastro.png
label_imagem2.bind("<Button-1>", on_click)

janela.mainloop()





