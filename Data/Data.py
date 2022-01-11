import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from Brand import Brand


class Data:
    def __init__(self, brand_list):
        self.__brand_list = brand_list
        self.__brands = []
        self.__models = []

    def get_data(self):
        self.__create_brands()
        self.__create_models()

    def __create_brands(self):
        for brand in self.__brand_list:
            self.__brands.append(Brand(brand, brand.lower))

    def __create_models(self):
        for brand in self.__brands:
            self.__models.append(brand.get_best_model())




page = requests.get("https://www.mgsm.pl/pl/katalog/samsung/galaxya52s5gdualsim/")
page
print(page.content)
print(type(page.content))
a = str(page.content)
f = open('file.txt', "wb")
f.write(page.content)
f.close()


page2 = requests.get("https://www.mgsm.pl/pl/katalog/huawei/p8lite/")
page2
print(page2.content)
print(type(page2.content))
a = str(page2.content)
f = open('file2.txt', "wb")
f.write(page2.content)
f.close()


class GetData:
    def __init__(self):
        pass
    def get(self):
        pass

class ParseData:
    def __init__(self):
        pass
    def read_date(self, id):
        soup = BeautifulSoup()
        soup.get_attribute_list(id)

