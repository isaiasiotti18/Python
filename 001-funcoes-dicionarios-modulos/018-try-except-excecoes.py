try:
  a = 18
  b = 9
  c = a / b
  print(c.split())
except ZeroDivisionError:
  print('Não é possível dividir por zero.')
except NameError as error:
  print(f'Message Error: {error}')
except Exception as error:
  print(f'Message Error: {error}')