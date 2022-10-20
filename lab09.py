def menor_matriz(matriz1, matriz2):
    if len(matriz1) < len(matriz2) or len(matriz1) == len(matriz2):
        return matriz1
    else:
        return matriz2


def maior_matriz(matriz1, matriz2):
    if len(matriz1) > len(matriz2):
        return matriz1
    else:
        return matriz2


def calculadora_supermatrizes(matriz1, matriz2):
    """Função que calcula e imprime a dimensão da supermatriz comum entre as matrizes 1 e 2. Por definição, a matriz1
    é a matriz de menor dimensão. Como é garantido que uma existe uma supermatriz comum, é garantido que haja uma
    igualdade entre uma das quatros extremidades da menor matriz (matriz1) e um elemento qualquer de posição ij da
    maior matriz (matriz2). Logo, é suficiente que a posição desse elemento seja encontrada para se determinar as
    dimensões da supermatriz comum"""
    linha_supermatriz = 0
    coluna_supermatriz = 0
    for i in range(len(matriz2)):
        if linha_supermatriz == 0 and coluna_supermatriz == 0:  # Condicional que sai do loop caso a igualdade entre as
            # extremidades ja tenha sido encontrada
            for j in range(len(matriz2)):
                # Quando uma matriz menor está totalmente contida (seja apenas pelas linhas, ou apenas pelas colunas, ou
                # ou por ambas) na maior matriz, então a dimensão da linha, ou coluna, ou ambas, da supermatriz será
                # igual à respectiva dimensão da matriz maior. Por isso foram criadas as condicionais.
                if matriz1[0][0] == matriz2[i][j]:  # Caso no qual o elemento do canto superior esquerdo da matriz menor é
                    # igual a um elemento na posição ij na matriz 2
                    if len(matriz1) + i > len(matriz2):
                        linha_supermatriz = len(matriz1) + i
                    else:
                        linha_supermatriz = len(matriz2)
                    if len(matriz1) + j > len(matriz2):
                        coluna_supermatriz = len(matriz1) + j
                    else:
                        coluna_supermatriz = len(matriz2)
                    break
                elif matriz1[0][len(matriz1) - 1] == matriz2[i][j]:  # Caso no qual o elemento do canto superior direito da
                    # matriz menor é igual a um elemento na posição ij na matriz 2
                    if len(matriz1) + i > len(matriz2):
                        linha_supermatriz = len(matriz1) + i
                    else:
                        linha_supermatriz = len(matriz2)
                    if len(matriz1) + len(matriz2) - j - 1 > len(matriz2):
                        coluna_supermatriz = len(matriz1) + len(matriz2) - j - 1
                    else:
                        coluna_supermatriz = len(matriz2)
                    break
                elif matriz1[len(matriz1) - 1][0] == matriz2[i][j]:  # Caso no qual o elemento do canto inferior esquerdo da
                    # matriz menor é igual a um elemento na posição ij na matriz 2
                    if len(matriz1) + len(matriz2) - i - 1 > len(matriz2):
                        linha_supermatriz = len(matriz1) + len(matriz2) - i - 1
                    else:
                        linha_supermatriz = len(matriz2)
                    if len(matriz1) + j > len(matriz2):
                        coluna_supermatriz = len(matriz1) + j
                    else:
                        coluna_supermatriz = len(matriz2)
                    break
                elif matriz1[len(matriz1) - 1][len(matriz1) - 1] == matriz2[i][j]:  # Caso no qual o elemento do canto
                    # inferior direito da matriz menor é igual a um elemento na posição ij na matriz 2
                    if len(matriz1) + len(matriz2) - i - 1 > len(matriz2):
                        linha_supermatriz = len(matriz1) + len(matriz2) - i - 1
                    else:
                        linha_supermatriz = len(matriz2)
                    if len(matriz1) + len(matriz2) - j - 1 > len(matriz2):
                        coluna_supermatriz = len(matriz1) + len(matriz2) - j - 1
                    else:
                        coluna_supermatriz = len(matriz2)
                    break
        else:
            break
    print(linha_supermatriz, "x", coluna_supermatriz)


matrizes = []
m, n = input().split(" ")
while m != "0" and n != "0":
    matriz_m = []
    matriz_n = []
    for k in range(int(m)):
        linha = input().split(" ")
        for x in range(len(linha)):
            linha[x] = int(linha[x])
        matriz_m.append(linha)
    for k in range(int(n)):
        linha = input().split(" ")
        for x in range(len(linha)):
            linha[x] = int(linha[x])
        matriz_n.append(linha)
    matrizes.append(matriz_m)
    matrizes.append(matriz_n)
    m, n = input().split(" ")

for k in range(0, len(matrizes), 2):
    calculadora_supermatrizes(menor_matriz(matrizes[k], matrizes[k + 1]), maior_matriz(matrizes[k], matrizes[k + 1]))
