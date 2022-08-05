# -*- coding: utf-8 -*-
bd1 = [] #vetor input inicial
bd2 = [] #vetor TTASK
umax = 0
ttask =0
# funcao ler arquivo input
def ler_input():
    try:
        with open("input.txt", "r") as entrada:
            bd = entrada.read()
            bd = bd.split("\n")
            for num, item in enumerate(bd):
                bd[num] = int(item)
            return bd
    except ValueError as e:
        print("Erro, não encontrei o arquivo / outro", e)
        return False
        
def gera_bd_tttask():
    global bd1, bd2, umax, ttask
    bd1 =  ler_input() 
    ttask = bd1[0] # pego TTASK posicao 0
    umax = int(bd1[1]) #pego umax posicao 1
    base = int(bd1[2] + ttask) #base para o vetor de monitor TTASK 4+1 = 5
    bd1 = bd1[2:len(bd1)]
    for item in bd1:
        if (item != 0):
            bd2.append(base)
        else:
            bd2.append(0)
        base += 1
gera_bd_tttask()

#pego a ultima casa do vetor TTASK para finalizar o monitor de TTASK
ultima_casa = bd2[-1]

servidores = 0 
def computa_dados(num):
  global servidores
  serv_nec = int(num/2)+num%2
  if(serv_nec>servidores):
    compl=f"{serv_nec-servidores} servidor criado"
    servidores = serv_nec
  elif(serv_nec==servidores):
    compl="nenhum servidor criado ou removido"
  else:
    compl = f"{abs(serv_nec-servidores)} servidor removido"
    servidores = serv_nec
  regra = f'{serv_nec} servidor para {num} usuario: {compl}'
  return(regra)
  


print(f"\n{5*'*'}MONITOR TTASK X SERVIDOR{5*'*'}\n")
t = 0
while True:
    #gero as combinacoes possiveis para o monitor de TTASK
    #pegando o vetor criado e subtraindo 1 para todos valores n 0
    for num, item in enumerate(bd2):
        if (bd2[num]) != 0:
            bd2[num] -= 1
    t += 1

    soma = 0
    for n in range(0, t):
        try:
            if (bd2[n] != 0):
                soma += bd1[n]
        except:
            if n + 1 == ultima_casa:
                soma = 0
            else:
                soma = bd1[-1]

    print(t, "-", soma, bd2, computa_dados(soma))
    #caso o ultimo valor do vetor TTASK seja 0 ele para o loop
    if bd2[-1] == 0:
        break