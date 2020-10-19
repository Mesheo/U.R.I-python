def mostrar(a, b):
    for i in range(len(a)):
        print(f'{b}[{i}] = {a[i]}')
    return None

par = []
impar = []

for n in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        mostrar(par, 'par')
        par.clear()
    elif len(impar) == 5:
        mostrar(impar, 'impar')
        impar.clear()
mostrar(impar, 'impar')
mostrar(par, 'par')
