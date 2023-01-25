import tkinter as tk
from buscas import buscaEmLargura, buscaEmProfundidade, aplicandoCaminho
from jogo import JogoDosOito
from time import sleep

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
