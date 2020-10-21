n = int(input())
for a in range(n):
    texto = input().split()
    t1, t2 = texto
    combinacao = ''
    
    if len(t1)<= len(t2):
        for i in range(len(t1)):
            combinacao += t1[i] + t2[i]
        combinacao += t2[len(t1):]
    else:
        for i in range(len(t2)):
            combinacao += t1[i] + t2[i]
        combinacao += t1[len(t2):]
    print(combinacao)
