import requests
from bs4 import BeautifulSoup

# Obtém o conteúdo da página com as informações dos estados brasileiros
url = "https://www.estadosecapitaisdobrasil.com/"
resposta = requests.get(url)
html = resposta.content

# Cria um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontra todas as divs que contêm as informações dos estados
estados_divs = soup.find_all('div', {'class': 'estado'})

# Cria uma lista com as siglas das unidades federativas
ufs = [div.find('span', {'class': 'sigla'}).text for div in estados_divs]

# Cria uma lista com os nomes dos estados
nomes_estados = [div.find('h2').text for div in estados_divs]

# Exibe as bandeiras dos estados
for uf, nome_estado in zip(ufs, nomes_estados):
    # Obtém o link da imagem da bandeira
    url_imagem = f"https://www.estadosecapitaisdobrasil.com/wp-content/uploads/estados/uf-{uf}.png"
    
    # Cria a tag HTML para exibir a bandeira e o nome do estado
    tag_html = f"<div><img src='{url_imagem}' width='80' height='80'><br>{nome_estado}</div>"
    
    # Imprime a tag HTML
    print(tag_html)
