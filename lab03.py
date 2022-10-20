def impar(n):
    """Define se um número é impar ou não"""
    if n % 2 != 0:
        return True
    else:
        return False


def torre(n, coluna, linha):
    """Função que determinará a impressão do tabuleiro da torre"""
    # Criando listas iniciais que serão responsáveis por cada linha do tabuleiro conforme o tipo
    linha_letras = []
    linha_normal = []
    linha_peca = []
    for k in range(n):  # Criando as respectivas linhas com base nas entradas e especificações do usuário
        linha_letras.append(chr(97 + k))
        if k != int(ord(coluna) - 97):
            linha_normal.append("-")
            linha_peca.append("x")
        else:
            linha_normal.append("x")
            linha_peca.append("o")

    for k in range(n):  # Impressão das linhas ja prontas, com base em seu tipo, e do respecito número da linha
        if int(n - k) != int(linha):
            print(int(n - k), *linha_normal)
        else:
            print(int(n - k), *linha_peca)
    print(" ", *linha_letras)


def rei(n, coluna, linha):
    """Função que determinará a impressão do tabuleiro do rei"""
    # Criando as listas iniciais que serão responsáveis por cada linha do tabuleiro conforme o tipo
    linha_letras = []
    linha_sup_inf = []  # linhas superiores e inferiores à localização da peça
    linha_normal = []
    linha_peca = []
    for k in range(n):
        linha_normal.append("-")
        linha_letras.append(chr(97 + k))
        if k == int(ord(coluna) - 96) or k == int(ord(coluna) - 98):
            linha_sup_inf.append("x")
            linha_peca.append("x")
        elif k == int(ord(coluna) - 97):
            linha_sup_inf.append("x")
            linha_peca.append("o")
        else:
            linha_sup_inf.append("-")
            linha_peca.append("-")

    for k in range(n):
        print(int(n) - k, end=" ")
        if k == n - (int(linha) + 1):
            print(*linha_sup_inf)
        elif k == n - (int(linha) - 1):
            print(*linha_sup_inf)
        elif k == n - int(linha):
            print(*linha_peca)
        else:
            print(*linha_normal)
    print(" ", *linha_letras)


def peao(n, coluna, linha):
    """Função que determinará a impressão do tabuleiro do peão"""
    linha_normal = []
    linha_peca = []
    linha_sup = []  # Linha superior à posição da peça
    linha_letras = []
    for k in range(n):
        linha_normal.append("-")
        linha_letras.append(chr(97 + k))
        if k == ord(coluna) - 97:
            linha_peca.append("o")
            linha_sup.append("x")
        else:
            linha_peca.append("-")
            linha_sup.append("-")

    for k in range(n):
        print(int(n) - k, end=" ")
        if int(linha) == 2 and (k == n - (int(linha) + 1) or k == n - (int(linha) + 2)):  # Caso do peao na casa inicial
            print(*linha_sup)
        elif k == n - (int(linha) + 1):
            print(*linha_sup)
        elif k == n - (int(linha)):
            print(*linha_peca)
        else:
            print(*linha_normal)
    print(" ", *linha_letras)


def cavalo(n, coluna, linha):
    """Função que determinará a impressão do tabuleiro do cavalo"""
    linha_normal = []
    linha_peca = []
    linha_letras = []
    linha_sup_inf = []  # Linha imediatamente acima/abaixo da peça
    linha_2sup_inf = []  # Segunda linha imediatamente acima/abaixo da peça
    for k in range(n):
        linha_normal.append("-")
        linha_letras.append(chr(97 + k))
        if k == ord(coluna) - 98 or k == ord(coluna) - 96:
            linha_2sup_inf.append("x")
            linha_sup_inf.append("-")
            linha_peca.append("-")
        elif k == ord(coluna) - 99 or k == ord(coluna) - 95:
            linha_sup_inf.append("x")
            linha_2sup_inf.append("-")
            linha_peca.append("-")
        elif k == ord(coluna) - 97:
            linha_peca.append("o")
            linha_2sup_inf.append("-")
            linha_sup_inf.append("-")
        else:
            linha_sup_inf.append("-")
            linha_2sup_inf.append("-")
            linha_peca.append("-")

    for k in range(n):
        print(int(n) - k, end=" ")
        if k == n - int(linha):
            print(*linha_peca)
        elif k == n - int(linha) - 1 or k == n - int(linha) + 1:
            print(*linha_sup_inf)
        elif k == n - int(linha) - 2 or k == n - int(linha) + 2:
            print(*linha_2sup_inf)
        else:
            print(*linha_normal)
    print(" ", *linha_letras)


def bispo(n, coluna, linha):
    """Função que determinará a impressão do tabuleiro do bispo"""
    linha_letras = []
    linha_peca = []
    lista_linhas = []  # Lista que abrigará todas as linhas, em ordem decrescente (alto do tabuleito para baixo)
    for k in range(n):  # Determinando a lista de letras e a lista que conterá a peça
        linha_letras.append(chr(97 + k))
        if k == ord(coluna) - 97:
            linha_peca.append("o")
        else:
            linha_peca.append("-")

    for g in range(n):
        if g > n - int(linha):  # Criando as listas das linhas atacadas, de cima pra baixo, e colocando-as em ordem
            # (inclusive a linha que contem a peça) na lista de linhas
            lista_linha = []
            for x in range(n):
                if x == ord(coluna) - 97 - n + int(linha) + g:
                    lista_linha.append("x")
                elif x == ord(coluna) - 97 + n - int(linha) - g:
                    lista_linha.append("x")
                else:
                    lista_linha.append("-")
            lista_linhas.append(lista_linha)

        if g == n - int(linha):
            lista_linhas.append(linha_peca)

        if g < n - int(linha):
            lista_linha = []
            for i in range(n):
                if i == ord(coluna) - 97 - (n - int(linha) - g) or i == ord(coluna) - 97 + (n - int(linha) - g):
                    lista_linha.append("x")
                else:
                    lista_linha.append("-")
            lista_linhas.append(lista_linha)

    for k in range(n):
        print(n - k, *lista_linhas[k])
    print(" ", *linha_letras)


def rainha(n, coluna, linha):
    """Função que determinará a impressão do tabuleiro do rainha"""
    linha_letras = []
    linha_peca = []
    lista_linhas = []  # Lista que abrigará todas as linhas, em ordem decrescente (alto do tabuleito para baixo)
    for k in range(n):  # Determinando a lista de letras e a lista que conterá a peça
        linha_letras.append(chr(97 + k))
        if k == ord(coluna) - 97:
            linha_peca.append("o")
        else:
            linha_peca.append("x")

    for g in range(n):
        if g > n - int(linha):  # Criando as listas das linhas atacadas, de cima pra baixo, e colocando-as em ordem
            # (inclusive a linha que contem a peça) na lista de linhas
            lista_linha = []
            for x in range(n):
                if x == ord(coluna) - 97 - n + int(linha) + g:
                    lista_linha.append("x")
                elif x == ord(coluna) - 97 + n - int(linha) - g:
                    lista_linha.append("x")
                elif x == ord(coluna) - 97:
                    lista_linha.append("x")
                else:
                    lista_linha.append("-")
            lista_linhas.append(lista_linha)

        if g == n - int(linha):
            lista_linhas.append(linha_peca)

        if g < n - int(linha):
            lista_linha = []
            for i in range(n):
                if i == ord(coluna) - 97 - (n - int(linha) - g) or i == ord(coluna) - 97 + (n - int(linha) - g):
                    lista_linha.append("x")
                elif i == ord(coluna) - 97:
                    lista_linha.append("x")
                else:
                    lista_linha.append("-")
            lista_linhas.append(lista_linha)

    for k in range(n):  # Imprimindo todas as linhas, já em ordem, na lista de linhas
        print(n - k, *lista_linhas[k])
    print(" ", *linha_letras)


casas = input()
lista_tabuleiros = []
while casas != "0":
    peca = input()
    lista_auxiliar = list()
    lista_auxiliar.append(casas)
    lista_auxiliar.append(peca.split(" "))
    lista_tabuleiros.append(lista_auxiliar)
    casas = input()

for h in range(len(lista_tabuleiros)):
    if lista_tabuleiros[h][1][0] == "Torre":
        print(f"Movimentos para a peca Torre a partir da casa {lista_tabuleiros[h][1][1]}{lista_tabuleiros[h][1][2]}.")
        torre(int(lista_tabuleiros[h][0]), lista_tabuleiros[h][1][1], lista_tabuleiros[h][1][2])
        print()
    elif lista_tabuleiros[h][1][0] == "Cavalo":
        print(f"Movimentos para a peca Cavalo a partir da casa {lista_tabuleiros[h][1][1]}{lista_tabuleiros[h][1][2]}.")
        cavalo(int(lista_tabuleiros[h][0]), lista_tabuleiros[h][1][1], lista_tabuleiros[h][1][2])
        print()
    elif lista_tabuleiros[h][1][0] == "Bispo":
        print(f"Movimentos para a peca Bispo a partir da casa {lista_tabuleiros[h][1][1]}{lista_tabuleiros[h][1][2]}.")
        bispo(int(lista_tabuleiros[h][0]), lista_tabuleiros[h][1][1], lista_tabuleiros[h][1][2])
        print()
    elif lista_tabuleiros[h][1][0] == "Peao":
        print(f"Movimentos para a peca Peao a partir da casa {lista_tabuleiros[h][1][1]}{lista_tabuleiros[h][1][2]}.")
        peao(int(lista_tabuleiros[h][0]), lista_tabuleiros[h][1][1], lista_tabuleiros[h][1][2])
        print()
    elif lista_tabuleiros[h][1][0] == "Dama":
        print(f"Movimentos para a peca Dama a partir da casa {lista_tabuleiros[h][1][1]}{lista_tabuleiros[h][1][2]}.")
        rainha(int(lista_tabuleiros[h][0]), lista_tabuleiros[h][1][1], lista_tabuleiros[h][1][2])
        print()
    elif lista_tabuleiros[h][1][0] == "Rei":
        print(f"Movimentos para a peca Rei a partir da casa {lista_tabuleiros[h][1][1]}{lista_tabuleiros[h][1][2]}.")
        rei(int(lista_tabuleiros[h][0]), lista_tabuleiros[h][1][1], lista_tabuleiros[h][1][2])
        print()



def par(n):
    if n % 2 == 0 and n != 0:
        return True
    else:
        return False


def atribuicao(string):
    elementos = string.split(" ")
    try:
        int(elementos[0][0])
        print(f"Erro de sintaxe: {elementos[0]} nao e um nome permitido para uma variavel.")
        return
    except ValueError:
        soma = 0
        for k in range(len(elementos)):
            if par(k):
                if elementos[k - 1] == "+" or k == 2:
                    soma += int(elementos[k])
                elif elementos[k - 1] == "-":
                    soma -= int(elementos[k])

