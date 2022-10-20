viloes = dict() # Dicionario que conterá, como chave, o nome de cada suspeito, e como valor, as características dele

nome = input().split(": ") # A primeira entrada será sempre o nome do primeiro suspeito
while nome[0] != "--": # Quando recebe como entrada "--", significa o fim das entradas de viloes e caracteristicas
    viloes[nome[1]] = dict() # Criando a chave relativa à entrada do nome do vilão no dicionario de viloes
    entrada = input().split(": ") # Entrada da característica
    while entrada[0] != "-" and entrada[0] != "--": # Caso a entrada seja "-", deve-se iniciar um novo vilão
        viloes[nome[1]][entrada[0]] = entrada[1] # Associando a caracteristica ao dicionario de cada vilão
        entrada = input().split(": ")
    if entrada[0] != "--": # Caso a entrada seja diferente de "--", é necessária mais uma entrada, para 
        # recomeçar o loop da linha 4
        nome = input().split(": ")
    else: # Do contrario, é necessário que nome[0] == "--" para que o loop seja quebrado
        nome = entrada


evidencias = dict()

evidencia = input().split(": ")
while evidencia[0] != "---": # Enquanto a entrada relativa a evidencia não for "---", tem-se uma nova evidencia por vir
    evidencias[evidencia[0]] = evidencia[1] # Adicionando a atual evidencia a um dicionario de evidencias
    evidencia = input().split(": ")

suspeitos = set(viloes.keys()) # O conjunto(pois não pode haver repetição) de suspeitos se inicia 
# com todos os vilões, pois nenhuma característica das evidencias foi avaliada ainda.

for chave, valor in evidencias.items():
    suspeitos_atuais = set()  # Lista que abrigará os suspeitos que contem a característica em atual avaliação. 
    # (dentre os que ja possuem as características avalidas anteriormente) 
    for i in suspeitos:
        try:
            if viloes[i][chave] == valor:
                suspeitos_atuais.add(i)
        except KeyError:
            pass
    suspeitos = suspeitos_atuais # Por fim, a lista de suspeitos é atualizada com os suspeitos que, além
    # de terem as características anteriormente avaliadas, possuem a característica que acaba de ser avaliada.

suspeitos = sorted(suspeitos) # Colocando a lista de suspeitos em ordem alfabetica
if len(suspeitos) == 1: # Caso de impressão para apenas 1 suspeito
    print("Suspeito(a):")
    print(*suspeitos, sep="\n")
elif len(suspeitos) == 0: # Caso de impressão para nenhum suspeito
    print("Nenhum suspeito(a) com essas caracteristicas foi identificado(a).")
else: # Caso de impressão para mais de 1 suspeito
    print("Suspeitos(as):")
    print(*suspeitos, sep="\n")