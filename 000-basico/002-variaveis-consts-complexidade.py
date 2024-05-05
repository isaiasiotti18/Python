ISSO_E_UMA_CONSTANTE = 100 #CONSTANTE
isso_nao = "Não sou uma constante, e sim uma variável" #variavel


velocidade = 61
local_carro = 101

RADAR = 60 # Velocidade maxima ro radar 1
LOCAL_1 = 100 # Local do radar
RADAR_RANGE = 1 # A distância onde o radar pega

if velocidade > RADAR:
  print("Velocidade carro passou do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
  local_carro <= (LOCAL_1 + RADAR_RANGE) and \
  velocidade > RADAR:
    print('carro multado em radar 1') 