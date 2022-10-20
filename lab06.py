class Medabot:
    '''Define os atributos do medabot de cada medalutador. Observações importantes: 1 - Todos os "@property" criados
    foram lidos ao longo do programa; 2 - O atributo "adquirido", inicialmente vazio, foi criado para facilitar o acesso
    à medapeça adquirda após a vitória de um medabot.'''
    def __init__(self, atq, dfs, torso, pernas, bracoE, bracoD, bonusATQ, bonusDFS, adquirido):
        self._atq = atq
        self._dfs = dfs
        self._bracoE = bracoE
        self._bracoD = bracoD
        self._bonusATQ = bonusATQ
        self._bonusDFS = bonusDFS
        self._torso = torso
        self._pernas = pernas
        self._adquirido = adquirido

    @property
    def atq(self):
        return self._atq

    @property
    def dfs(self):
        return self._dfs

    @property
    def torso(self):
        return self._torso

    @property
    def pernas(self):
        return self._pernas

    @property
    def bracoE(self):
        return self._bracoE

    @property
    def bracoD(self):
        return self._bracoD

    @property
    def bonusATQ(self):
        return self._bonusATQ

    @property
    def bonusDFS(self):
        return self._bonusDFS

    @property
    def adquirido(self):
        return self._adquirido

    @bracoE.setter
    def bracoE(self, bracoE):
        self._bracoE = bracoE

    @bracoD.setter
    def bracoD(self, bracoD):
        self._bracoD = bracoD

    @torso.setter
    def torso(self, torso):
        self._torso = torso

    @pernas.setter
    def pernas(self, pernas):
        self._pernas = pernas

    @atq.setter
    def atq(self, atq):
        self._atq = atq

    @dfs.setter
    def dfs(self, dfs):
        self._dfs = dfs

    @adquirido.setter
    def adquirido(self, adquirido):
        self._adquirido = adquirido


class Medalutador:
    def __init__(self, id, H, k, medabot, lista_bracoE, lista_bracoD, lista_torso, lista_pernas):
        self._id = id
        self._medabot = medabot
        self._H = H
        self._k = k
        self._lista_bracoE = lista_bracoE
        self._lista_bracoD = lista_bracoD
        self._lista_torso = lista_torso
        self._lista_pernas = lista_pernas
        self._Hinicial = H

    def obter_ID(self):
        return self._id

    @property
    def lista_pernas(self):
        return self._lista_pernas

    @property
    def lista_bracoE(self):
        return self._lista_bracoE

    @property
    def lista_bracoD(self):
        return self._lista_bracoD

    @property
    def lista_torso(self):
        return self._lista_torso

    @property
    def id(self):
        return self._id

    @property
    def Hinicial(self):
        return self._Hinicial

    @property
    def H(self):
        return self._H

    @property
    def k(self):
        return self._k

    @property
    def medabot(self):
        return self._medabot

    @H.setter
    def H(self, H):
        self._H = H

    def __repr__(self):
        return str(self.id)


def substituicao(vencedor, perdedor):
    '''Determina as condições para a substituição das medapeças, e executa sua substituição nos atributos do vencedor.
    Muda, também, a habilidade do vencedor e do perdedor, conforme os indíce k e o resultado da batalha. Além disso,
    retorna um valor que irá ser usado na função "imprimir_resultado_da_batalha"'''
    dif_bracoE = int(perdedor.medabot.bracoE) - int(vencedor.medabot.bracoE)
    dif_bracoD = int(perdedor.medabot.bracoD) - int(vencedor.medabot.bracoD)
    dif_torso = int(perdedor.medabot.torso) - int(vencedor.medabot.torso)
    dif_pernas = int(perdedor.medabot.pernas) - int(vencedor.medabot.pernas)
    dif_habilidade = int(vencedor.H) - int(perdedor.H) if int(vencedor.H) - int(perdedor.H) > 0 else 0

    if dif_torso >= dif_bracoE and dif_torso >= dif_bracoD and dif_torso >= dif_pernas:
        vencedor.lista_torso.append(perdedor.medabot.torso)
        vencedor.medabot.torso = max(vencedor.lista_torso)
        vencedor.medabot.adquirido = (f"T{perdedor.medabot.torso}")
        perdedor.lista_torso.remove(perdedor.medabot.torso)
        perdedor.medabot.torso = max(perdedor.lista_torso)

    elif dif_bracoE >= dif_bracoD and dif_bracoE > dif_torso and dif_bracoE >= dif_pernas:
        vencedor.lista_bracoE.append(perdedor.medabot.bracoE)
        vencedor.medabot.bracoE = max(vencedor.lista_bracoE)
        vencedor.medabot.adquirido = (f"E{perdedor.medabot.bracoE}")
        perdedor.lista_bracoE.remove(perdedor.medabot.bracoE)
        perdedor.medabot.bracoE = max(perdedor.lista_bracoE)

    elif dif_bracoD > dif_bracoE and dif_bracoD > dif_torso and dif_bracoD >= dif_pernas:
        vencedor.lista_bracoD.append(perdedor.medabot.bracoD)
        vencedor.medabot.bracoD = max(vencedor.lista_bracoD)
        vencedor.medabot.adquirido = (f"D{perdedor.medabot.bracoD}")
        perdedor.lista_bracoD.remove(perdedor.medabot.bracoD)
        perdedor.medabot.bracoD = max(perdedor.lista_bracoD)

    else:
        vencedor.lista_pernas.append(perdedor.medabot.pernas)
        vencedor.medabot.pernas = max(vencedor.lista_pernas)
        vencedor.medabot.adquirido = (f"P{perdedor.medabot.pernas}")
        perdedor.lista_pernas.remove(perdedor.medabot.pernas)
        perdedor.medabot.pernas = max(perdedor.lista_pernas)

    if dif_habilidade + int(vencedor.k) <= vencedor.Hinicial:
        vencedor.H = dif_habilidade + int(vencedor.k)
    else:
        vencedor.H = vencedor.Hinicial
    if (int(perdedor.H)//2) + int(perdedor.k) <= int(perdedor.Hinicial):
        perdedor.H = (int(perdedor.H)//2) + int(perdedor.k)
    else:
        perdedor.H = perdedor.Hinicial

    vencedor.medabot.dfs = int(max(vencedor.lista_torso)) + int(max(vencedor.lista_pernas)) + int(vencedor.medabot.bonusDFS)
    perdedor.medabot.dfs = int(max(perdedor.lista_torso)) + int(max(perdedor.lista_pernas)) + int(perdedor.medabot.bonusDFS)
    vencedor.medabot.atq = int(max(vencedor.lista_bracoE)) + int(max(vencedor.lista_bracoD)) + int(vencedor.medabot.bonusATQ)
    perdedor.medabot.atq = int(max(perdedor.lista_bracoE)) + int(max(perdedor.lista_bracoD)) + int(perdedor.medabot.bonusATQ)


def imprimir_ficha_tecnica(i, j):
    '''Imprime o valor de cada atributo do medabot, bem como a soma responsável por esse resultado'''
    print(f'\tA{str(i.obter_ID())} = E{str(i.medabot.bracoE)} + D{str(i.medabot.bracoD)} + {str(i.medabot.bonusATQ)} = {str(i.medabot.atq)}')
    print(f'\tD{str(i.obter_ID())} = T{str(i.medabot.torso)} + P{str(i.medabot.pernas)} + {str(i.medabot.bonusDFS)} = {str(i.medabot.dfs)}')
    print(f'\tH{str(i.obter_ID())} = {str(i.H)}')
    print(f'\tA{str(j.obter_ID())} = E{str(j.medabot.bracoE)} + D{str(j.medabot.bracoD)} + {str(j.medabot.bonusATQ)} = {str(j.medabot.atq)}')
    print(f'\tD{str(j.obter_ID())} = T{str(j.medabot.torso)} + P{str(j.medabot.pernas)} + {str(j.medabot.bonusDFS)} = {str(j.medabot.dfs)}')
    print(f'\tH{str(j.obter_ID())} = {str(j.H)}')


def batalhar(i, j):
    '''Define os padrões para se estabelecer o vencedor, e devolve o vencedor'''
    if (i.medabot.atq > j.medabot.dfs or i.medabot.dfs < j.medabot.atq) and i.medabot.atq - j.medabot.dfs != j.medabot.atq - i.medabot.dfs:
        if i.medabot.atq - j.medabot.dfs > j.medabot.atq - i.medabot.dfs:
            substituicao(i, j)
            return i
        else:
            substituicao(j, i)
            return j

    elif i.H != j.H:
        if i.H > j.H:
            substituicao(i, j)
            return i
        elif i.H < j.H:
            substituicao(j, i)
            return j
    else:
        if i.obter_ID() < j.obter_ID():
            substituicao(i, j)
            return i
        elif i.obter_ID() > j.obter_ID():
            substituicao(j, i)
            return j


def imprimir_resultado_da_batalha(k):
    print(f'Medalutador {k} venceu e recebeu a {k.medabot.adquirido}\n')



def simular_torneios_de_cyberlutas(lista_de_medalutadores):
  lista_torneio_principal = []
  lista_de_repescagem     = []
  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)
  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)
  print('Cyberluta Final')
  print(f'Medalutadores: {i} vs {j}')
  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j)
  print(f'Campeao: medalutador {k}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
  if len(lista_de_medalutadores) < 2:
    return lista_de_medalutadores
  lista_de_vencedores = []
  while len(lista_de_medalutadores) >= 2:
    i = lista_de_medalutadores.pop(0)
    j = lista_de_medalutadores.pop(0)
    if i.obter_ID() > j.obter_ID():
      i, j = j, i
    if lista_de_repescagem != None:
      print('Cyberluta do Torneio Principal')
    else:
      print('Cyberluta da Repescagem')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    imprimir_resultado_da_batalha(k)
    if lista_de_repescagem != None:
      if i == k:
        lista_de_repescagem.append(j)
      else:
        lista_de_repescagem.append(i)
    lista_de_vencedores.append(k)
  lista_de_vencedores.extend(lista_de_medalutadores)
  return lista_de_vencedores



# Print inicial, que define a quantidade de medalutadores que participarão do torneio.
n = int(input())
lista_de_medalutadores = []

for k in range(n):  # Inicio dos inputs, que serão responsáveis pela habilidade, índice K e quantidade
                    # de atributos incial. Define-se, também, as listas de atributos de cada medapeça.
    input_1 = input().split(" ")
    input_medalha = input()
    braco_direito = [0]
    braco_esquerdo = [0]
    pernas = [0]
    torso = [0]
    for g in range(int(input_1[2])):  # Inputs relativos às medapeças de cada medalutador e organização conforme o tipo
        pontos = input()
        if pontos[0] == "D":
            braco_direito.append(int(pontos[2:]))
        elif pontos[0] == "E":
            braco_esquerdo.append(int(pontos[2:]))
        elif pontos[0] == "P":
            pernas.append(int(pontos[2:]))
        elif pontos[0] == "T":
            torso.append(int(pontos[2:]))
    # definindo os medabots a partir dos atributos obtidos pelas entradas, e atribuindo o respectivo medabot ao medalutador
    medabot = Medabot(max(braco_direito) + max(braco_esquerdo) + int(input_medalha[0:2]),
                    max(torso) + max(pernas) + int(input_medalha[2:]),
                    max(torso),
                    max(pernas),
                    max(braco_esquerdo),
                    max(braco_direito),
                    int(input_medalha[0:2]),
                    int(input_medalha[2:]),
                    None)
    medalutador = Medalutador(k + 1, int(input_1[0]), int(input_1[1]), medabot, braco_esquerdo, braco_direito, torso, pernas)
    lista_de_medalutadores.append(medalutador)



simular_torneios_de_cyberlutas(lista_de_medalutadores)
