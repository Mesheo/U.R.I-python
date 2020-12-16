#Recebe as tomadas
tomadas = input().split()

#Armazena cada tomada em uma variável 
tomada1 = int(tomadas[0])
tomada2 = int(tomadas[1])
tomada3 = int(tomadas[2])
tomada4 = int(tomadas[3])

#Soma cada tomada e subtrai 3, o numero de tomadas perdidas.
total = (tomada1 + tomada2 + tomada3 + tomada4) -3
print(total)