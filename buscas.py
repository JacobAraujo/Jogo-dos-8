import random
from copy import deepcopy
from heapq import heappop, heappush

import numpy

from jogo import JogoDosOito
from jogoDos8 import busca_heuristica2


def getEstadoFilho(estadoPai, direcao, profundidade):
    jogoAdd = deepcopy(estadoPai[0])
    jogoAdd.move(direcao)
    listaDirecoes = deepcopy(estadoPai[1])
    listaDirecoes.append(direcao)
    estado = (jogoAdd, listaDirecoes, profundidade)
    return estado


def buscaEmProfundidade(jogo=JogoDosOito(), resposta=JogoDosOito.objetivo):
    # jogo, direcao de que veio, nome, profundidade
    estadoInicial = (jogo, [], 0, 0)

    pilha = [estadoInicial]
    menor = float('inf')
    maxIteracao = float('inf')
    visitados = set()
    estadosVisitados = 0
    maiorFronteira = 0

    profundidadeMaxima = 20
    while pilha:
        if len(pilha) > maiorFronteira:  # pega a maior fronteira que foi guardada
            maiorFronteira = len(pilha)

        estadoAtual = pilha.pop()
        
        if estadoAtual[2] > profundidadeMaxima:
            continue

        # visitado = False
        # for teste in visitados:
        #     if estadoAtual[0].igual(teste):
        #         visitado = True
        #         break
        # if visitado:
        #     continue

        if estadoAtual[0].distanciaDeManhattan() <= menor:
            menor = estadoAtual[0].distanciaDeManhattan()
            estadoMelhor = estadoAtual

        if estadoAtual[0].estaCerto():
            print('esta certo')
            break

        direcoes = estadoAtual[0].movimentosPossiveis()

        # if estadoAtual[1]:
        #     direcoes.remove(JogoDosOito.direcaoContraria(estadoAtual[1][-1]))

        random.shuffle(direcoes)

        for direcao in direcoes:
            estadoFilho = getEstadoFilho(
                estadoAtual, direcao, estadoAtual[2] + 1)                   
            pilha.append(estadoFilho)
        
        visitados.add(estadoAtual[0])
        estadosVisitados += 1  # Pega quantos nós foram visitados
        
        if estadosVisitados >= maxIteracao:
            break

    estadoMelhor[0].imprime()
    print(estadoMelhor[0].distanciaDeManhattan())
    print('Profundidade: ', estadoMelhor[2])
    print('Nos visitados: ', estadosVisitados)
    print('Maior fronteira: ', maiorFronteira)
    return estadoMelhor[1]


def buscaEmLargura(jogo, resposta=JogoDosOito().objetivo):
    # jogo, lista de direcoes de que veio, nome
    estadoInicial = (jogo, [], 0)

    # menor = 10
    profundidade = 0
    flag = False
    fronteira = []
    fronteira.append([estadoInicial])
    fronteira.append([])
    estadosVisitados = 0
    maiorFronteira = 0

    while (profundidade < 15):

        if len(fronteira[0]) > maiorFronteira:
            maiorFronteira = len(fronteira[0])

        while fronteira[0]:
            node = fronteira[0].pop()
            # if node[0].quantidadePosicoesErradas() <= menor:
            #     menor = node[0].quantidadePosicoesErradas()
            #     estadoMelhor = node[0]
            #     estadoMelhor.imprime()
            #     print(estadoMelhor.quantidadePosicoesErradas())

            estadosVisitados += 1  # estados verificados

            if node[0].estaCerto():
                print('esta certo')
                flag = True
                break
            direcoes = node[0].movimentosPossiveis()
            for direcao in direcoes:
                filho = getEstadoFilho(node, direcao, profundidade+1)
                fronteira[1].append(filho)
        fronteira[0] = fronteira[1]
        fronteira[1] = []
        # print('Profundidade: ', profundidade)
        if flag:
            break
        profundidade += 1

    node[0].imprime()
    print('Profundidade: ', profundidade)
    print('Nos visitados: ', estadosVisitados)
    print('Maior fronteira: ', maiorFronteira)
    return node[1]

def executaBuscaHeuristica():
    matriz = [['1', '3', '0'], ['4', '5', '6'], ['7', '8', '2']]
    resposta = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    busca_heuristica2(matriz, resposta)

def aplicandoCaminho(jogo, caminho):
    jogo.imprime()
    for direcao in caminho:
        jogo.move(direcao)
        jogo.imprime()


# jogo = JogoDosOito()
# # jogo.jogo[0] = [1, 2, ' ']
# # jogo.jogo[1] = [4, 5, 6]
# # jogo.jogo[2] = [3, 7, 8]

# # jogo.jogo[0] = [7, 3, ' ']
# # jogo.jogo[1] = [4, 8, 6]
# # jogo.jogo[2] = [2, 1, 5]

# jogo.jogo[0] = [1, 3, ' ']
# jogo.jogo[1] = [4, 5, 6]
# jogo.jogo[2] = [7, 8, 2]

# buscaEmProfundidade(jogo)