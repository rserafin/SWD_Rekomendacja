import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from parser_package.brand import Brand


class Data:
    def __init__(self, brand_list, models_name_raw=None):
        self.__brand_list = brand_list
        self.__models_data_raw = models_name_raw
        self.__brands = []

    def download_data(self):
        self.__create_brands()
        self.__create_models()

    def get_all_data(self):
        data_base = {}
        for brand in self.__brands:
            for model in brand.get_models_object():
                model.read_data()
                data_base[model.get_full_name()] = model.get_data()
        return data_base

    def __create_brands(self):
        if self.__models_data_raw is not None:
            for brand in self.__brand_list:
                if brand in self.__models_data_raw:
                    self.__brands.append(Brand(brand, self.__models_data_raw[brand]))
                else:
                    self.__brands.append(Brand(brand))
        else:
            for brand in self.__brand_list:
                self.__brands.append(Brand(brand))

    def __create_models(self):
        for brand in self.__brands:
            brand.create_models()
