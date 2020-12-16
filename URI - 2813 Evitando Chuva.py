dias = int(input())

emcasa = 0
levadoParaCasa = 0
Escritorio = 0
levadoParaEscritorio = 0

for i in range(dias):
    x, y = input().split()
    if x == "chuva":
        if levadoParaCasa == 0:
            emcasa += 1
            levadoParaEscritorio += 1
        else:
            levadoParaCasa -= 1
            levadoParaEscritorio += 1
    if y == "chuva":
        if levadoParaEscritorio == 0:
            Escritorio += 1
            levadoParaCasa += 1
        else:
            levadoParaEscritorio = levadoParaEscritorio - 1
            levadoParaCasa = levadoParaCasa + 1
print(emcasa, Escritorio)