import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from Model import Model


class Brand:
    def __init__(self, brand_name, brand_page):
        self.__brand_name = brand_name
        self.__brand_page = brand_page
        self.__brand_link = self.__get_link_brand()

    def get_best_model(self):
        models = []
        models_links = self.__get_models_link()
        for model_link in models_links:
            models.append(Model(model_link))
        return models

    def __get_link_brand(self):
        base_link = 'https://www.mgsm.pl/pl/katalog/'
        brand_link = '{}{}'.format(base_link, self.__brand_page)
        requests.get(brand_link)
        return brand_link

    def __get_models_link(self):
        models_links = []
        brand_page = requests.get(self.__brand_link)
        # to do
        return models_links
