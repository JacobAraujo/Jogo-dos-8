from jogo import JogoDosOito
import networkx as nx
from copy import deepcopy
import random

def adicionaEstadoFilho(arvore, estadoPai, direcao, nome):
    jogoAdd = deepcopy(estadoPai[0]) 
    jogoAdd.move(direcao)
    estado = (jogoAdd, direcao)
    arvore.add_node(cont)
    nx.set_node_attributes(arvore, estado, nome)
    return estado
    

jogo = JogoDosOito()
jogo.jogoAleatorio()

camada = 0
estadoInicial = (jogo, '') # jogo, direcao de que veio
arvoreDeBusca = nx.Graph()
arvoreDeBusca.add_node(0)
nx.set_node_attributes(arvoreDeBusca, estadoInicial, 0)


cont = 1
pilha = [estadoInicial]
while pilha and cont <100000:
    estadoAtual = pilha.pop()
    estadoAtual[0].imprime()
    if estadoAtual[0].estaCerto():
        print('esta certo')
        break
    direcoes = estadoAtual[0].movimentosPossiveis()
    random.shuffle(direcoes)
    for direcao in direcoes:
        estadoFilho = adicionaEstadoFilho(arvoreDeBusca, estadoAtual, direcao, cont)
        pilha.append(estadoFilho)
        cont += 1
print(cont)
