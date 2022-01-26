import requests
from bs4 import BeautifulSoup


class Model:
    def __init__(self, model_link, brand):
        self.__model_link = model_link
        self.__brand = brand
        self.__model_data = {}

    def read_data(self):
        raw_data = requests.get(self.__model_link)
        soup = BeautifulSoup(raw_data.content, 'html.parser')
        # brand
        self.__model_data['brand'] = self.__brand
        # model
        model = soup.find_all('b', {'itemprop': 'brand'})[1].get_text()
        self.__model_data['model'] = self.__change_string(model)
        # rating
        rating = soup.find_all('span', {'itemprop': 'ratingValue'})[0].get_text()
        rating = rating.replace(',', '.')
        self.__model_data['rating'] = float(rating)
        # tr object
        tr_object = soup.find_all('tr')
        # standards
        standards = self.__tr_searcher(tr_object, 'Standardy')
        standards = standards.find_all('td', {'class': 'phoneCategoryValue noDict'})[0].get_text()
        self.__model_data['standards'] = self.__change_string(standards)
        # weight
        weight = self.__tr_searcher(tr_object, 'Waga')
        weight = weight.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['weight'] = self.__change_string(weight)
        # screen
        screen = self.__tr_searcher(tr_object, 'Wyświetlacz')
        screen = screen.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['screen'] = self.__change_string(screen)
        # battery
        battery = self.__tr_searcher(tr_object, 'Standardowa bateria')
        battery = battery.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['battery'] = self.__change_string(battery)
        # charging
        charging = self.__tr_searcher(tr_object, 'Szybkie ładowanie')
        charging = charging.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['charging']= self.__change_string(charging)
        # memory
        memory = self.__tr_searcher(tr_object, 'Pamięć wbudowana')
        memory = memory.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['memory'] = self.__change_string(memory)
        # memory RAM
        memory_RAM = self.__tr_searcher(tr_object, 'Pamięć RAM')
        memory_RAM = memory_RAM.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['memory_RAM'] = self.__change_string(memory_RAM)
        # system
        system = self.__tr_searcher(tr_object, 'System operacyjny')
        system = system.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['system'] = self.__change_string(system)
        # processor
        processor = self.__tr_searcher(tr_object, 'Procesor')
        processor = processor.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['processor'] = self.__change_string(processor)
        # on market
        on_market = self.__tr_searcher(tr_object, 'Wprowadzony na rynek')
        on_market = on_market.find_all('td', {'class': 'phoneCategoryValue'})[0].get_text()
        self.__model_data['on_market'] = self.__change_string(on_market)

    def get_data(self):
        return self.__model_data

    def get_full_name(self):
        return '{} {}'.format(self.__brand, self.__model_data['model'])

    @staticmethod
    def __change_string(raw_string):
        raw_string = raw_string.replace('\n', '')
        raw_string = raw_string.replace('\t', '')
        raw_string = raw_string.replace('czytaj więcej', '')
        raw_string = raw_string.replace('\xa0', ' ')

        return raw_string

    @staticmethod
    def __tr_searcher(tr_object, parameter):
        for tr in tr_object:
            if parameter in tr.text:
                return tr
