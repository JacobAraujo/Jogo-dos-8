from jogo import JogoDosOito
import networkx as nx
from copy import deepcopy
import random
from collections import deque

# Falta oegar o caminho até a solução. Vou fazer isso usando o propriedade "direcao" na tupla "estado" para
# retroceder o estado até o estado inicial pegando o caminho inverso

def getEstadoFilho(estadoPai, direcao, nome, profundidade):
    jogoAdd = deepcopy(estadoPai[0]) 
    jogoAdd.move(direcao)
    estado = (jogoAdd, direcao, nome, profundidade)
    return estado

def adicionaNaArvore(arvore, estado):
    arvore.add_node(estado[2])
    nx.set_node_attributes(arvore, estado, estado[2])
    
def getFilhos(estado, direcoes):
    filhos = []
    cont = estado[2]
    for direcao in direcoes:
        filhos.append(getEstadoFilho(estado, direcao, cont))
        cont += 1    
    return filhos

def ordenaFilhos(filhos):
    distanciasDeManhattan = []
    filhosOrdenados = []
    for filho in filhos:
        filhosOrdenados.append(filho)        
    for filho in filhos:
        distanciasDeManhattan.append(filho[0].distanciaDeManhattan())
    distanciasDeManhattan.sort()
    for filho in filhos:
        lugarCerto = distanciasDeManhattan.index(filho[0].distanciaDeManhattan())
        filhosOrdenados[lugarCerto] = filho
    return filhosOrdenados

def personalizaEscolha(filhos):
    filhosPersonalizado = []
    num = 40
    for filho in filhos:
        for i in range(num):
            filhosPersonalizado.append(filho)
        num -= 10
    return filhosPersonalizado
    
def buscaEmProfundidade():
    jogo = JogoDosOito()
    jogo.jogo[0] = [1, 2, ' ']
    jogo.jogo[1] = [4, 5, 6]
    jogo.jogo[2] = [3, 7, 8]

    estadoInicial = (jogo, '', 0, 0) # jogo, direcao de que veio, nome, profundidade

    cont = 1
    menor = 10
    pilha = [estadoInicial]
    visitados = []
    estadoMelhor = estadoInicial
    
    profundidadeMaxima = 31
    while pilha and cont <100000:
        estadoAtual = pilha.pop() # pilha = [1, 3, 4]
        # print('Estado atual: ')
        # estadoAtual[0].imprime()  
        
        if estadoAtual[0].quantidadePosicoesErradas() <= menor:
            menor = estadoAtual[0].quantidadePosicoesErradas()
            estadoMelhor = estadoAtual[0]
            estadoMelhor.imprime()
            print(estadoMelhor.quantidadePosicoesErradas())
            
        if estadoAtual[0].estaCerto():
            print('esta certo')
            break
        visitados.append(estadoAtual[0])
        
        if estadoAtual[3] > profundidadeMaxima:
            continue
        
        for teste in visitados:
            if estadoAtual[0].igual(teste):
                continue
        direcoes = estadoAtual[0].movimentosPossiveis()
        random.shuffle(direcoes)
        for direcao in direcoes:
            estadoFilho = getEstadoFilho(estadoAtual, direcao, cont, estadoAtual[3] + 1)
            pilha.append(estadoFilho)
            cont += 1
    print(cont)
    
def buscaEmLargura():
    jogo = JogoDosOito()
    # jogo.jogo[0] = [1, ' ', 3]
    # jogo.jogo[1] = [2, 5, 6]
    # jogo.jogo[2] = [4, 7, 8]
    jogo.jogoAleatorio()
    
    estadoInicial = (jogo, '', 0) # jogo, direcao de que veio, nome
    
    menor = 10
    cont = 1
    profundidade = 0
    flag = False
    fronteira = []
    fronteira.append([estadoInicial])
    fronteira.append([])
    
    while(profundidade < 31):
        while fronteira[0]:
            node = fronteira[0].pop() 
            if node[0].quantidadePosicoesErradas() <= menor:
                menor = node[0].quantidadePosicoesErradas()
                estadoMelhor = node[0]
                estadoMelhor.imprime()
                print(estadoMelhor.quantidadePosicoesErradas())
            if node[0].estaCerto():
                print('esta certo')
                flag = True
                break            
            direcoes = node[0].movimentosPossiveis()
            for direcao in direcoes:
                filho = getEstadoFilho(node, direcao, cont, profundidade+1)
                cont += 1
                fronteira[1].append(filho)
                # nx.draw(arvoreDeBusca, with_labels=True, node_size=1200, node_color='red')
                # plt.show()
        fronteira[0] = fronteira[1]
        fronteira[1] = []
        profundidade += 1
        print('Profundidade: ', profundidade)
        if flag:
            break

buscaEmLargura()
