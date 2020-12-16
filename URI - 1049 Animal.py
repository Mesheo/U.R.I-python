#Recebe as entradas
caracteristica_a = input('')
caracteristica_b = input('')
caracteristica_c = input('')

#Dicionario com as chaves(nome dos animais) e os valores(caracteristicas)
animais = {'aguia': ['carnivoro', 'ave', 'vertebrado'],
            'pomba': ['onivoro', 'ave', 'vertebrado'],
           'homem': ['onivoro', 'mamifero', 'vertebrado'],
            'vaca': ['herbivoro', 'mamifero', 'vertebrado'],
           'pulga': ['hematofago', 'inseto', 'invertebrado'],
           'lagarta': ['herbivoro', 'inseto', 'invertebrado'],
            'sanguessuga': ['hematofago', 'anelideo', 'invertebrado'],
           'minhoca': ['invertebrado', 'anelideo', 'onivoro']}

#Percorre cada chave dentro do dicionário
for key in animais.keys():
    
    #checa se as caracteristicas estão dentro dos valores de cada chave
    if caracteristica_a in animais[key]:
        if caracteristica_b in animais[key]:
            if caracteristica_c in animais[key]:
                print(key)
  
    
