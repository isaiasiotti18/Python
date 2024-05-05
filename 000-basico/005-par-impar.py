numero = input("Informe um número inteiro: ")

try:
  numInformado = int(numero)
  if(numInformado % 2 == 0):
    print(f'O número {numero} é um número Par')
  elif(numInformado % 2 != 0 ):
    print(f'O número {numero} informado é um número Ímpar')
except:
  print("Você precisa informar um número inteiro")