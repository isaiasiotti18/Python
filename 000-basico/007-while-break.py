condicao = True

while condicao:
  nome = input("Qual é o seu nome: ")
  print(f'Seu nome é {nome}')
  print('Para finalizar digite "sair" ')
  
  if nome == 'sair':
    break