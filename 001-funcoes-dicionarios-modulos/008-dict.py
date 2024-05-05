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

print(pessoa['enderecos'][0])
print(pessoa['nome'])
for dado in pessoa:
  print(dado, pessoa[dado])