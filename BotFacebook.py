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
lista_de_nao_encontrado = ["TRV-001","TRV-010", "TRV-014", "TRV-017", "TRV-020", "TRV-021", "TRV-024", "TRV-025", "TRV-027",
    "LOC-001", "LOC-003", "LOC-004", "LOC-006", "LOC-008", "LOC-009", "LOC-010", "LOC-011", "LOC-012", "LOC-013", 
    "LOC-014", "LOC-015", "LOC-017", "LOC-019", "LOC-020", "LOC-022", "LOC-023", "LOC-024", "LOC-025", 
    "LOC-026", "LOC-027", "LOC-028", "LOC-034", "LOC-035", "LOC-036", "LOC-039",
    "OUT-001", "OUT-004", "OUT-005", "OUT-006", "OUT-007", "OUT-008", "OUT-009", "OUT-010", "OUT-011", 
    "OUT-012", "OUT-013", "OUT-014", "OUT-015", "OUT-016", "OUT-017", "OUT-018",
    "APV-002", "APV-003", "APV-005", "APV-006", "APV-007", "APV-008", "APV-009", "APV-011", "APV-012", 
    "APV-013", "APV-014", "APV-016", "APV-017", "APV-018", "APV-019", "APV-020", "APV-021", "APV-022", 
    "APV-025", "APV-027", "APV-028", "APV-029",
    "CSV-002", "CSV-003", "CSV-004", "CSV-005", "CSV-006", "CSV-008", "CSV-009", "CSV-010", "CSV-011", 
    "CSV-012", "CSV-013", "CSV-014", "CSV-016", "CSV-017", "CSV-019", "CSV-021", "CSV-023", "CSV-025", 
    "CSV-027", "CSV-028", "CSV-030", "CSV-033", "CSV-035", "CSV-036", "CSV-037", "CSV-038", "CSV-042", 
    "CSV-043", "CSV-045", "CSV-046", "CSV-047", "CSV-048", "CSV-049", "CSV-050", "CSV-052", "CSV-053", 
    "CSV-054", "CSV-055", "CSV-056"
]


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
       time.sleep(50)

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
       time.sleep(50)

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



