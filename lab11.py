def distancia(x1, y1, x2, y2):
    """Função que calcula a distância euclidiana entre 2 pontos no plano cartesiano"""
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


def ponto_distancia_max(lista_x, lista_y, limite):
    """Função que calcula e imprime a ordenada do ponto (0, Y) que fornecem a distancia minimizada
    do esconderijo mais distante"""
    # Não é necessário que todas as distâncias sejam calculadas. Como Y progride linearmente até o limite,
    # as funções das maiores distancias progridem conforme uma parábola de concavidade positiva, ou seja,
    # existe um ponto de mínimo tal que a maior distancia do ponto anterior (determinada na funçao por dis_ant_m)
    # e a maior distância do próximo ponto (determinada na função por dist_prox_m) são maiores do que o ponto
    # analisado (determinado por dist_m). Para isso, basta fazer uma busca binária
    n = limite 
    e = 0
    d = n - 1
    while e <= d:
        m = (e + d)//2
        dis_ant_m = 0
        dis_m = 0
        dis_prox_m = 0
        for j in range(len(lista_x)):
            dis_atual = distancia(lista_x[j], lista_y[j], 0, m)
            if dis_atual > dis_m:
                dis_m = dis_atual
            dis_atual_ant_m = distancia(lista_x[j], lista_y[j], 0, m - 1)
            if dis_atual_ant_m > dis_ant_m:
                dis_ant_m = dis_atual_ant_m
            dis_atual_prox_m = distancia(lista_x[j], lista_y[j], 0, m + 1)
            if dis_atual_prox_m > dis_prox_m:
                dis_prox_m = dis_atual_prox_m
        if dis_ant_m > dis_m < dis_prox_m:
            print(m)
            return
        elif dis_ant_m > dis_m > dis_prox_m: # Caso decresçam, o ponto está mais a esquerda
            e = m + 1
        elif dis_ant_m < dis_m < dis_prox_m: # Caso cresça, o ponto está mais a direita
            d = m - 1





n, y0 = map(int, input().split(" "))

while n != 0 and y0 != 0:
    esconderijos_x = []
    esconderijos_y = []
    for k in range(n):
        x, y = map(int, input().split(" "))
        if y in esconderijos_y: # Elimininado de antemão os casos de ordenadas iguais
            indice = esconderijos_y.index(y)
            if abs(x) > abs(esconderijos_x[indice]):
                esconderijos_x[indice] = x
        else:
            esconderijos_x.append(x)
            esconderijos_y.append(y)
    ponto_distancia_max(esconderijos_x, esconderijos_y, y0)
    n, y0 = map(int, input().split(" "))

