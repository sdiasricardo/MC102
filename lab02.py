# definindo as variaváveis e os valores de entrada iniciais
canal = input()
n = int(input())
# definindo as listas que vão abrigar os dados
lista_views_2018 = []
lista_views_2019 = []
lista_views_2020 = []
lista_views_total = []
# atribuindo os valores de entrada às respectivas listas
for i in range(n):
    data = input()
    separacao = list(map(int, data.split("-")))
    views = int(input())
    if separacao[0] == 2018:
        lista_views_2018.append(views)
        lista_views_total.append(views)
    elif separacao[0] == 2019:
        lista_views_2019.append(views)
        lista_views_total.append(views)
    elif separacao[0] == 2020:
        lista_views_2020.append(views)
        lista_views_total.append(views)
# definindo variave auxiliares
n_significativo = len(lista_views_2020) + len(lista_views_2019) + len(lista_views_2018)
# iniciando a saida de dados
print("Canal: %s" % canal)
print("Total de views do trienio: %d" % sum(lista_views_total))
print("Media de views do trienio: %s" % format(sum(lista_views_total)/n_significativo, '.2f'))
k = 2018
# separando os casos de views total = 0
if sum(lista_views_total) == 0:
    while k <= 2020:
        print("\n%d" % k)
        print("Total: 0")
        print("Porcentagem das views do trienio: indeterminada")
        print("Media: 0.00")
        k += 1
else:
    print()
    print(2018)
    print("Total: %d" % sum(lista_views_2018))
    print("Porcentagem das views do trienio: %s" % format((sum(lista_views_2018)/sum(lista_views_total))*100, ".2f"))
    print("Media: % s" % format(sum(lista_views_2018)/len(lista_views_2018), ".2f"))
    print()
    print(2019)
    print("Total: %d" % sum(lista_views_2019))
    print("Porcentagem das views do trienio: %s" % format((sum(lista_views_2019)/sum(lista_views_total))*100, ".2f"))
    print("Media: % s" % format(sum(lista_views_2019)/len(lista_views_2019), ".2f"))
    print()
    print(2020)
    print("Total: %d" % sum(lista_views_2020))
    print("Porcentagem das views do trienio: %s" % format((sum(lista_views_2020)/sum(lista_views_total))*100, ".2f"))
    print("Media: % s" % format(sum(lista_views_2020)/len(lista_views_2020), ".2f"))
