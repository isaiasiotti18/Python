lista = [1, 45, 29, 20, 19, 29, 38, 47, 91]
lista.sort(reverse=True)
print(lista)

nomes = [
  {'nome': 'Isaias'},
  {'nome': 'Santos'},
  {'nome': 'Batista'},
  {'nome': 'Iotti'},
  {'nome': 'Obliquio'}
]

nomes.sort(key=lambda item: item['nome'])
print(nomes)

