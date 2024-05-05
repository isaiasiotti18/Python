while True:
  n1 = input('Digite um número: ')
  n2 = input('Digite outro número: ')
  operador = input('Digite um operador (+-/*): ')
  
  numeros_validos = None
  
  try:
    n1 = float(n1)
    n2 = float(n2)
    numeros_validos = True
  except:
    numeros_validos = None
    
  if numeros_validos is None:
    print('Números Digitados são Invalidos.')
    continue
  
  operadores_permitidos = '+-/*'
  
  if (operador not in operadores_permitidos) and (len(operador) > 1):
    print('Operador Invalido.')
    continue
  
  if operador == '+':
    print(n1 + n2)
  elif operador == '-':
    print(n1 - n2)
  elif operador == '*':
    print(n1 * n2)
  elif operador == '/':
    try:
      print(n1 / n2)
    except:
      print('Você está tentando realizar divisão por zero...')
      continue
  else:
    print('Algo inesperado aconteceu.')
  
  sair = input('Quer sair? [s] sim: ').lower().startswith('s')
  if sair is True:
    break