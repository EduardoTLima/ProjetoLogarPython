import customtkinter as CTk
import tkinter as Tk
import sqlite3
from datetime import datetime
from chamada_sqlite import criar_tabelas

def janela_Logar(Janela_Inicial):
    global janela_Login

    #Definições da Janela:
    criar_tabelas()
    CTk.set_appearance_mode("light")
    CTk.set_default_color_theme("blue")
    janela_Login = Tk.Toplevel(Janela_Inicial)
    janela_Login.grab_set()
    janela_Login.title("Login")
    janela_Login.resizable(width=False, height=False)
    largura = 230
    altura = 250
    largura_tela = janela_Login.winfo_screenwidth()
    altura_tela = janela_Login.winfo_screenheight()
    posx = largura_tela/2 - largura/2
    posy = altura_tela/2 - altura/2
    janela_Login.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))
    
    #Elementos:
    texto = CTk.CTkLabel(janela_Login, text="Fazer Login")
    texto.pack(padx=10, pady=10)
    email = CTk.CTkEntry(janela_Login, placeholder_text="Seu e-mail")
    email.pack(padx=10, pady=10)
    senha = CTk.CTkEntry(janela_Login, placeholder_text="Sua senha", show="*")
    senha.pack(padx=10, pady=10)
    botao = CTk.CTkButton(janela_Login, text="Login", command=lambda: login(email, senha))
    botao.pack(padx=10, pady=10)
    botaoCad = CTk.CTkButton(janela_Login, text="Cadastro", command=lambda: cadastrar(janela_Login))
    botaoCad.pack(padx=10, pady=10)

    #Funções extras
    janela_Login.bind("<Escape>", lambda event: janela_Login.destroy())

    janela_Login.mainloop()

#Funções:
def login(email, senha):
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tecnicos WHERE email = ? AND senha = ?", (email.get(), senha.get()))
    tecnico = cursor.fetchall()
    con.close()

    if tecnico:
        email = tecnico[0][1]
        Tk.messagebox.showinfo("Login", "Login de administrador realizado com sucesso!")
        HistLogin(email, senha)
        janela_Login.destroy()
        import Janela_Cadastro
    else:
        Tk.messagebox.showerror("Erro","Email ou Senha inválido \nTente novamente")



def HistLogin(email, senha):
    data_login = datetime.now()
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO historico_login (nome, email, data_login) VALUES (?,?,?)",(email.get(), senha.get(), data_login))
    con.commit()
    con.close()

def cadastrar(janela_Login):
    from Janela_Cadastro import janela
    janela(janela_Login)

