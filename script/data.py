from bs4 import BeautifulSoup
import html5lib
from urllib.parse import urljoin

url = "https://bloggerspassion.com/contact/"
def getEmail(html):
    urls = []
    soup = BeautifulSoup(html, 'html5lib')
    #recuper tout les title de h1

    #Recuper tout les lien dans la page
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        link_text = link.get_text()
        if href:
            full_url = urljoin(url, href)
            if '@' in link_text:
                print(link_text)
            else:
                urls.append(full_url)

    #verifier si @ est dans le lien si oui ont en registres sa dans json sinon on rourner tout les 
    return urls


getEmail(url)