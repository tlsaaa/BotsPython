import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
options = Options()
options.add_argument('-profile')
options.add_argument('/home/maquinalinux/snap/firefox/common/.mozilla/firefox/4bam2voy.Default User/')

service = Service(executable_path='/usr/local/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=options)

valor=0
postou=0
cont_postou = 0
nao_encontrado = 0
url = 'https://web.facebook.com/marketplace/you/selling?title_search='
codigo = ["TRV", "CSV", "OUT", "APV", "LOC"]
cont_codigo = 0
lista_de_nao_encontrado = []
print(f'{codigo[cont_codigo]}-00{valor}')

while postou < 1000:
 if cont_postou < 20:
  valor+=1
  if f'{codigo[cont_codigo]}-00{valor}' not in lista_de_nao_encontrado and f'{codigo[cont_codigo]}-0{valor}' not in lista_de_nao_encontrado:
   if nao_encontrado < 15:
    if valor < 10:
     url_nova = f'{url}{codigo[cont_codigo]}-00{valor}'
     driver.get(url_nova)
     time.sleep(20)
     try:
      image = driver.find_element(By.CLASS_NAME, "x1n2onr6")
      image.click()
      time.sleep(10)
      try:
       link = driver.find_element(By.XPATH, "//*[text()='Anunciar para mais locais']")
       link.click()
       time.sleep(10)
       action = ActionChains(driver)
       action.send_keys(Keys.TAB).perform()
       for i in range(20):
        action.send_keys(Keys.TAB).perform()
        time.sleep(1)
        action.send_keys(Keys.SPACE).perform()
        time.sleep(1)
       time.sleep(3)
       x=824
       y=727
       pyautogui.click(x,y)
       time.sleep(10)
       postou +=1
       cont_postou +=1
       nao_encontrado = 0
      except NoSuchElementException:
       time.sleep(3)
       print("nao tem o link para anunciar")
       nao_encontrado+=1
       lista_de_nao_encontrado.append(f'{codigo[cont_codigo]}-00{valor}')
 
     except ElementNotInteractableException:
      try: 
       caso_2 = driver.find_element(By.XPATH, "//*[text()='Tente usar outras palavras-chave ou confira se está tudo escrito corretamente']")
       time.sleep(2)
       nao_encontrado+=1
       print("imovel nao cadastrado")

      except NoSuchElementException:
       print("erro ao tentar clicar na imagem")
       break

    else:
     url_nova = f'{url}{codigo[cont_codigo]}-0{valor}'
     driver.get(url_nova)
     time.sleep(10)

     try:
      image = driver.find_element(By.CLASS_NAME, "x1n2onr6")
      image.click()
      time.sleep(10)
      try:
       link = driver.find_element(By.XPATH, "//*[text()='Anunciar para mais locais']")
       link.click()
       time.sleep(10)
       action = ActionChains(driver)
       action.send_keys(Keys.TAB).perform()
       for i in range(20):
        action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        action.send_keys(Keys.SPACE).perform()
        time.sleep(1)
       time.sleep(3)
       x=824
       y=727
       pyautogui.click(x,y)
       time.sleep(10)
       postou +=1
       cont_postou +=1
       nao_encontrado = 0
      except NoSuchElementException:
       time.sleep(3)
       print("nao tem o link para anunciar")
       nao_encontrado+=1
       lista_de_nao_encontrado.append(f'{codigo[cont_codigo]}-0{valor}')
 
     except ElementNotInteractableException:
      try: 
       caso_2 = driver.find_element(By.XPATH, "//*[text()='Tente usar outras palavras-chave ou confira se está tudo escrito corretamente']")
       time.sleep(2)
       nao_encontrado+=1
       print("imovel nao cadastrado")

      except NoSuchElementException:
       print("erro ao tentar clicar na imagem")
       break

   else:
    if cont_codigo < 3:
     cont_codigo +=1
     valor=1
     nao_encontrado = 0
    else:
     cont_codigo = 0
     valor=1
     nao_encontrado = 0

 
 else:
  print("todas as postagens foram realizadas por hoje")
  time.sleep(86400)
  cont_postou = 0



