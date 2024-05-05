conjunto = set()

conjunto.add(1)

conjunto.add('Isaias')

conjunto.update({'Isaias02', 'Kero', 2349, 'Outro Nome'})

print(conjunto)

conjunto.remove('Isaias') #Aqui da erro se não encontrar o elemento

print(conjunto)

conjunto.discard(2349) #Aqui não dá erro.

print(conjunto)