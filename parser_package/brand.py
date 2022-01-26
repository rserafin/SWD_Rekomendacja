import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from parser_package.model import Model


class Brand:
    def __init__(self, brand_name, models_name_raw=None):
        self.__brand_name = brand_name
        self.__brand_page = brand_name.lower()
        self.__model_list_raw = models_name_raw
        self.__brand_link = self.__get_link_brand()
        self.__models = []

    def create_models(self):
        models_links = self.__get_models_link()
        for model_link in models_links:
            self.__models.append(Model(model_link, self.__brand_name))

    def get_models_object(self):
        return self.__models

    def __get_link_brand(self):
        base_link = 'https://www.mgsm.pl/pl/katalog/'
        brand_link = '{}{}'.format(base_link, self.__brand_page)
        requests.get(brand_link)
        return brand_link

    def __get_models_link(self):
        model_links = []
        if self.__model_list_raw is not None:
            for model_raw in self.__model_list_raw:
                model_link = '{}{}{}'.format(self.__brand_link, '/', model_raw)
                model_links.append(model_link)
        else:
            requests.get(self.__brand_link)
        return model_links
