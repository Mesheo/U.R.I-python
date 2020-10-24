#recebe a quantidade de vezes que vai fazer o processo
n = int(input())

#executa o loop nessa quantidade
for i in range(n):
    
    #receber quantidade de carneiros
    numero_de_carneirinhos = int(input())
    #recebe numero de cada carneiro
    carneiros = input().split()
    #analisa a lista carneiros
        
    carneiros_de_vdd = []
    for carneiro in carneiros:
            
        #adiciona o carneiro na lista se ele não se repetir
        if carneiro not in carneiros_de_vdd:
            carneiros_de_vdd.append(carneiro)
            
    print(len(carneiros_de_vdd)) 