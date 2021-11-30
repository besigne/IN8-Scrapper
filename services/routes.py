import json
import requests
from bs4 import BeautifulSoup
from model.laptop import Laptop


def index():
    page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    soup = BeautifulSoup(page.text, "html.parser")

    all_thumbnails = soup.find_all('div', {'class': 'thumbnail'})

    lenovo_models = []

    for models in all_thumbnails:

        description = models.find('p', {'class': 'description'})
        product = models.find('a', {'class': 'title'})

        if "Lenovo" in description.get_text():

            url_single_lenovo = requests.get("https://webscraper.io/" + product['href'])
            lenovo_soup = BeautifulSoup(url_single_lenovo.text, "html.parser")
            trial = lenovo_soup.find_all('div', {'class': 'col-lg-10'})
            lenovo_description = lenovo_soup.find('p', {'class': 'description'})
            lenovo_description = lenovo_description.get_text()
            storages = lenovo_soup.find('div', {'class': 'swatches'})
            price = lenovo_soup.find('h4', {'class': 'pull-right price'})
            price = price.get_text()
            price = price.replace('$', '')

            values_storages = []
            add = 0
            for storage in storages:
                if storage.get_text() != "\n":
                    price = float(price)
                    price += add
                    values_storages += [[storage.get_text()] + ['$' + str(price)]]
                    add = 20

            product = product.get_text()
            product = product.replace('...', '')
            notebook_lenovo = Laptop(
                name=product,
                model=values_storages,
                description=lenovo_description
            )

            lenovo_models += [notebook_lenovo.__dict__]

    return json.dumps(lenovo_models)

