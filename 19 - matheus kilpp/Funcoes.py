def validar_placa(placa):
    if len(placa) != 8:  # Verifica se a placa tem exatamente 8 caracteres
        return False
    elif not (placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha()): # Verifica se os 3 primeiros caracteres são letras
        return False
    elif placa[3] != '-':  # Verifica se o 4 caractere é um hifen
        return False
    elif not (placa[4].isdigit() and placa[5].isdigit() and placa[6].isdigit() and placa[7].isdigit()):  # Verifica se os 4 últimos caracteres são números
        return False
    else:
      return True

def cadastrar_placa():
  letras_mercosul = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
  placa = input("Digite a placa do carro (Ex: AAA-1111): ").upper()
  if validar_placa(placa):
      numero = int(placa[5])
      placa_mercosul = placa[:5] + letras_mercosul[numero] + placa[6:] #Cria a placa mercosul

      if verificar_estado(placa): # Verifica se a placa pertence a SC
        estado = "SC"
      else:
        estado = "Outro estado"

      if ler_placa(placa):
        print("Esta placa já foi registrada")
        return
      else:
        with open('placas_cadastradas.txt', 'a') as arquivo: #adiciona no arquivo a nova placa
          arquivo.write(f"{placa},{placa_mercosul},{estado}\n")
          print("Placa cadastrada com sucesso")
          print(f"Placa normal: {placa}, Placa Mercosul: {placa_mercosul}, Estado: {estado}")
  else:
      print("Formato de placa inválido. Use o formato AAA-1111")


def verificar_estado(placa):
    intervalos_sc = [("LWR", "MMM"), ("OKD", "OKH"), ("QHA", "QJZ"), ("QTK", "QTM"), ("RAA", "RAJ"), ("RDS", "REB"), ("RKW", "RLP")] # Letras de Santa Catarina
    prefixo = placa[:3]   # Escolhe as primeiras letras do código
    for (inicio, fim) in intervalos_sc:  # Verificar se as letras estao na lista
        if inicio <= prefixo <= fim:
          return True
        else:
          return False


def consultar_placa():
    placa = input("Digite a placa do carro (Ex: AAA-1111): ").upper() #pede a placa
    if not validar_placa(placa): # Validar a placa
        print("A placa fornecida está fora do formato esperado. Use o formato AAA-1111")
        return
    else:
      if verificar_estado(placa): # Chama a função de verificar o estado
        print(f"A placa {placa} pertence ao estado de Santa Catarina (SC)")
      else:
        print(f"A placa {placa} não pertence ao estado de Santa Catarina (SC)")

def listar_placa():
    try:
        with open('placas_cadastradas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        if not linhas: #caso nao tenha cadastro, mostrara uma mensagem para usuario
            print("Nenhuma placa cadastrada")
        else:
            print("-----Placas cadastradas:-----")
            for linha in linhas:
                print(linha.strip()) #mostra as placas cadastradas, por linha, apagando qualquer caractere em branco ou vazio
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")

def alterar_placa():
    try:
        with open('placas_cadastradas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        if not linhas:
            print("Nenhuma placa cadastrada") #caso nao tenha cadastro, mostrara uma mensagem para usuario
            return

        placa_alterar = input("Digite a placa que deseja alterar (AAA-1111): ").upper() #pede a placa de alterar para o usuario

        if not validar_placa(placa_alterar):
            print("Erro: A placa fornecida está fora do formato esperado. Use o formato AAA-1111)")
            return

        encontrado = False
        nova_placa = input("Digite a nova placa (AAA-1111): ").upper()

        if validar_placa(nova_placa):
          letras_mercosul = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
          numero = int(nova_placa[5]) #faz a placa mercosul a partir da placa_alterar
          nova_mercosul = nova_placa[:5] + letras_mercosul[numero] + nova_placa[6:]

          if verificar_estado(nova_placa): # Verifica se a placa pertence a SC
            novo_estado = "SC"
          else:
            novo_estado = "Outro estado"

          if ler_placa(nova_placa): #verifica se a placa que deseja alterar já esta registrada
            print("A placa nova que deseja alterar já está registrada")
            return

        else:
          print("Erro: A nova placa fornecida está fora do formato esperado. Use o formato AAA-1111)")
          return


        with open('placas_cadastradas.txt', 'w') as arquivo:
            for linha in linhas:
                placa, placa_mercosul, estado = linha.strip().split(',') #poe todas as linhas no padrao com virgula
                if placa == placa_alterar: #substitui a placa
                 arquivo.write(f"{nova_placa},{nova_mercosul},{novo_estado}\n") #escreve a nova placa no arquivo
                 print(f"Placa alterada com sucesso!, nova placa: {nova_placa}, placa mercosul: {nova_mercosul}, estado: {novo_estado}")
                 encontrado = True
                else:
                    arquivo.write(linha) #caso nao seja a placa desejada, a linha será reescrita

        if not encontrado:
            print("Placa não encontrada")
    except FileNotFoundError:
      print("Arquivo de dados não encontrado")

def excluir_placa():
    try:
        with open('placas_cadastradas.txt', 'r') as arquivo: #abrir o arquivo de leitura
            linhas = arquivo.readlines()
        if not linhas:
          print("Nenhuma placa cadastrada")
          return
        else:
          placa_excluir = input("Digite a placa que deseja excluir (Ex: AAA-1111): ").upper()

        with open('placas_cadastradas.txt', 'w') as arquivo:
            placa_encontrada = False
            for linha in linhas:
                dados = linha.strip().split(',')
                placa = dados[0]  # pega o primeiro indice, a placa
                if placa != placa_excluir:
                    arquivo.write(linha)  #reescreve a linha, assim, nao apagando
                else:
                    placa_encontrada = True

            if placa_encontrada:
                print(f"Placa excluída com sucesso, placa excluída: {placa_excluir}")
            else:
                print("Placa não encontrada")

    except FileNotFoundError:
        print("Arquivo de dados não encontrado")

def ler_placa(placa_procurada):
  try:
    with open('placas_cadastradas.txt', 'r') as arquivo:
      linhas = arquivo.readlines()
      for linha in linhas:
        placa, placa_mercosul, estado = linha.strip().split(',')
        if placa == placa_procurada:
          return True  # Placa encontrada
    return False  # Placa não encontrada
  except FileNotFoundError:
    return False