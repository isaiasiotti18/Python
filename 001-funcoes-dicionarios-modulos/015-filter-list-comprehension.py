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

import pprint

def p(v):
  pprint.pprint(v, sort_dicts=False, width=40)
  

produtos = [
  {'produto': 'p1', 'preco': 20 },
  {'produto': 'p1-2', 'preco': 8 },
  {'produto': 'p2', 'preco': 65 },
  {'produto': 'p3', 'preco': 33 },
  {'produto': 'p4', 'preco': 14 }
]

# ANTES DO FOR é MAPEAMENTO
# DEPOIS DO FOR é FILTER
mapProdutos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  if produto['preco'] > 20 else {**produto}
  for produto in produtos
  if produto['preco'] > 10
]
p(mapProdutos)

