def numApareceMenosVzs(qtdVzs_cada_num, valores, numero_max):
    for numero in range(1,numero_max+1):
        if valores.count(numero) == min(qtdVzs_cada_num):
            print(numero, end=' ')
    print()
    
# PP
qtd_de_cartelas, qtd_numeros, numero_max = list(map(int,input().split()))

while qtd_de_cartelas != 0 and qtd_numeros != 0 and numero_max != 0:
    valores = []
    qtdVzs_cada_num = []

    for cartela in range(qtd_de_cartelas):
        x = [valores.append(y) for y in list(map(int, input().split()))]

    for numero in range(1,numero_max+1):
        qtdVzs_cada_num.append(valores.count(numero))

    numApareceMenosVzs(qtdVzs_cada_num, valores, numero_max)
    qtd_de_cartelas, qtd_numeros, numero_max = list(map(int,input().split()))