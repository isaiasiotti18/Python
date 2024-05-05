horario = input("Informe as horas (Número Inteiro): ")

try:
  horaInformada = int(horario)
  if(horaInformada >= 0 and horaInformada <= 11):
    print('Bom dia! 0-11')
  elif(horaInformada >= 12 and horaInformada <= 17):
    print('Boa tarde! 12-17')
  elif(horaInformada >= 18 and horaInformada <= 23):
    print('Boa noite! 12-17')
  else:
    print('Número informado incorreto.')
except:
  print("Você precisa informar um número inteiro")