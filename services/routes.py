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
        price = models.find('h4', {'class': 'pull-right price'})
        description = models.find('p', {'class': 'description'})
        if "Lenovo" in description.get_text():
            aux = description.get_text()
            name_and_description = aux.split(sep=',')
            price = price.get_text()
            lenovo = Laptop(model=name_and_description[0],
                            price=price,
                            screen=name_and_description[1],
                            processor=name_and_description[2],
                            ram=name_and_description[3],
                            storage=name_and_description[4],
                            os=name_and_description[5])
            lenovo_models += [lenovo.__dict__]

    return json.dumps(lenovo_models)

