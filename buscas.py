from jogo import JogoDosOito
import networkx as nx
from copy import deepcopy
import random
from pyvis.network import Network
import matplotlib.pyplot as plt
from IPython.display import display
from collections import deque

def adicionaEstadoFilho(arvore, estadoPai, direcao, nome):
    jogoAdd = deepcopy(estadoPai[0]) 
    jogoAdd.move(direcao)
    estado = (jogoAdd, direcao, nome)
    arvore.add_node(nome)
    nx.set_node_attributes(arvore, estado, nome)
    return estado
    
def buscaEmProfundidade():
    jogo = JogoDosOito()
    jogo.jogoAleatorio()

    estadoInicial = (jogo, '', 0) # jogo, direcao de que veio
    arvoreDeBusca = nx.Graph()
    arvoreDeBusca.add_node(0)
    nx.set_node_attributes(arvoreDeBusca, estadoInicial, 0)

    cont = 1
    menor = 10
    pilha = [estadoInicial]
    visitados = []
    estadoMelhor = estadoInicial
    while pilha and cont <100000:
        estadoAtual = pilha.pop()
        # print('Estado atual: ')
        # estadoAtual[0].imprime()
        
        if estadoAtual[0].quantidadePosicoesErradas() <= menor:
            menor = estadoAtual[0].quantidadePosicoesErradas()
            estadoMelhor = estadoAtual[0]
            estadoMelhor.imprime()
            print(estadoMelhor.quantidadePosicoesErradas())
        
        # print('\n')
        # for i in pilha:
        #     print(i[2], end='')
        # print('\n')
    
        # for i in pilha:
        #     print(i[2], ': ')
        #     i[0].imprime()
            
        if estadoAtual[0].estaCerto():
            print('esta certo')
            break
        visitados.append(estadoAtual[0])
        for teste in visitados:
            if estadoAtual[0].igual(teste):
                continue
        direcoes = estadoAtual[0].movimentosPossiveis()
        random.shuffle(direcoes)
        for direcao in direcoes:
            estadoFilho = adicionaEstadoFilho(arvoreDeBusca, estadoAtual, direcao, cont)
            pilha.append(estadoFilho)
            arvoreDeBusca.add_edge(estadoAtual[2], cont)
            # nx.draw(arvoreDeBusca, with_labels=True, node_size=1200, node_color='red')
            # plt.show()
            cont += 1
    print(cont)
    
def buscaEmLargura():
    jogo = JogoDosOito()
    jogo.jogoAleatorio()
    
    estadoInicial = (jogo, '', 0) # jogo, direcao de que veio, nome
    arvoreDeBusca = nx.Graph()
    arvoreDeBusca.add_node(0)
    nx.set_node_attributes(arvoreDeBusca, estadoInicial, 0)
    
    menor = 10
    cont = 1
    flag = False
    fronteira = []
    fronteira.append([estadoInicial])
    
    while(cont < 1000):
        fronteira.append([])
        for node in fronteira[-2]: 
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
                estadoFilho = adicionaEstadoFilho(arvoreDeBusca, node, direcao, cont)
                cont += 1
                fronteira[-1].append(estadoFilho)
                arvoreDeBusca.add_edge(node[2], estadoFilho[2])
                # nx.draw(arvoreDeBusca, with_labels=True, node_size=1200, node_color='red')
                # plt.show()
        if flag:
            break
                
# buscaEmProfundidade()
buscaEmLargura()
                
