def par(n):
    """Função booleana que verifica se um numero é par (retorna True) ou ímpar (retorna False)"""
    if n % 2 == 0:
        return True
    else:
        return False


def operacao(lista, range_inicio, range_parada, dicionario, indice_pulado):
    """Função que realiza a operação fornecida pelo range_inicio/range_final, que se encontra dentro da lista. Também
     verifica se o elemento a ser somado ou subtraido é uma variável ou um valor. Caso seja uma variável, verifica se a
     mesma se encontra no dicionario de variáveis, e caso não esteja, exibe uma mensagem de erro. Caso seja um comando
     de atribuicao, indice_pulado = 0, para que o indíce 0, que seria relativo ao nome da variável e seria indicado
     como par, seja pulado. Do contrario, atribuicao = None, para que no comando que não seja o de atribuição, o
     primeiro elemento (indice 0) não seja pulado. Retorna o resultado da expressão desejada."""
    resultado = 0
    for k in range(range_inicio, range_parada):
        if par(k) and k != indice_pulado:
            try:  # Verificando se determinado objeto da lista é uma variável ou um valor
                int(lista[k])
                if lista[k - 1] == "+" or k == range_inicio:
                    resultado += int(lista[k])
                elif lista[k - 1] == "-":
                    resultado -= int(lista[k])
            except ValueError:
                if lista[k] in dicionario.keys():  # Verificando se aquela variável já está atribuida no
                    # dicionário de variáveis
                    if lista[k - 1] == "+" or k == range_inicio:
                        resultado += int(dicionario[lista[k]])
                    elif lista[k - 1] == "-":
                        resultado -= int(dicionario[lista[k]])
                else:
                    print(f"Erro de referencia: a variavel {lista[k]} nao foi definida.")
                    return
    return resultado


def atribuicao(elementos, dicionario):
    try:
        int(elementos[0][0])
        print(f"Erro de sintaxe: {elementos[0]} nao e um nome permitido para uma variavel.")
        return
    except ValueError:
        soma = 0
        a = ["var", "=", "1", ">", "2", "AND", "1", "<", "5"]
        exp = [0, "AND", 1, "OR", 1]
        if "==" in elementos or ">" in elementos or "<" in elementos or ">=" in elementos or "<=" in elementos or "!=" \
                in elementos:  # Verificando sé um comando de atribuicao booleana
            if "AND" in elementos or "OR" in elementos:  # Verificando se é uma booleana composta
                expressoes = []
                expressao = []
                for k in range(len(elementos)):
                    if k == len(elementos) - 1:
                        expressao.append(elementos[k])
                        expressoes.append(expressao)
                    elif k != 0 and k != 1 and elementos[k] != "AND" and elementos[k] != "OR":
                        expressao.append(elementos[k])
                    elif elementos[k] == "AND" or elementos[k] == "OR":
                        expressoes.append(expressao)
                        expressoes.append(elementos[k])
                        expressao = []
                for k in range(len(expressoes)):
                    if expressoes[k] != "AND" and expressoes[k] != "OR":
                        if "==" in expressoes[k]:
                            soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("=="), dicionario, None)
                            soma_direita = operacao(expressoes[k], expressoes[k].index("==") + 1, len(expressoes[k]),
                                                    dicionario, None)
                            if soma_esquerda is None or soma_direita is None:
                                return
                            elif soma_esquerda == soma_direita:
                                expressoes[k] = 1
                            else:
                                expressoes[k] = 0
                        elif ">" in expressoes[k]:
                            soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index(">"), dicionario, None)
                            soma_direita = operacao(expressoes[k], expressoes[k].index(">") + 1, len(expressoes[k]),
                                                    dicionario, None)
                            if soma_esquerda is None or soma_direita is None:
                                return
                            elif soma_esquerda > soma_direita:
                                expressoes[k] = 1
                            else:
                                expressoes[k] = 0
                        elif "<" in expressoes[k]:
                            soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("<"), dicionario, None)
                            soma_direita = operacao(expressoes[k], expressoes[k].index("<") + 1, len(expressoes[k]),
                                                    dicionario, None)
                            if soma_esquerda is None or soma_direita is None:
                                return
                            elif soma_esquerda < soma_direita:
                                expressoes[k] = 1
                            else:
                                expressoes[k] = 0
                        elif ">=" in expressoes[k]:
                            soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index(">="), dicionario, None)
                            soma_direita = operacao(expressoes[k], expressoes[k].index(">=") + 1, len(expressoes[k]),
                                                    dicionario, None)
                            if soma_esquerda is None or soma_direita is None:
                                return
                            elif soma_esquerda >= soma_direita:
                                expressoes[k] = 1
                            else:
                                expressoes[k] = 0
                        elif "<=" in expressoes[k]:
                            soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("<="), dicionario, None)
                            soma_direita = operacao(expressoes[k], expressoes[k].index("<=") + 1, len(expressoes[k]),
                                                    dicionario, None)
                            if soma_esquerda is None or soma_direita is None:
                                return
                            elif soma_esquerda <= soma_direita:
                                expressoes[k] = 1
                            else:
                                expressoes[k] = 0
                        elif "!=" in expressoes[k]:
                            soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("!="), dicionario, None)
                            soma_direita = operacao(expressoes[k], expressoes[k].index("!=") + 1, len(expressoes[k]),
                                                    dicionario, None)
                            if soma_esquerda is None or soma_direita is None:
                                return
                            elif soma_esquerda != soma_direita:
                                expressoes[k] = 1
                            else:
                                expressoes[k] = 0

                if expressoes.count(1) >= expressoes.count("AND") + 1:
                    soma = 1

            else:  # Caso de booleana simples
                if "==" in elementos:
                    soma_esquerda = operacao(elementos, 2, elementos.index("=="), dicionario, 0)
                    soma_direita = operacao(elementos, elementos.index("==") + 1, len(elementos), dicionario, 0)
                    soma += 1 if soma_esquerda == soma_direita else 0
                elif ">" in elementos:
                    soma_esquerda = operacao(elementos, 2, elementos.index(">"), dicionario, 0)
                    soma_direita = operacao(elementos, elementos.index(">") + 1, len(elementos), dicionario, 0)
                    soma += 1 if soma_esquerda > soma_direita else 0
                elif "<" in elementos:
                    soma_esquerda = operacao(elementos, 2, elementos.index("<"), dicionario, 0)
                    soma_direita = operacao(elementos, elementos.index("<") + 1, len(elementos), dicionario, 0)
                    soma += 1 if soma_esquerda < soma_direita else 0
                elif ">=" in elementos:
                    soma_esquerda = operacao(elementos, 2, elementos.index(">="), dicionario, 0)
                    soma_direita = operacao(elementos, elementos.index(">=") + 1, len(elementos), dicionario, 0)
                    soma += 1 if soma_esquerda >= soma_direita else 0
                elif "<=" in elementos:
                    soma_esquerda = operacao(elementos, 2, elementos.index("<="), dicionario, 0)
                    soma_direita = operacao(elementos, elementos.index("<=") + 1, len(elementos), dicionario, 0)
                    soma += 1 if soma_esquerda <= soma_direita else 0
                elif "!=" in elementos:
                    soma_esquerda = operacao(elementos, 2, elementos.index("!="), dicionario, 0)
                    soma_direita = operacao(elementos, elementos.index("!=") + 1, len(elementos), dicionario, 0)
                    soma += 1 if soma_esquerda != soma_direita else 0

        else:  # Caso para que é uma expressão aritmética
            soma = operacao(elementos, 2, len(elementos), dicionario, 0)
    try:
        dicionario[elementos[0]] = int(soma)
        return dicionario
    except TypeError:
        return


def sem_atribuicao(elementos, dicionario):
    soma = 0
    if "==" in elementos or ">" in elementos or "<" in elementos or ">=" in elementos or "<=" in elementos or "!=" \
            in elementos:  # Verificando sé um comando de atribuicao booleana
        if "AND" in elementos or "OR" in elementos:  # Verificando se é uma booleana composta
            expressoes = []  # Lista que abrigará cada uma das expressoes boleanas em forma de lista para a utilizacao
            # na função operaçào. Cada uma das expressoes é separadas por AND ou OR
            expressao = []  # Lista auxiliar que irá abrigar cada uma das expressões, para que sejam abrigadas na lista
            # "expressões"
            for k in range(len(elementos)):  # Iterando sobre a lista de todos os elementos da entrada para gerar uma
                # lista com uma expressão individual, que será abrigada na lista de expressões junto ao AND ou OR
                if k == len(elementos) - 1:
                    expressao.append(elementos[k])
                    expressoes.append(expressao)
                elif elementos[k] != "AND" and elementos[k] != "OR":
                    expressao.append(elementos[k])
                elif elementos[k] == "AND" or elementos[k] == "OR":
                    expressoes.append(expressao)
                    expressoes.append(elementos[k])
                    expressao = []
            for k in range(len(expressoes)):  # Iterando sobre a lista de expressões e realizando cada uma das operações
                # que, caso seja verdadeira, substitui a sua posição k na lista de expressoes por 1, e caso seja falsa,
                # substitui sua posição k na lista de expressoes por 0
                if expressoes[k] != "AND" and expressoes[k] != "OR":
                    if "==" in expressoes[k]:
                        soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("=="), dicionario, None)
                        soma_direita = operacao(expressoes[k], expressoes[k].index("==") + 1, len(expressoes[k]),
                                                dicionario, None)
                        if soma_esquerda is None or soma_direita is None:
                            return
                        elif soma_esquerda == soma_direita:
                            expressoes[k] = 1
                        else:
                            expressoes[k] = 0
                    elif ">" in expressoes[k]:
                        soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index(">"), dicionario, None)
                        soma_direita = operacao(expressoes[k], expressoes[k].index(">") + 1, len(expressoes[k]),
                                                dicionario, None)
                        if soma_esquerda is None or soma_direita is None:
                            return
                        elif soma_esquerda > soma_direita:
                            expressoes[k] = 1
                        else:
                            expressoes[k] = 0
                    elif "<" in expressoes[k]:
                        soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("<"), dicionario, None)
                        soma_direita = operacao(expressoes[k], expressoes[k].index("<") + 1, len(expressoes[k]),
                                                dicionario, None)
                        if soma_esquerda is None or soma_direita is None:
                            return
                        elif soma_esquerda < soma_direita:
                            expressoes[k] = 1
                        else:
                            expressoes[k] = 0
                    elif ">=" in expressoes[k]:
                        soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index(">="), dicionario, None)
                        soma_direita = operacao(expressoes[k], expressoes[k].index(">=") + 1, len(expressoes[k]),
                                                dicionario, None)
                        if soma_esquerda is None or soma_direita is None:
                            return
                        elif soma_esquerda >= soma_direita:
                            expressoes[k] = 1
                        else:
                            expressoes[k] = 0
                    elif "<=" in expressoes[k]:
                        soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("<="), dicionario, None)
                        soma_direita = operacao(expressoes[k], expressoes[k].index("<=") + 1, len(expressoes[k]),
                                                dicionario, None)
                        if soma_esquerda is None or soma_direita is None:
                            return
                        elif soma_esquerda <= soma_direita:
                            expressoes[k] = 1
                        else:
                            expressoes[k] = 0
                    elif "!=" in expressoes[k]:
                        soma_esquerda = operacao(expressoes[k], 0, expressoes[k].index("!="), dicionario, None)
                        soma_direita = operacao(expressoes[k], expressoes[k].index("!=") + 1, len(expressoes[k]),
                                                dicionario, None)
                        if soma_esquerda is None or soma_direita is None:
                            return
                        elif soma_esquerda != soma_direita:
                            expressoes[k] = 1
                        else:
                            expressoes[k] = 0

            if expressoes.count(1) >= expressoes.count("AND") + 1:  # Para que a booleana composta seja verdadeira, o
                # número de expressões verdadeiras deve ser igual ao número de operadores "AND"+ 1
                soma = 1
        else:  # Caso de booleana simples
            if "==" in elementos:
                soma_esquerda = operacao(elementos, 0, elementos.index("=="), dicionario, None)
                soma_direita = operacao(elementos, elementos.index("==") + 1, len(elementos), dicionario, None)
                soma += 1 if soma_esquerda == soma_direita else 0
            elif ">" in elementos:
                soma_esquerda = operacao(elementos, 0, elementos.index(">"), dicionario, None)
                soma_direita = operacao(elementos, elementos.index(">") + 1, len(elementos), dicionario, None)
                soma += 1 if soma_esquerda > soma_direita else 0
            elif "<" in elementos:
                soma_esquerda = operacao(elementos, 0, elementos.index("<"), dicionario, None)
                soma_direita = operacao(elementos, elementos.index("<") + 1, len(elementos), dicionario, None)
                soma += 1 if soma_esquerda < soma_direita else 0
            elif ">=" in elementos:
                soma_esquerda = operacao(elementos, 0, elementos.index(">="), dicionario, None)
                soma_direita = operacao(elementos, elementos.index(">=") + 1, len(elementos), dicionario, None)
                soma += 1 if soma_esquerda >= soma_direita else 0
            elif "<=" in elementos:
                soma_esquerda = operacao(elementos, 0, elementos.index("<="), dicionario, None)
                soma_direita = operacao(elementos, elementos.index("<=") + 1, len(elementos), dicionario, None)
                soma += 1 if soma_esquerda <= soma_direita else 0
            elif "!=" in elementos:
                soma_esquerda = operacao(elementos, 0, elementos.index("!="), dicionario, None)
                soma_direita = operacao(elementos, elementos.index("!=") + 1, len(elementos), dicionario, None)
                soma += 1 if soma_esquerda != soma_direita else 0

    else:  # Caso para que é uma expressão aritmética
        soma = operacao(elementos, 0, len(elementos), dicionario, None)
    try:
        print(int(soma))
    except TypeError:
        return


dicionario_de_variaveis = {}
entradas = []

"""
while True:
    try:
        entrada = input()
        entradas.append(entrada.split(" "))
    except EOFError:
        break

for entrada in entradas:
    if "=" in entrada:
        atribuicao(entrada, dicionario_de_variaveis)
    else:
        sem_atribuicao(entrada, dicionario_de_variaveis)
"""

a = input()
while a != "":
    entradas.append(a.split(" "))
    a = input()
for entrada in entradas:
    if "=" in entrada:
        atribuicao(entrada, dicionario_de_variaveis)
    else:
        sem_atribuicao(entrada, dicionario_de_variaveis)


print("Encerrando... Bye-bye.")
