from bs4 import BeautifulSoup
import html5lib


def getEmail(html):
    urls = []
    soup = BeautifulSoup(html, 'html5lib')
    #recuper tout les title de h1

    #Recuper tout les lien dans la page


    #verifier si @ est dans le lien si oui ont en registres sa dans json sinon on rourner tout les 
    return urls