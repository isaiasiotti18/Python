path = 'C:\\Users\\isaia\\Desktop\\Python\\002-manipulacao-arquivos\\folder\\'

txt = 'meuarquivo.txt'

file_path = path + txt

# file = open(file_path, 'w')
# file.close()

# with open(file_path, 'w') as file:
#   file.write('Primeira Linha\n')
#   file.write('Segunda Linha.\n')
#   print(file.read())
  
# with open(file_path, 'r') as file:
#   print(file.read())

with open(file_path, 'w+') as file:
  file.write('Primeira Linha\n')
  file.write('Segunda Linha.\n')
  file.seek(0,0) # Movendo o cursor para o topo do arquivo
  print(file.read())