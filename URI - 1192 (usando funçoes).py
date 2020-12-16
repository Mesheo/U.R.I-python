def hash(itens, tabela):
    for item in itens:
        posicao = item % len(tabela)
        tabela[posicao].append(item)

def mostrar(tabela):
    final = ' -> \ '
    meio = ' ->'
    for indice in range(len(tabela)):
        print(indice, end ='')
        for numero in tabela[indice]:
            print(meio, numero, end = '')
        print(final)
n = int(input())

for b in range(n):
    tamanho_da_tabela, qtd_itens = map(int, input().split())
    itens = list(map(int, input().split()))

    tabela = []
    #preencher tabela
    for i in range(tamanho_da_tabela):
        index = []
        tabela.append(index)

    hash(itens, tabela)
    mostrar(tabela)
    while b < n:
        print()