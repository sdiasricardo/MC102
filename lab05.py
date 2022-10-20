# definindo as funções para utilizar nos comandos 'sorted'
def minusculas(x):
    mi = 0
    for i in range(len(x)):
        if x[i].islower() is True:
            mi += 1
    return mi


def maiusculas(x):
    ma = 0
    for i in range(len(x)):
        if x[i].isupper() is True:
            ma = ma + 1
    return ma


def alfabeto(x):
    alf = 0
    for i in range(len(x)):
        if x[i].isalpha() is True:
            alf += 1
    return alf


def palavras(x):
    string_separada = x.split(" ")
    return len(string_separada)


def caracteres(x):
    soma = 0
    for i in range(len(x)):
        soma = soma + ord(x[i])
    return soma


def padrao_impressao(x):
    for i in range(len(x)):
        print(x[i])


# definindo as entradas
entrada1 = input().split(" ")
enderecos = []
for k in range(int(entrada1[1])):
    enderecos.append(input())

# organizando as saídas de acordo com os dias da semana
if entrada1[0] == "Segunda":
    seg_formatada = sorted(enderecos, key=minusculas)
    padrao_impressao(seg_formatada)
elif entrada1[0] == "Terca":
    ter_formatada = sorted(enderecos, key=maiusculas, reverse=True)
    padrao_impressao(ter_formatada)
elif entrada1[0] == "Quarta":
    qua_formatada = sorted(enderecos, key=alfabeto)
    padrao_impressao(qua_formatada)
elif entrada1[0] == "Quinta":
    qui_formatada = sorted(enderecos, key=palavras)
    padrao_impressao(qui_formatada)
elif entrada1[0] == "Sexta":
    sex_formatada = sorted(enderecos, key=caracteres, reverse=True)
    padrao_impressao(sex_formatada)
