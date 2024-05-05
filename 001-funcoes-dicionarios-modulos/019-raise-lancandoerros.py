def lancaErro():
  raise ZeroDivisionError('Divisor não pode ser zero.')

def divide(x,y):
  if y == 0:
    lancaErro()
  
  return x / y

print(divide(6,0))