import tkinter as tk
from tkinter import * #importamos o pacote tkinter

from jogoDos8 import busca_heuristica2, buscaHeuristicaAEstrela
from buscas import buscaEmLargura, buscaEmProfundidade, aplicandoCaminho
from jogo import JogoDosOito
from time import sleep

def start_game():
    # Iniciar a busca em largura
    jogo = JogoDosOito()
    jogo.jogo[0] = [1, 3, ' ']
    jogo.jogo[1] = [4, 5, 6]
    jogo.jogo[2] = [7, 8, 2]

    matriz = [['1', '3', '0'], ['4', '5', '6'], ['7', '8', '2']]
    resposta = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    
    print("Selecione o metodo de busca:")
    print("1. Busca heuristica")
    print("2. Busca A*")
    print("3. Busca em largura")
    print("4. Busca em profundidade")

    escolha = "4"

    if escolha == "1":
        caminho = busca_heuristica2(matriz, resposta)
    elif escolha == "2":
        caminho = buscaHeuristicaAEstrela(matriz, resposta)
    elif escolha == "3":
        caminho = buscaEmLargura(jogo)
    elif escolha == "4":
        caminho = buscaEmProfundidade(jogo)
    else:
        print("Opcao invalida")
        return
    
    print('iniciando...')
    if escolha == "1" or escolha == "2":
        # para busca heuristica
        for estado in caminho:
            for i in range(3):
                for j in range(3):
                    estado[i][j] = int(estado[i][j])
            jogo = JogoDosOito()
            jogo.jogo[0] = estado[0]
            jogo.jogo[1] = estado[1]
            jogo.jogo[2] = estado[2]
            update_game_state(jogo)
            root.update()
            sleep(1)
    if escolha == '3' or escolha == '4':
        jogo.imprime()
        for direcao in caminho:
            jogo.move(direcao)
            jogo.imprime()
            update_game_state(jogo)
            root.update()
            sleep(1)

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