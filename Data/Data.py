import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup



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

class ParseData:
    def __init__(self):
        pass
    def read_date(self, id):
        soup = BeautifulSoup()
        soup.get_attribute_list(id)

