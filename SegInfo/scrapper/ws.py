from bs4 import BeautifulSoup

import requests

site = requests.get("https://climatempo.com.br/").content
#objeto recebendo o conteúdo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando o site html
#print(soup.prettify())
#transforma o html em string e o print vai exibir o html

print(soup.title.string)
