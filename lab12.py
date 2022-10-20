def distancia(x1, y1, x2, y2):
    """Função que calcula a distância euclidiana entre 2 pontos no plano cartesiano"""
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


def construtor_matriz(m, n):
    """Função que constrói uma matriz de m linhas e n colunas, inteiramente de "-"."""
    matriz = []
    for k in range(m):
        linha = []
        for k in range(n):
            linha.append("-")
        matriz.append(linha)
    return matriz


def impressor_matriz(matriz):
    """Função que, dada uma matriz, a imprime."""
    for i in range(len(matriz)):
        for j in range(len(matriz[1])):
            if j == len(matriz[0]) - 1:
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")


def borda_quadrado(ci, cj, l, matriz):
    """Função que desenha as bordas de um quadrado lado l (sempre ímpar) centrado no ponto (cx, cy)
    em uma matriz."""
    for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if (i == ci - l//2 or i == ci + l//2) and (cj - l//2 <= j <= cj + l//2): # Desenhando as bordas
                    # de cima e de baixo
                    matriz[i][j] = "x"
                elif (ci - l//2 <= i <= ci + l//2) and (j == cj - l//2 or j == cj + l//2): # Desenhando as bordas
                    # esquerda e direita
                    matriz[i][j] = "x"
    return matriz



def quadrado(ci, cj, l, matriz):
    """Função recursiva que desenha um quadrado de lado l (sempre ímpar) centrado no ponto (cx, cy)
    em uma matriz."""
    if l == 1: # Caso o lado do quadrado seja 1, o quadrado será apenas o seu centro
        matriz[ci][cj] = "x"
        return matriz
    else: # Do contrário, basta que seja feita a borda do quadrado de lado n e que haja uma recursão,
        # para que se realize a parte interna do quadrado inicial, ou seja, um novo quadrado de lado
        # n - 2.
        matriz = borda_quadrado(ci, cj, l, matriz)
        return quadrado(ci, cj, l - 2, matriz)


def borda_circulo(ci, cj, r, matriz):
    """Função que desenha o contorno de um círculo de raio r e centrado no ponto (ci, cj)"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if r - (2)**(1/2) < distancia(i, j, ci, cj) <= r: # Para que o ponto Aij pertença a borda
                # de um círculo de raio r e centro (ci, cj), basta que ele esteja a uma distancia menor
                # ou igual à r de (ci, cj) e que essa distancia seja maior do que r - sqrt(2), visto que
                # sqrt(2) seria a distância de um determinado ponto à sua diagonal, ou seja, basta que
                # um ponto esteja a uma distancia menor ou igual ao raio e maior do que o elemento de 
                # sua diagonal interna na direção do centro.
                matriz[i][j] = "x"
    return matriz


def circulo(ci, cj, r, matriz):
    """Função recursiva que desenha um circulo de raio centrado no ponto (cx, cy) em uma matriz."""
    if r == 0: # Caso o raio do círculo seja 0, ele será apenas o seu centro
        matriz[ci][cj] = "x"
        return matriz
    else: # Do contrário, basta que seja calculada sua borda, de raio r, e que haja uma recursão,
        # para que se realize a parte interna do  círculo inicial, ou seja, um novo círculo de raio
        # r - 1
        matriz = borda_circulo(ci, cj, r, matriz)
        return circulo(ci, cj, r - 1, matriz)

# Início das entradas

m, n = map(int, input().split(" "))
tela = construtor_matriz(m, n)


q = int(input())
desenhos = []
for k in range(q):
    desenho = input().split(" ")
    desenhos.append(desenho) # 

for d in desenhos:
    if d[0] == "quadrado":
        tela = quadrado(int(d[1]), int(d[2]), int(d[3]), tela)
    elif d[0] == "circulo":
        tela = circulo(int(d[1]), int(d[2]), int(d[3]), tela)

impressor_matriz(tela)
