import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from Brand import Brand


class Data:
    def __init__(self, brand_list):
        self.__brand_list = brand_list
        self.__brands = []
        self.__models = []

    def download_data(self):
        self.__create_brands()
        self.__create_models()

    def __create_brands(self):
        for brand in self.__brand_list:
            self.__brands.append(Brand(brand, brand.lower))

    def __create_models(self):
        for brand in self.__brands:
            self.__models.append(brand.get_best_model())
