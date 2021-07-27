from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import os
clear = lambda: os.system('cls')

# Links do site
tags = []

site = "https://google.com/"

# 
file_classic = open(r".\classic.txt", 'r', encoding='utf8')
lista_classic = file_classic.readlines()
classic = [s.replace("\n", "") for s in lista_classic]

file_mobile = open(r".\mobile.txt", 'r', encoding='utf8')
lista_mobile = file_mobile.readlines()
mobile = [s.replace("\n", "") for s in lista_mobile]

file_tablet = open(r".tablet.txt", 'r', encoding='utf8')
lista_tablet = file_tablet.readlines()
tablet = [s.replace("\n", "") for s in lista_tablet]

clear()

def acesso(agent):
    global driver
    global profile
    global ua
    options = Options()
    options.add_argument(f'user-agent={agent}')
    options.add_argument("--headless")
    
    driver = webdriver.Chrome(executable_path=r".\chromedriver.exe",options=options)
    ua = driver.execute_script("return navigator.userAgent;")
    print("Abrindo o site...")
    driver.get(site)
    #driver.maximize_window()
    #sleep(3)
    print(driver.execute_script("return navigator.userAgent;"))
    sleep(1)
    driver.close()
    # scroll()

# Função que rola a página
def scroll():
    print(driver.current_url)
    driver.find_element_by_tag_name("body").click()
    print("\nRolando a tela...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")
    url()

# Função que rola a página e espera para o próximo acesso
def scroll_final():
    print(driver.current_url)
    driver.find_element_by_tag_name("body").click()
    print("Rolando a tela...\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")

    print("Esperando 35 segundos para fechar os navegadores...\n")
    sleep(3)
    print(ua)
    driver.quit()
    sleep(3)

# Acessa 2 páginas no site 
def url():
    url.counter += 1
    print("Esperando 20 segundos...")
    sleep(3)
    print("\nAcessando um link...")
    sleep(3)
    driver.get(random.choice(tags))
    sleep(5)

    while url.counter < 2:
        scroll()
    else:
        scroll_final()


# Contadores 
def mobilef():
    mobilef.counter += 1
    print("Total de mobiles: {}".format(mobilef.counter))

def classicf():
    classicf.counter += 1
    print("Total de destkops: {}".format(classicf.counter))

def tabletf():
    tabletf.counter += 1
    print("Total de tablets: {}".format(tabletf.counter))

url.counter = 0

mobilef.counter = 0
classicf.counter = 0
tabletf.counter = 0


while True:
    acesso(random.choice(mobile))
    mobilef()

    if mobilef.counter == 10:
        acesso(random.choice(classic))
        classicf()

    if mobilef.counter == 50:
        acesso(random.choice(tablet))
        tabletf()

        mobilef.counter = 0
        classicf.counter = 0
        tabletf.counter = 0