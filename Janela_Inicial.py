import customtkinter as CTk
from tkinter import *
import tkinter as Tk

#Definições da Janela
CTk.set_appearance_mode("light")
CTk.set_default_color_theme("dark-blue")
Janela_inicial = CTk.CTk()
Janela_inicial.title("Inicio")
Janela_inicial.resizable(width=False, height=False)
largura = 700
altura = 390
largura_tela = Janela_inicial.winfo_screenwidth()
altura_tela = Janela_inicial.winfo_screenheight()
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2
Janela_inicial.geometry("%dx%d+%d+%d"% (largura, altura, posx, posy))

#Estrutura do código
img = Tk.PhotoImage(file="IMAGENS\ITCONNECT_LOGO.png")
imagem = Tk.Label(Janela_inicial, image=img)
imagem.pack(side=LEFT)
botaoimg = PhotoImage(file="IMAGENS\BOTAOADM.png")

#Frame
frame =CTk.CTkFrame(master=Janela_inicial, width=350, height=396, fg_color="#6FAEC7")
frame.propagate(TRUE)
frame.pack(side=RIGHT)

botaoTelaLogin = Tk.Button(frame, image=botaoimg, command= lambda: Logar(Janela_inicial))
botaoTelaLogin.place(x=300, y=20)
tecnico = CTk.CTkLabel(frame, text="Entrar como Técnico:", font=("Roboto", 12))
tecnico.place(x=180, y=20)
botaoIniciar = CTk.CTkButton(frame, text="Iniciar Chamada", font=("Roboto", 14), fg_color="#2F69DB", width=70, height=50)
botaoIniciar.place(x=130, y=170)

#Funções extras
Janela_inicial.bind("<Escape>", lambda event: Janela_inicial.destroy())

def Logar(Janela_inicial):
    from Janela_Login import janela_Logar
    janela_Logar(Janela_inicial)

Janela_inicial.mainloop()