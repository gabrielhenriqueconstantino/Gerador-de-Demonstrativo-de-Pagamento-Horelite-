import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from tkinter import * #importa o tkinter

#configurações da bliblioteca watchdog
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("File changed, restarting application...")
            os.execv(sys.executable, ['python'] + sys.argv)

#conteúdo principal da aplicação
def run_app():
    root = Tk()

# janela
    root.geometry("700x400")
    root.title("GeradorHolerith")
    root.config(bg="lightblue")

    # título de texto com fonte branca
    titulo = Label(root, text="Bem-vindo ao Gerador de Holerith", font=("Helvetica", 18, "bold"), bg="lightblue", fg="white")
    titulo.pack(pady=20)  # Adiciona um espaçamento vertical ao redor do título

    root.mainloop()

#configurações da bliblioteca watchdog - atualizar a aplicação a cada alteração
if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        run_app()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


