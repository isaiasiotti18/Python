cpf = '07107429590'
nove_digitos = cpf[:9]

regressivo = 10

resultado = 0

for digito in nove_digitos:
  resultado += int(digito) * regressivo
  regressivo -= 1
  

primeiro_digito = (resultado * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# ====

dez_digitos = nove_digitos + str(primeiro_digito)
regressivo_02 = 11

resultado_02 = 0

for digito in dez_digitos:
  resultado_02 += int(digito) * regressivo_02
  regressivo_02 -= 1

segundo_digito = (resultado_02 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado:
  print('CPF É VÁLIDO.')
else:
  print('CPF INVALIDO.')