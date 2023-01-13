from jogo import JogoDosOito
import networkx as nx
from copy import deepcopy

def adicionaEstadoFilho(arvore, estadoPai, direcao, nome):
    jogoAdd = deepcopy(estadoPai[0]) 
    jogoAdd.move(direcao)
    estado = (jogoAdd, direcao, estadoPai[2]+1)
    arvore.add_node(cont)
    nx.set_node_attributes(arvore, estadoPai, nome)
    

jogo = JogoDosOito()
jogo.jogoAleatorio()

camada = 0
estadoInicial = (jogo, '', 0) # jogo, direcao de que veio, camada
arvoreDeBusca = nx.Graph()
arvoreDeBusca.add_node(0)
nx.set_node_attributes(arvoreDeBusca, estadoInicial, 0)


cont = 1
pilha = [estadoInicial]
while pilha:
    estadoAtual = pilha.pop()
    direcoes = estadoAtual[0].movimentosPossiveis()
    for direcao in direcoes:
        adicionaEstadoFilho(arvoreDeBusca, estadoAtual, direcao, cont)
        print(arvoreDeBusca.nodes())
        cont += 1
        
