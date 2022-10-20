def teraf_lare(m, n, lista):
    """Função recursiva que, dada uma área m x n, retorna uma lista com as quantidades de submagias e seus níveis.
    A lista será do tipo [[x1, y1], [x2, y2] . . .[xp, yp]], onde xp e yp representam, respectivamente,
    a quantidade de áreas de lado 2^(yp)."""
    if m == 1: # Caso uma das dimensões seja 1, tem-se apenas a quantidade da outra dimensão de submagias
        # nivel 0
        submagia = []
        submagia.append(n)
        submagia.append(0)
        lista.append(submagia)
        return lista
    elif n == 1:
        submagia = []
        submagia.append(m)
        submagia.append(0)
        lista.append(submagia)
        return lista
    else: # Do contrário, tem -se:
        if m == 0 or n == 0: # Caso uma das dimensões seja igual a 0, não existe mais tabuleiro, portanto
            # não se podem conjurar mais submagias
            return lista
        elif m > n: # Caso n seja menor, ele terá o máximo lado possível
            for j in range(n):
                for k in range(n//2, 0, -1): # Verificando qual o máximo valor menor do que n que corresponde
                    # a uma potência de 2
                    if n - j == 2**(k):
                        if j == 0: # Caso o próprio lado seja uma potência de 2, o tabuleiro pode ser dividido
                            # em duas partes, sendo uma delas de dimensão n x n, e a outra m - n x n. Para 
                            # o cálculo das submagias da segunda, basta chamar a função novamente
                            submagia = [1]
                            submagia.append(k)
                            lista.append(submagia)
                            return teraf_lare(m - n, n, lista)
                        else: # Do contrário, o tabuleiro pode ser divido em 3 subregiões. A primeira, de dimensão
                            # n - j x n - j, ja representa a primeira e maior submagia que poderá ser calculada.
                            # Para o cálculo das submagias das outras duas regiões, basta chamar a função novamente,
                            # com os parâmetros que restam da área do tabuleiro inicial subtraída da área da maior 
                            # submagia (ou o primeiro tabuleiro)
                            submagia = [1]
                            submagia.append(k)
                            lista.append(submagia)
                            return teraf_lare(m - 2**(k), n, lista), teraf_lare(2**(k), j, lista)
        elif m < n or m == n: # Quando m < n ou m == 0, a lógica é exatamente a mesma da utilizada em n, porém 
            # relativas a dimensão m
            for j in range(m):
                for k in range(m//2, 0, -1):
                    if m  - j == 2**(k):
                        if j == 0:
                            submagia = [1]
                            submagia.append(k)
                            lista.append(submagia)
                            return teraf_lare(m, n - m, lista)
                        else:
                            submagia = [1]
                            submagia.append(k)
                            lista.append(submagia)
                            return teraf_lare(m, n - 2**(k), lista), teraf_lare(2**(k), j, lista)


def BubbleSort_submagias(a):
    """Função que organiza a lista de submagias conforme o índice que determina o seu lado."""
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1][1] > a[j][1]:
                a[j - 1], a[j] = a[j], a[j - 1]


m, n = map(int, input().split(" "))
submagias = []

teraf_lare(m, n, submagias)
BubbleSort_submagias(submagias)

# Somando os valores de submagias repetidas, para gerar a quantidade total de conjurações de cada submagia
k = 0
j = len(submagias)
while k <= j - 2:
    soma = submagias[k][0]
    x = k
    i = x + 1
    while submagias[x][1] == submagias[x + 1][1]: # Comparando cada elemento com o próximo da lista. Caso tenham
        # o valor yp iguais, é adicionado o valor de conjurações à variável soma, que depois sera o único
        # valor na lista de submagias.
        soma += submagias[x + 1][0]
        submagias.pop(x + 1) # Após a comparação, os item de índice [x + 1] é removido, de forma que o próximo
        # elemento se torna o elemento de índice [ i + 1], para que seja comparado
        j = len(submagias)
        if x + 1 == j: # Caso o índice [x + 1] seja igual ao comprimento da lista, o loop é quebrado pois a 
            # comparação chegou ao fim (e para evitar IndexError)
            break
    submagias[k][0] = soma # Ao fim, o valor total de conjurações submagia de nível yp é atualizado
    k += 1 # k aumenta em 1 unidade, para a comparação com o próximo elemento da lista

total_submagias = 0
pm = 0
for submagia in submagias: # Contabilizacão da quantidade total de submagias de todos os níveis e do PM.
    total_submagias += submagia[0]
    pm += submagia[0] * 2 **(submagia[1])
    
print("---")
print("Grimorio de Teraf L'are")
print("---")
for submagia in submagias:
    print(f"{submagia[0]} submagia(s) de nivel {submagia[1]}")
print("---")
print(f"Total de submagia(s) conjurada(s): {total_submagias}")
print(f"Total de PM gasto: {pm}")
print("---")

