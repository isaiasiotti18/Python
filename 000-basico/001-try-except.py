numero = input("Vou dobrar: ")

try:
  numero_float = float(numero)
  print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
  print('Isso não é um numero.')