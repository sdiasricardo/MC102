def impar(n):
    """Define se um número é impar ou não"""
    if n % 2 != 0:
        return True
    else:
        return False


def decodificar(E, L):
    """Responsável por decodificar e imprimir as mensagens, seguindo as regras de linhas pares e ímpares."""
    mensagens = [] # Lista que abrigará as mensagens decodificadas
    for k in range(L):
        if impar(k+1) is True: # Início do procedimento para as linhas ímpares
            mensagem_codificada = input()
            caracteres = []
            for i in range(0, len(mensagem_codificada), E):
                caracteres.append(chr(int(mensagem_codificada[i:i+E], 16)))
            mensagem_decodificada = "".join(caracteres)
            mensagens.append(mensagem_decodificada) # Adiciona a mensagem já decodificada na lista de mensagens

        elif impar(k+1) is False: # Início do procedimento para as linhas pares
            mensagem_codificada = input()
            caracteres = []
            for i in range(0, len(mensagem_codificada), E):
                caracteres.append(chr(int(mensagem_codificada[i:i+E], 8)))
            mensagem_invertida = "".join(caracteres)
            mensagem_decodificada = mensagem_invertida[::-1] # Inverte a ordem dos caracteres da mensagem
            mensagens.append(mensagem_decodificada)
    print(*mensagens, sep="\n")


def codificar(E, L):
    """Responsável por codificar e imprimir as mensagens, seguindo as regras de linhas pares e ímpares"""
    mensagens = []
    for k in range(L):
        if impar(k+1) is True:
            mensagem_nao_codificada = input()
            caracteres = []
            for i in range(len(mensagem_nao_codificada)):
                caracter_codificado = hex(ord(mensagem_nao_codificada[i])) # Transforma cada caracter relativo em ASCII
                                                                           # da mensagem inicial em seu correspondente
                                                                           # em hexadecimal
                caracter_corrigido = caracter_codificado[2:] # Exclui os 0x do numero exadecimal
                if len(caracter_corrigido) < E: # Adiciona, caso necessario, o número de 0 que faltam para que haja um
                                                # número de casas igual a E
                    caracteres.append(caracter_corrigido.zfill(E))
                else:
                    caracteres.append(caracter_corrigido)
            mensagem_codificada = "".join(caracteres)
            mensagens.append(mensagem_codificada.upper())

        elif impar(k+1) is False:
            mensagem_nao_codificada = input()
            caracteres = []
            for i in range(len(mensagem_nao_codificada)):
                caracter_codificado = oct(ord(mensagem_nao_codificada[i]))
                caracter_corrigido = caracter_codificado[2:]
                if len(caracter_corrigido) < E:
                    caracteres.append(caracter_corrigido.zfill(E))
                else:
                    caracteres.append(caracter_corrigido)
            mensagem_codificada = "".join(reversed(caracteres)) #Inverte a ordem dos caracteres invertidos
            mensagens.append(mensagem_codificada.upper())
    print(*mensagens, sep="\n")



# Inicio da execução do código, com duas condicionais que vão direcionar ela
# O input inicial se refere às entradas que dão as informações de codificação
# ou decodificação, algarismos nas leituras octais e hexadecimais, e quantidade
# de linhas/codigos que serão fornecidas
input_inicial = input()
if input_inicial[0] == "1":
    codificar(int(input_inicial[2]), int(input_inicial[4:]))
elif input_inicial[0] == "2":
    decodificar(int(input_inicial[2]), int(input_inicial[4:]))
