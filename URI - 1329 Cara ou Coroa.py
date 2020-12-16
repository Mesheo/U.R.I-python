#numero de vezes que vou fazer o precesso
quantidades_de_jogadas = int(input())

#contador de vitoria para mary e john
mary = 0
john = 0

#executa o loop enquanto for diferente de 0
while quantidades_de_jogadas != 0:
    resultados = input().split()
    
    #para cada numero dentro de resultados analisar se é 0 ou 1
    for numero in resultados:
        
        #se for zero, acrescentar no contador mary
        if numero == '0':
            mary += 1
        #se não for zero acrescentar no contador john
        else:
            john += 1
            
    print(f'Mary won {mary} times and John won {john} times')
    quantidades_de_jogadas = int(input())
    mary = 0
    john = 0