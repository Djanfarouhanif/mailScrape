from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import requests
from data import getEmail





# Configuration de Selenium pour Edge
def seleniumN():
    edge_options = Options()
    edge_options.add_argument("--headless") # Ecécuter en mode headless (sans interface graphique)
    service = Service()
    driver = webdriver.Edge(service=service, options=edge_options)

    # Accéder à une page web
    driver.get('https://bloggerspassion.com/contact/')

    # Attendre que la page soit complètement chargée
    time.sleep(5)

    #Extraire le html de la page
    html = driver.page_source
    print(html)
    #Pour quitter la page
    driver.quit()

    return html

seleniumN()

def requestsExecute(url):
    #Verifiier s'il y'a plusieur url ou non
    urls_s = []
    if len(urls) == 0:
        response = requests.get(url)
        html = response.text

        url = getEmail(html)

    else:
        for url in urls:
            response = requests.get(url)

            #recuperer la page html
            html = response.text
  
            #Recuper les email
            urls = getEmail(html)
            for i in urls:
                urls_s.append(i)

            
#Utiliser BeautifulSoup pour analyser le HTML

