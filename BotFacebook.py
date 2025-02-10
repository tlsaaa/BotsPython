import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException

options = Options()
options.add_argument('-profile')
options.add_argument('/home/maquinalinux/snap/firefox/common/.mozilla/firefox/4bam2voy.Default User/')

service = Service(executable_path='/usr/local/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, timeout = 10)
valor=0
postou=0
cont_postou = 0
nao_encontrado = 0
url = 'https://web.facebook.com/marketplace/you/selling?title_search='
codigo = ["TRV", "CSV", "OUT", "APV", "LOC"]
cont_codigo = 0
lista_de_nao_encontrado = ["TRV-001"]

while postou < 1000:
 if cont_postou < 20:
  valor+=1
  if f'{codigo[cont_codigo]}-00{valor}' not in lista_de_nao_encontrado and f'{codigo[cont_codigo]}-0{valor}' not in lista_de_nao_encontrado:
   if nao_encontrado < 15:
    if valor < 10:
     url_nova = f'{url}{codigo[cont_codigo]}-00{valor}'
     driver.get(url_nova)
     try:
      image = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@class="xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3"]')))
      time.sleep(3)
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
       buton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3" and @aria-label="Postar"]')))
       buton.click()
       postou +=1
       cont_postou +=1
       nao_encontrado = 0
       time.sleep(3)
      except NoSuchElementException:
       time.sleep(3)
       print(f'{codigo[cont_codigo]}-00{valor}')
       print("nao tem o link para anunciar")
       nao_encontrado+=1
       lista_de_nao_encontrado.append(f'{codigo[cont_codigo]}-00{valor}')
 
     except TimeoutException:
      try: 
       caso_2 = driver.find_element(By.XPATH, "//*[text()='Tente usar outras palavras-chave ou confira se está tudo escrito corretamente']")
       time.sleep(2)
       nao_encontrado+=1
       print(f'{codigo[cont_codigo]}-00{valor}')
       lista_de_nao_encontrado.append(f'{codigo[cont_codigo]}-00{valor}')
       print("imovel nao cadastrado")

      except NoSuchElementException:
       print("erro ao tentar clicar na imagem")
       break

    else:
     url_nova = f'{url}{codigo[cont_codigo]}-0{valor}'
     driver.get(url_nova)
     time.sleep(10)

     try:
      image = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@class="xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3"]')))
      time.sleep(3)
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
       buton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3" and @aria-label="Postar"]')))
       buton.click()
       postou +=1
       cont_postou +=1
       nao_encontrado = 0
       time.sleep(3)
      except NoSuchElementException:
       time.sleep(3)
       print(f'{codigo[cont_codigo]}-00{valor}')
       print("nao tem o link para anunciar")
       nao_encontrado+=1
       lista_de_nao_encontrado.append(f'{codigo[cont_codigo]}-0{valor}')
 
     except TimeoutException:
      try: 
       caso_2 = driver.find_element(By.XPATH, "//*[text()='Tente usar outras palavras-chave ou confira se está tudo escrito corretamente']")
       time.sleep(2)
       nao_encontrado+=1
       print(f'{codigo[cont_codigo]}-00{valor}')
       lista_de_nao_encontrado.append(f'{codigo[cont_codigo]}-0{valor}')
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



