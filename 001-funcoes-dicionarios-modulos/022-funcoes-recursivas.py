def recursiva(inicio=0, fim=4):
  inicio += 1
  return recursiva(inicio, fim)

def factorial(n):
  if n == 1 or n == 0:
    return 1
  return n * factorial(n - 1)


print(factorial(5))

  