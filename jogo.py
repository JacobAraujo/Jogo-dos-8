import math
import random


class JogoDosOito:

    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, ' ']]

    def __init__(self):
        self.jogo = []
        for i in range(3):
            self.jogo.append([[], [], []])

    # carrega uma tabela aleatória do jogo dos 8
    def jogoAleatorio(self):
        valores = [1, 2, 3, 4, 5, 6, 7, 8, ' ']
        for i in range(3):
            for j in range(3):
                self.jogo[i][j] = valores.pop(
                    random.randint(0, len(valores)-1))

    def distanciaManhattan(self, manhattan):
        sumo = 0

        for i in range(3):
            for j in range(3):
                sumo += manhattan(self.jogo[i][j], i, j)

        return sumo

    # Distância manhattan de fato
    def manhattan(p, i, j):
        val1 = 0
        val2 = 0
        if p == 1:
            val1 = i
            val2 = j
        elif p == 2:
            val1 = i
            val2 = j - 1
        elif p == 3:
            val1 = i
            val2 = j - 2
        elif p == 4:
            val1 = i - 1
            val2 = j
        elif p == 5:
            val1 = i - 1
            val2 = j - 1
        elif p == 6:
            val1 = i - 1
            val2 = j - 2
        elif p == 7:
            val1 = i - 2
            val2 = j
        else:
            val1 = i - 2
            val2 = j - 1

        return math.abs(val1) + math.abs(val2)

    # imprime no formato de tabela -> pode ser substituido pela interface
    def imprime(self):
        print('Tabela: ')
        for i in self.jogo:
            print(i)

    # vê se o estado atual é igual ao objetivo
    def estaCerto(self):
        return self.jogo == JogoDosOito.objetivo

    # retorna um vetor[i, j] que vai indicar a posicao de num

    def posicao(self, num):
        for i in range(3):
            for j in range(3):
                if self.jogo[i][j] == num:
                    return [i, j]

    # move o espaço vazio para alguma direção
    def move(self, direcao):
        if direcao == 'esquerda':
            posicaoDoVazio = self.posicao(' ')
            posicaoDoNumero = [posicaoDoVazio[0], posicaoDoVazio[1]-1]
            self.jogo[posicaoDoVazio[0]][posicaoDoVazio[1]
                                         ] = self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]]
            self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]] = ' '
        elif direcao == 'direita':
            posicaoDoVazio = self.posicao(' ')
            posicaoDoNumero = [posicaoDoVazio[0], posicaoDoVazio[1]+1]
            self.jogo[posicaoDoVazio[0]][posicaoDoVazio[1]
                                         ] = self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]]
            self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]] = ' '
        elif direcao == 'cima':
            posicaoDoVazio = self.posicao(' ')
            posicaoDoNumero = [posicaoDoVazio[0]-1, posicaoDoVazio[1]]
            self.jogo[posicaoDoVazio[0]][posicaoDoVazio[1]
                                         ] = self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]]
            self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]] = ' '
        elif direcao == 'baixo':
            posicaoDoVazio = self.posicao(' ')
            posicaoDoNumero = [posicaoDoVazio[0]+1, posicaoDoVazio[1]]
            self.jogo[posicaoDoVazio[0]][posicaoDoVazio[1]
                                         ] = self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]]
            self.jogo[posicaoDoNumero[0]][posicaoDoNumero[1]] = ' '

    def movimentosPossiveis(self):
        # verifica quais movimentos podem ser feitos e retorna as direçoes
        direcoes = ['esquerda', 'direita', 'baixo', 'cima']
        posicaoDoVazio = self.posicao(' ')
        if posicaoDoVazio[0] == 0:
            direcoes.remove('cima')
        if posicaoDoVazio[0] == 2:
            direcoes.remove('baixo')
        if posicaoDoVazio[1] == 0:
            direcoes.remove('esquerda')
        if posicaoDoVazio[1] == 2:
            direcoes.remove('direita')
        return direcoes
    
    def direcaoContraria(direcao):
        if direcao == 'baixo':
            return 'cima'
        if direcao == 'cima':
            return 'baixo'
        if direcao == 'esquerda':
            return 'direita'
        if direcao == 'direita':
            return 'esquerda'

    def igual(self, jogoComparado):
        for i in range(3):
            for j in range(3):
                if self.jogo[i][j] != jogoComparado.jogo[i][j]:
                    return False
        return True

    def quantidadePosicoesErradas(self):
        cont = 0
        for i in range(3):
            for j in range(3):
                if self.jogo[i][j] != JogoDosOito.objetivo[i][j]:
                    cont += 1
        return cont

    def distanciaDeManhattan(self):
        cont = 0
        num = 1
        posicaoAtual = [0, 0]
        for i in range(3):
            for j in range(3):
                posicaoAtual = self.posicao(num)
                distanciaHorizontal = abs(i - posicaoAtual[0])
                distanciaVertical = abs(j - posicaoAtual[1])
                cont += distanciaHorizontal + distanciaVertical
                if type(num) == int:
                    num += 1
                if num == 9:
                    num = ' '
        return cont

# jogo = JogoDosOito()
# jogo.jogoAleatorio()
# jogo.imprime()

# print(jogo.distanciaDeManhattan())
