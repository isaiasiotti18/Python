import json

pessoa = {
  'nome': 'Isaias',
  'idade': 24,
  'peso': 85.8,
  'enderecos': [
    { 'residencial': {
        'endereco': 'Av. Eduardo Andrea Matarazzo',
        'numero': 6130,
        'complemento': 'BLOCO 01, APTO 203',
        'cep': 14075820
      }
    },
    { 'comercial': {
        'endereco': 'Av. Eduardo Andrea Matarazzo',
        'numero': 4015,
        'complemento': 'Atacadão S.A',
        'cep': 14061810
      }
    }
  ]
}

path = 'C:\\Users\\isaia\\Desktop\\Python\\002-manipulacao-arquivos\\folder\\'
file_name = 'arquivo.json'
file_path = path + file_name

with open(file_path, 'w', encoding='utf-8') as file:
  json.dump(
    pessoa, 
    file, 
    ensure_ascii=False,
    indent=2
  )

with open(file_path, 'r') as file:
  pessoa = json.load(file)
  print(pessoa)
  print(type(pessoa))
