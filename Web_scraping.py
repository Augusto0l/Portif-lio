import requests
from bs4 import BeautifulSoup

# URL da página principal do G1
url = "https://g1.globo.com/"

# Enviar uma requisição HTTP para o site
resposta = requests.get(url)

# Criar um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# Encontrar todos os elementos que contêm os títulos das notícias
# No G1, os títulos principais estão dentro de tags <a> com a classe 'feed-post-link'
noticias = soup.find_all("a", class_="feed-post-link")

# Exibir os títulos das notícias
for i, noticia in enumerate(noticias, start=1):
    print(f"{i}. {noticia.text.strip()}")
