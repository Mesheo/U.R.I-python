#recebe a quantidade de vezes que vai fazer o processo
n = int(input())

#executa o loop nessa quantidade
for i in range(n):
    
    #receber quantidade de carneiros
    numero_de_carneirinhos = int(input())
    #recebe numero de cada carneiro
    carneiros = input().split()
    
    #Monto um conjunto (sem repetições)
    conjunto_carneiros = set(carneiros)
    
    #printo o tamanho do conjunto
    print(len(conjunto_carneiros))
    