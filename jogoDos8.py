# https://github.com/LUCIANOGFORTES02/JogoDos8/blob/main/jogoDos8.py

import copy
# matriz=[ ['0','1','2'],['7','8','3'],['6','5','4'] ]
# Resultado esperado
resposta = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

# matriz=[['1','3','6'],['4','2','0'],['7','5','8']]
matriz = [['1', '3', '0'], ['4', '5', '6'], ['7', '8', '2']]
matriz = [['4', '1', '3'], ['5', '6', '0'], ['7', '8', '2']]
matrizTeste = [['0', '6', '1'], ['4', '5', '3'], ['7', '8', '2']]
# matriz=[['6','5','1'],['4','8','0'],['7','2','3']]

from heapq import heappop, heappush
from random import shuffle
from time import sleep
import numpy
from copy import deepcopy
from jogo import JogoDosOito

# import numpy

# resposta=[['1','2','3'],['8','0','4'],['7','6','5']]

# matriz=[ ['1','2','3'],['4','5','0'],['6','7','8'] ]
# matriz=[ ['1','3','0'],['4','5','6'],['7','8','2'] ]
# matriz=[ ['1','2','3'],['7','4','5'],['0','8','6'] ]


#nao encontra solução
#matrizTeste=[ ['2','3','1'],['4','5','7'],['6','8','0'] ] # 
# matriz=[ ['2','3','1'],['4','5','7'],['6','8','0'] ] #ñ é encontrada na busca gulosa
# matriz=[ ['7','8','0'],['4','5','6'],['2','1','3'] ] #não é encontrada na busca gulosa nem na heuristica
# matriz=[ ['8','7','6'],['5','4','3'],['2','1','0'] ] #não é encontrada na busca gulosa nem na heuristica
# matriz=[ ['2','3','1'],['4','5','7'],['6','8','0'] ] #não é encontrada na busca gulosa

# Criar tabuleiro
def imprimindoTablueiro(matriz):
    for i in range(0, 3):
        print("|".join(matriz[i]))  # unir as strings

        if (i < 2):
            print("------")
    print("\n")


def criandoTabuleiro():
    print("Digite o estado inicial :")
    matriz = []
    for i in range(0, 3):
        linha = []
        for j in range(0, 3):
            linha.append(
                str(input("Digite o valor [" + str(i) + "," + str(j) + "]:")))
            # linha.append('0')
        matriz.append(linha)
    return matriz


# Função para verificar se o movimento é valido
def verifica(x, y):
    v = True
    if (x < 0 or x > 2):
        v = False
    if (y < 0 or y > 2):
        v = False

    return v

# Função para realizar os movimentos
# Recebe como parametros a matriz
# Gera todos os filhos do estado em branco


def movimento(matriz):
    jogadas = []  # Gravar as jogadas
    valor = '0'
    x, y = localizar(matriz, valor)

    # sobe
    Vx = x-1
    Vy = y
    if verifica(Vx, Vy):  # realiza as trocas dos elementos
        copia = copy.deepcopy(matriz)
        m = copia[x][y]
        copia[x][y] = copia[Vx][Vy]
        copia[Vx][Vy] = m
        jogadas.append(copia)

    # desce
    Vx = x+1
    Vy = y
    if verifica(Vx, Vy):
        copia = copy.deepcopy(matriz)
        m = copia[x][y]
        copia[x][y] = copia[Vx][Vy]
        copia[Vx][Vy] = m
        jogadas.append(copia)

    # direita
    Vx = x
    Vy = y+1
    if verifica(Vx, Vy):
        copia = copy.deepcopy(matriz)
        m = copia[x][y]
        copia[x][y] = copia[Vx][Vy]
        copia[Vx][Vy] = m
        jogadas.append(copia)

    # esquerda
    Vx = x
    Vy = y-1
    if verifica(Vx, Vy):
        copia = copy.deepcopy(matriz)
        m = copia[x][y]
        copia[x][y] = copia[Vx][Vy]
        copia[Vx][Vy] = m
        jogadas.append(copia)

    return jogadas


# Função para localizar o espaço vazio
def localizar(matriz, valor):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == valor:
                return i, j

# Heuristica distância de Manhattan


def distaciaDeManhattan(matriz, resposta):
    dist = 0
    for i in matriz:
        for j in i:
            # if not (j=='0'):#Não considera a movimentação da pedra branca
            xAtual, yAtual = localizar(matriz, j)
            xCorreto, yCorreto = localizar(resposta, j)
            distancia = abs(int(xAtual-xCorreto)) + \
                abs(int(yAtual-yCorreto))  # Distancia de Manhattan
            dist += distancia

    return dist


def menorSomatorio(filhos):
    distanciasDosFilhos = []
    for i in filhos:
        distanciasDosFilhos.append(distaciaDeManhattan(i, resposta))
    print("Vetor de distancia dos filhos")
    print(distanciasDosFilhos)
    posVet = distanciasDosFilhos.index(min(distanciasDosFilhos))
    # retorna o filho que tem a menor distancia das peças
    return filhos[posVet]

# Número de elementos na posição errada


def posicaoErrada(matriz, resposta):
    cont = 0
    for i in range(3):
        for j in range(3):
            if matriz[i][j] != resposta[i][j]:
                cont += 1
    return cont

def MatrizEmString(s):
    s1 = s[0] + s[1] + s[2]
    return ''.join([str(v) for v in s1])


# Busca gulosa com fronteira muito grande são todos os nós que ainda não foram expandidos
def busca_heuristica2(matrizPai, resposta=JogoDosOito.objetivo):
    h = []
    # Adiciona os elementos a heap  (distancia de manhattan , nó)
    heappush(h, (distaciaDeManhattan(matrizPai, resposta), matrizPai, 0))
    visitados = [matrizPai]
    Dicionario=dict()
    cont = 0
    fronteira=0
    qtdnos=0
    while (len(h) > 0):
        if len(h)>fronteira:#Pegar a maior fornteira
            fronteira = len(h)
        
        cont += 1
        
        (_,pai, movimentosPai) = heappop(h)  # Retira o menor elemento da heap

        #imprimindoTablueiro(pai)

        for filho in movimento(pai):
            qtdnos+=1
            if filho not in visitados:
                visitados.append(filho)
                Dicionario[MatrizEmString(filho)] = pai
                if filho == resposta:
                    print("Solução encontrada")
                    print("Tamanho do vetor dos nós que são visitados "+str(len(visitados)))
                    print("Quantidades de movimento "+str(cont))
                    print("Maior fronteira de estados guardada "+ str(fronteira))
                    print("Quantidade de nós geradas "+ str(qtdnos))
                    print("Profundidade " + str(movimentosPai+1))
                    resposta=[]
                    node=filho
                    x=0
                    while node != matrizPai:
                        resposta.append(node)
                        node = Dicionario[MatrizEmString(node)]
                    resposta.append(matrizPai)
                    resposta.reverse()
                    for i in resposta: 
                        print(x,"\n")
                        imprimindoTablueiro(i)
                        x+=1

                    
                    return resposta

                else:
                    movimentosFilho = movimentosPai + 1
                    heappush(h, (distaciaDeManhattan(filho, resposta), filho,movimentosFilho))

    print("Sem Solucao")


def buscaHeuristicaAEstrela(matrizPai, resposta):
    h = []
    # Tupla = valor do nó (movimentos já feitos + distância de Manhattan), movimentos já feitos, matriz
    # valor do nó da matriz pai = 0 + (distaciaDeManhattan(matrizPai,resposta)
    heappush(h, (distaciaDeManhattan(matrizPai, resposta), 0, matrizPai))
    visitados = [matrizPai]
    dicionario = dict()
    cont = 0
    while (len(h) > 0):
        cont += 1
        # print("\n"+str(cont)+"\n")
        (_, movimentosPai, pai) = heappop(h)  # Retira o menor elemento da heap
        # imprimindoTablueiro(pai)

        for filho in movimento(pai):
            if filho not in visitados:
                visitados.append(filho)
                filhoStr = MatrizEmString(filho)
                dicionario[filhoStr] = pai
                if filho == resposta:
                    resposta = []
                    node = filho
                    x = 0
                    while node != matrizPai:
                        resposta.append(node)
                        node = dicionario[MatrizEmString(node)]
                    resposta.append(matrizPai)
                    resposta.reverse()
                    for i in resposta:
                        print(x, "\n")
                        imprimindoTablueiro(i)
                        x += 1

                    return resposta
                else:
                    movimentosFilho = movimentosPai + 1
                    heappush(
                        h, (movimentosFilho + distaciaDeManhattan(filho, resposta), movimentosFilho, filho))

    print("Sem Solucao")
