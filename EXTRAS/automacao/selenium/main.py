import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

path = 'C:\\Users\\isaia\\Desktop\\Python\\EXTRAS\\automacao\\selenium\\'

caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True
caps['acceptSslCerts'] = True

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options, desired_capabilities=caps)

driver.get("https://valorinveste.globo.com/cotacoes/")

driver.find_element(By.CLASS_NAME, 'cookie-banner-lgpd_accept-button').click()
  
tableRows = driver.find_elements(By.TAG_NAME, 'tr')
tableRows.pop(0)
tableRows.pop(-1)

stocks = []

# USAR XPATH como se fosse um seletor parent - children

for row in tableRows:
  try:
    nameStock = row.find_element(By.TAG_NAME, 'td')
    codigo = row.find_element(By.XPATH, f'//tr[{tableRows.index(row)+1}]/td[2]')
    valor = row.find_element(By.XPATH, f'//tr[{tableRows.index(row)+1}]/td[3]')
    variacao = row.find_element(By.XPATH, f'//tr[{tableRows.index(row)+1}]/td[4]')
    fechamento_dia_anterior = row.find_element(By.XPATH, f'//tr[{tableRows.index(row)+1}]/td[5]')
    restInformation = row.text.split(' ')
        
    stock = {
      'nome': nameStock.text,
      'codigo': codigo.text,
      'valor': valor.text,
      'variacao': variacao.text,
      'fechamento_dia_anterior': fechamento_dia_anterior.text,
    }
    stocks.append(stock)
  
  except Exception as e:
    print("Erro inesperado, finalizando...")
    break
  
driver.quit()

sleep(2)

file_name = 'arquivo.json'
file_path = path + file_name

print("Iniciando escrita no arquivo JSON...")
sleep(2)

with open(file_path, 'w', encoding='utf-8') as file:
  json.dump(
    stocks, 
    file, 
    ensure_ascii=False,
    indent=2
  )
  
  print("ESCRITA NO ARQUIVO FINALIZADA...")

# tableRowsFile = path+'tableRows.txt'
# with open(tableRowsFile, 'w', encoding='utf-8') as file:
#   for row in tableRows:
#     newRow = row.text.split(' ')
#     file.write(f'{newRow}\n')
#   sleep(3)