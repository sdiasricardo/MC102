def semelhanca(x, y):
    s = 0
    for z in range(len(x)):
        if x[z] == y[z]:
            s += 1
    return s


def padrao1(tentativa, mestra, k, tentativas):
    print("Senha incorreta")
    print("Semelhanca:", semelhanca(tentativa, mestra))
    print("Tentativas restantes:", int(tentativas) - 1 - k)
    print()


def padrao2(tentativas, k):
    print("Senha incorreta")
    print("Semelhanca: Erro: quantidade de digitos incongruente")
    print("Tentativas restantes:", (int(tentativas) - 1 - k))
    print()

def padrao3():
    print("Tentativas esgotadas. Acionando defesas...")


def testes(mestra, tentativas):
    k = 0
    while k < int(tentativas):
        tentativa = input()
        if tentativa == mestra:
            print("Senha reconhecida. Desativando defesas...")
            k = k + int(tentativas) + 1
        elif len(tentativa) > len(mestra) or len(tentativa) < len(mestra):
            if(int(tentativas) - 1 - k) == 0:
                padrao2(tentativas, k)
                padrao3()
            else:
                padrao2(tentativas, k)
            k += 1
        else:
            # criando condicionais para casos de esgotamento de tentativas e casos com tentivas restantes
            if (int(tentativas) - 1 - k) == 0:
                padrao1(tentativa, mestra, k, tentativas)
                padrao3()
                k += 1
            else:
                padrao1(tentativa, mestra, k, tentativas)
                k += 1


def main():
    entrada = input().split(" ")
    testes(entrada[0], entrada[1])


main()
