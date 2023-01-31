import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "https://lista.mercadolivre.com.br/" + input("Digite o nome do produto que deseja buscar: ").replace(" ", "-")

print(url)
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

products = soup.find_all("li", class_="ui-search-layout__item shops__layout-item")
x = PrettyTable(["Nome", "Preço"])
for product in products:
    name = product.find("h2").text
    price = product.find("span", class_="price-tag-fraction").text
    link = product.find("a")["href"]
    x.add_row([name, price])

print(x)
