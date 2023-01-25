import random
from copy import deepcopy
import numpy

from jogo import JogoDosOito

def getEstadoFilho(estadoPai, direcao, nome, profundidade):
    jogoAdd = deepcopy(estadoPai[0])
    jogoAdd.move(direcao)
    estado = (jogoAdd, direcao, nome, profundidade)
    return estado

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
        lugarCerto = distanciasDeManhattan.index(
            filho[0].distanciaDeManhattan())
        filhosOrdenados[lugarCerto] = filho
    return filhosOrdenados

def buscaEmProfundidade():
    jogo = JogoDosOito()
    # jogo.jogo[0] = [1, 2, ' ']
    # jogo.jogo[1] = [4, 5, 6]
    # jogo.jogo[2] = [3, 7, 8]
    
    # jogo.jogo[0] = [7, 3, ' ']
    # jogo.jogo[1] = [4, 8, 6]
    # jogo.jogo[2] = [2, 1, 5]  
    
    jogo.jogo[0] = [1, 3, ' ']
    jogo.jogo[1] = [4, 5, 6]
    jogo.jogo[2] = [7, 8, 2]

    # jogo, direcao de que veio, nome, profundidade
    estadoInicial = (jogo, '', 0, 0)

    cont = 1
    pilha = [estadoInicial]
    menor = float('inf')
    visitados = []
    estadosVisitados = 0
    maiorFronteira = 0

    profundidadeMaxima = 10
    while pilha:
        if len(pilha) > maiorFronteira: # pega a maior fronteira que foi guardada
            maiorFronteira = len(pilha)        
        
        estadoAtual = pilha.pop() 
        
        visitado = False
        for teste in visitados:
            if estadoAtual[0].igual(teste):
                visitado = True
                break
        if visitado:
            continue
        
        visitados.append(estadoAtual[0])
        
        if estadoAtual[0].distanciaDeManhattan() <= menor:
            menor = estadoAtual[0].distanciaDeManhattan()
            estadoMelhor = estadoAtual
        
        if estadoAtual[0].estaCerto():
            print('esta certo')
            break
        
        estadosVisitados += 1 # Pega quantos nós foram visitados

        if estadoAtual[3] > profundidadeMaxima:
            continue
            
        direcoes = estadoAtual[0].movimentosPossiveis()

        if estadoAtual[1]:
            direcoes.remove(JogoDosOito.direcaoContraria(estadoAtual[1]))
        
        random.shuffle(direcoes)
        
        for direcao in direcoes:
            estadoFilho = getEstadoFilho(
                estadoAtual, direcao, cont, estadoAtual[3] + 1)
            pilha.append(estadoFilho)
            cont += 1

    estadoMelhor[0].imprime()
    print('Profundidade: ', estadoMelhor[3])
    print('Nos visitados: ', estadosVisitados)
    print('Maior fronteira: ', maiorFronteira)


def buscaEmLargura():
    jogo = JogoDosOito()
    # jogo.jogo[0] = [1, ' ', 3]
    # jogo.jogo[1] = [2, 5, 6]
    # jogo.jogo[2] = [4, 7, 8]

    jogo.jogo[0] = [1, 3, ' ']
    jogo.jogo[1] = [4, 5, 6]
    jogo.jogo[2] = [7, 8, 2]

    estadoInicial = (jogo, '', 0)  # jogo, direcao de que veio, nome

    menor = 10
    cont = 1
    profundidade = 0
    flag = False
    fronteira = []
    fronteira.append([estadoInicial])
    fronteira.append([])
    estadosVisitados = 0
    maiorFronteira = 0

    while (profundidade < 31):
        
        if len(fronteira[0]) > maiorFronteira:
            maiorFronteira = len(fronteira[0])
        
        while fronteira[0]:
            node = fronteira[0].pop()
            # if node[0].quantidadePosicoesErradas() <= menor:
            #     menor = node[0].quantidadePosicoesErradas()
            #     estadoMelhor = node[0]
            #     estadoMelhor.imprime()
            #     print(estadoMelhor.quantidadePosicoesErradas())
            
            estadosVisitados += 1 # estados verificados

            if node[0].estaCerto():
                print('esta certo')
                flag = True
                break
            direcoes = node[0].movimentosPossiveis()
            for direcao in direcoes:
                filho = getEstadoFilho(node, direcao, cont, profundidade+1)
                cont += 1
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
    
def movimento(matriz=JogoDosOito()):
    direcoes = matriz.movimentosPossiveis()
    filhos = []
    for direcao in direcoes:
        jogoAdd = deepcopy(matriz)
        jogoAdd.move(direcao)
        filhos.append(jogoAdd)
    return filhos

def menorSomatorio(filhos):
    menor = float('inf')
    for filho in filhos:
        if filho.distanciaDeManhattan() < menor:
            melhorFilho = filho
            menor = filho.distanciaDeManhattan()
    return melhorFilho
    
def buscaHeuristica(matrizPai=JogoDosOito(), resposta=JogoDosOito.objetivo):
    custoDeEspaco=0
    nivel=0#Nível da árvore
    visitados=[matrizPai.jogo]#Começa com o pai
    while(True):
        if(matrizPai.estaCerto()):
            print("Solucao encontrada")
            break
        nivel+=1
        jogadasPossiveis=[]
        for filho in movimento(matrizPai):
            if filho.jogo not in visitados:
               #visitados.append(filho)
                jogadasPossiveis.append(filho)
                #visitados.append(filho)
        print("Tamanho dos visitados = "+str(len(visitados)))
        custoDeEspaco+=len(jogadasPossiveis)#Todos os filhos gerados
        try:
            matrizPai = menorSomatorio(jogadasPossiveis)#Retorna o filho com as peças menos distantes
            matrizPai.imprime()
        except:
            print("NAO POSSUI SOLUCAO")
            break
        visitados.append(matrizPai.jogo)
        
jogo = JogoDosOito()

# jogo.jogo[0] = [1, ' ', 3]
# jogo.jogo[1] = [2, 5, 6]
# jogo.jogo[2] = [4, 7, 8]

jogo.jogo[0] = [1, 3, ' ']
jogo.jogo[1] = [4, 5, 6]
jogo.jogo[2] = [7, 8, 2]

buscaHeuristica(jogo)
