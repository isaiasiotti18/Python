def soma(*args):
  return sum(args)
  
print(soma(9,2,4,7,9,6,3))

numeros = 1,2,34,5
print(soma(*numeros))