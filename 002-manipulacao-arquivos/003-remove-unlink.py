import os

path = 'C:\\Users\\isaia\\Desktop\\Python\\002-manipulacao-arquivos\\folder\\'
txt = 'meuarquivo.txt'
file_path = path + txt


# O 'a+' começa a escrever na ultima linha do arquivo (append mode)
with open(file_path, 'a+', encoding='utf-8') as file:
  file.write('Primeira Linha\n')
  file.write('Segunda Linha.\n')
  file.seek(0,0) # Movendo o cursor para o topo do arquivo
  print(file.read())
  

# Os dois fazem a mesma coisa.
os.unlink(file_path)
# os.remove(file_path)