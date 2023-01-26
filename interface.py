import tkinter as tk
from tkinter import * #importamos o pacote tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import threading
from threading import Thread
from random import shuffle

from jogoDos8 import busca_heuristica2,buscaHeuristicaAEstrela
from buscas import buscaEmLargura, buscaEmProfundidade, aplicandoCaminho
from jogo import JogoDosOito
from time import sleep

"""
def start_game():
    # Iniciar a busca em largura
    jogo = JogoDosOito()
    jogo.jogo[0] = [1, 3, ' ']
    jogo.jogo[1] = [4, 5, 6]
    jogo.jogo[2] = [7, 8, 2]
    
    caminho = buscaEmLargura(jogo)
    
    jogo.imprime()
    for direcao in caminho:
        jogo.move(direcao)
        update_game_state(jogo)
        root.update()
        sleep(1)

def reset_game():
    # Reiniciar o jogo
    pass

def update_game_state(jogo):
    for i in range(3):
        for j in range(3):
            game_matrix[i][j].config(text=jogo.jogo[i][j])



root = tk.Tk()

root.config(width=1000, height=1000)

start_button = tk.Button(root, text="Iniciar", command=start_game)
start_button.grid(row=4, column=0)
start_button.configure(width=5, height=3, font=("Arial"))

game_matrix = [[tk.Button(root, text=" ") for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        game_matrix[i][j].grid(row=i+1, column=j)
        
for i in range(3):
    for j in range(3):
        game_matrix[i][j].configure(width=4, height=2, bg="blue", font=("Arial", 24), fg="white")

status_label = tk.Label(root, text="Profundidade: 0\nEstados visitados: 0")
status_label

root.geometry("800x600+100+100")

root.mainloop()
"""

resposta = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

def start():
    global questao1,questao2,threadKill,thread
    mensagemProcessando["text"] = "Processando..."
    #questao1 = messagebox.askyesno('Escolha','Deseja ver a árvore?\nObs: A árvore é exibida até certo nível!')#pergunta se sim ou não
    #questao2 = False
   # if not(questao1):
      #  questao2 = messagebox.askyesno('Escolha','Deseja ver a animação?')#pergunta se sim ou não
    matrix = [[entrada.get(),entrada2.get(),entrada3.get()],[entrada4.get(),entrada5.get(),entrada6.get()],[entrada7.get(),entrada8.get(),entrada9.get()]]
    print("Aguarde o resultado final!\n")
    if(str(escolha.get())=='profundidade'):
        #if(questao2):
        #    mensagemProcessando["text"] = ""
        #    threadKill = threading.Event()
        #    thread=Thread(target=buscaEmProfundidade,args=(matrix,threadKill))#passa os parametros e a função para a thread
        #    thread.start()
        #    loadingStatus()
        #    return
        buscaEmProfundidade(matrix)
        mensagemProcessando["text"] = ""
    elif(str(escolha.get())=='largura'):
        #if(questao2):
        #    mensagemProcessando["text"] = ""
        #    threadKill = threading.Event()
        #    thread=Thread(target=buscaEmLargura,args=(matrix,threadKill))#passa os parametros e a função para a thread
        #    thread.start()
        #    loadingStatus()
        #    return
        buscaEmLargura(matrix)
        mensagemProcessando["text"] = ""
    elif(str(escolha.get())=='heuristica'):
        #if(questao2):
        #    mensagemProcessando["text"] = ""
        #    threadKill = threading.Event()
        #    thread=Thread(target=busca_heuristica2,args=(matrix,threadKill))#passa os parametros e a função para a thread
        #    thread.start()
        #    loadingStatus()
        #    return
        busca_heuristica2(matrix,resposta)
        mensagemProcessando["text"] = ""
    elif(str(escolha.get())=='A'):
        #if(questao2):
        #    mensagemProcessando["text"] = ""
        #    threadKill = threading.Event()
        #    thread=Thread(target=buscaHeuristicaAEstrela,args=(matrix,threadKill))#passa os parametros e a função para a thread
        #    thread.start()
        #    loadingStatus()
        #    return
        buscaHeuristicaAEstrela(matrix,resposta)
        mensagemProcessando["text"] = ""
    else:
        messagebox.showinfo('Algoritmo não selecionado.',"Escolha um método de busca antes de iniciar!")
        


def telaHome():#reset
    apagaJanela()
    global entrada,entrada1,entrada2,entrada3,entrada4,entrada5,entrada6,entrada7,entrada8,entrada9,escolha,mensagemProcessando
    mensagem = Label(window, text="Insira o estado Inicial", font="Arial 24")
    mensagem.pack()
    jogoDosOito = Frame(window)
    jogoDosOito.pack()
    entrada = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada.grid(row=0,column=0)
    entrada2 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada2.grid(row=0,column=1)
    entrada3 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada3.grid(row=0,column=2)
    entrada4 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada4.grid(row=1,column=0)
    entrada5 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada5.grid(row=1,column=1)
    entrada6 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada6.grid(row=1,column=2)
    entrada7 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada7.grid(row=2,column=0)
    entrada8 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada8.grid(row=2,column=1)
    entrada9 = ttk.Entry(jogoDosOito, font="arial 20 bold",width=5)
    entrada9.grid(row=2,column=2)
    
    #radioButtons:
    mensagemAlg = Label(window, text="Selecione o algoritmo de busca: ", font="arial 24 bold")
    mensagemAlg.pack()
    escolha = StringVar()#Guarda o valor escolhido
    escolha.set(1)
    escolha1 = ttk.Radiobutton(window,text='Busca em Profundidade', value='profundidade' ,cursor="hand2",variable = escolha)
    escolha2= ttk.Radiobutton(window,text='Busca em Largura', value='largura', cursor="hand2",variable = escolha)
    escolha3 = ttk.Radiobutton(window,text='Busca Heurística - Alg. Guloso', value='heuristica', cursor="hand2",variable = escolha)
    escolha4 = ttk.Radiobutton(window,text='Busca A*', value='A', cursor="hand2",variable = escolha)
    escolha1.pack(padx=(0,0))
    escolha2.pack(padx=(0,33))
    escolha3.pack(padx=(33,0))
    escolha4.pack(padx=(0,79))
    botao = ttk.Button(window, text="Iniciar", command=start,cursor="hand2")
    botao.pack()

    mensagemProcessando = Label(window, text="", font="Arial 10 normal")
    mensagemProcessando.pack()

def loadingStatus():
    frame = ttk.Frame()
    global pb
    pb = ttk.Progressbar(frame, length=300, mode='indeterminate')
    frame.pack()
    pb.pack()
    pb.start(10)#velocidade da barra
    
def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    return _list

def apagaJanela():
    try:
        if(thread.isAlive()):#se tiver alguma thread em execução então para ela
             threadKill.set()
    except:
        pass
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()


if __name__ == "__main__":  
    window = Tk()#instanciamos a classe tk
    window.title("IA - Jogo dos Oito")
    window.geometry("600x640+200+100")#largura x altura + pos_x + posy
    menu = Menu(window)
    window.config(menu=menu)
    menu.add_cascade(label='Resetar',command=telaHome)
    telaHome()
    window.mainloop()