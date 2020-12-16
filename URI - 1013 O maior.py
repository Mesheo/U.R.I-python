def maiorTermo(a, b, c):
    #variavel a na posicao maior
    if a > b and a > c:
        maior = a
        if b > c:
            meio_termo = b
            menor = c
        else:
            meio_termo = c
            menor = b
            
    #varivel a na posição meio_termo       
    elif a > b and a < c:
        meio_termo = a
        if b > c:
            maior = b
            menor = c
        else:
            maior = c
            menor = b
            
    #variavel a na posicao menor   
    elif a < b and a < c:
        menor = a
        if b > c:
            maior = b
            meio_termo = c
        else:
            maior = c
            meio_termo = b
    
    return maior


#ProgamaPrincipal
a, b , c = input().split()

maior = 0
menor = 0
meio_termo = 0

maior = maiorTermo(int(a), int(b) ,int(c))
print(f'{maior} eh o maior')