# print(list(range(10)))

# lista = [numero for numero in range(11)]
# print(lista)

# lista = [numero * 3 for numero in range(11)]
# print(lista)

# pessoas = [
#   { 'nome': 'Isaias', 'idade': 24 },
#   { 'nome': 'Janaina', 'idade': 42 },
#   { 'nome': 'Kero', 'idade': 27 }
# ]
# idades = [pessoa['idade'] for pessoa in pessoas]
# nomes = [pessoa['nome'] for pessoa in pessoas]
# print(idades)
# print(nomes)

produtos = [
  {'produto': 'p1', 'preco': 20 },
  {'produto': 'p1', 'preco': 65 },
  {'produto': 'p1', 'preco': 33 }
]

mapProdutos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  for produto in produtos
]
print(*mapProdutos, sep='\n')



