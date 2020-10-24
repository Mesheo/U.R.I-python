tabela_leds = {'1': 2, '2': 5,
               '3': 5, '4': 4, '5': 5,
               '6': 6, '7': 3, '8' : 7,
               '9' : 6, '0': 6}
n = int(input())
for i in range(n):
    numero = input()
    c  = 0
    for a in numero:
        if a in tabela_leds.keys():
            c += tabela_leds[a]
    print(f'{c} leds')
