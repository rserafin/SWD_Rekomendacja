import tkinter as tk
from tkinter.constants import FALSE
import pandas as pd
import tkinter.filedialog as fd
import random
from PIL import Image,ImageTk
from pandas._libs.tslibs.timestamps import Timestamp

from settings import Settings
from metods import *

class PhoneRecomender(tk.Tk):
    """Klasa przedstawiajaca program"""
    def __init__(self):
        """Inicjalizacja glownego ekranu i jego elementow"""
        super().__init__()

        self.settings = Settings()
        self.geometry(self.settings.screensize)
        self.resizable(self.settings.resize[0], self.settings.resize[1])
        self.title(self.settings.window_title)
        self.image_file = Image.open(self.settings.bg_name)

        #tlo
        self.bg_image = ImageTk.PhotoImage(self.image_file)
        self.bg_label = tk.Label(self, image= self.bg_image)
        self.bg_label.place(x= 0, y= 0)

        #bazy danych
        self.user_list = pd.read_csv(self.settings.user_list_filename)
        self.database = None    # miejsce na zapis wczytanej bazy danych
        self.random_db = pd.DataFrame(columns= self.settings.columns)
        self.simple_content_db = pd.DataFrame(columns= self.settings.columns)

        #przycisk do rekomendacji
        self.recommend_button = tk.Button(self, text= 'Rekomneduj!')
        self.recommend_button['command'] = self.recommend
        self.recommend_button.place(x= 150, y= 200, width= self.settings.button_weight, height= self.settings.button_height)

        #przycisk do wczytania bazy
        self.read_button = tk.Button(self, text= 'Wczytaj baze')
        self.read_button['command'] = self.read_database
        self.read_button.place(x= 150, y= 240, width= self.settings.button_weight, height= self.settings.button_height)

        #przycisk zmiany uzytkownika
        self.user_button = tk.Button(self, text= 'Zmien uzytkownika')
        self.user_button['command'] = self.change_user
        self.user_button.place(x= 150, y= 280, width= self.settings.button_weight, height= self.settings.button_height)

        #przycisk wyjscia
        self.quit_button = tk.Button(self, text= 'Wyjscie')
        self.quit_button['command'] = quit
        self.quit_button.place(x= 150, y= 320, width= self.settings.button_weight, height= self.settings.button_height)

        #informacja o wczytanej bazie danych
        self.db_info_text = tk.StringVar()
        self.db_info_text.set('Nie wczytano bazy dancyh.')
        self.db_info = tk.Label(self, textvariable= self.db_info_text)
        self.db_info.pack(ipady= 10, side= 'bottom', fill='x')

        #informacja o uzytkowniku
        self.user_name = ''
        self.user_list = pd.read_csv(self.settings.user_list_filename)
        self.user_text = tk.StringVar()
        self.user_text.set(f'Witaj {self.user_name}!')
        self.user_label = tk.Label(self, textvariable= self.user_text)
        self.user_label.place(x= 150, y= 180, width= self.settings.button_weight, height= 20)

    def read_database(self):
        """Funkcja wczytuje gotowa baze danych"""
        filetypes = (('csv files', '*.csv'),)
        filename = fd.askopenfilename(filetypes= filetypes)
        if filename:
            self.database = pd.read_csv(filename, low_memory = False, encoding="ISO-8859-1")
            tekst = f'Wczytano baze danych. Liczy ona {len(self.database)} pozycji.'
            self.db_info_text.set(tekst)

    def recommend(self):
        """Funkcja do utworzenia rekomendacji i ich wyswietlenie w nowym oknie"""
        new_window = tk.Toplevel(self)

        self.random_db = random_reco(self.database, self.settings.columns)
        self.simple_content_db = simple_reco(self.database, self.settings.columns)
        #print(self.random_db)

        #losowa rekomendacja
        random_label = tk.Label(new_window, text= 'Losowa rekomendacja')
        random_label.pack(side= 'top', fill= 'x')
        random_disp = tk.Text(new_window, height= 4)
        random_disp.insert('end', self.random_db[self.settings.columns])
        random_disp.pack(side= 'top', fill= 'x')

        #prosta content
        simple_label = tk.Label(new_window, text= 'Prosta content rekomendacja')
        simple_label.pack(side= 'top', fill= 'x')
        simple_disp = tk.Text(new_window, height= 4)
        simple_disp.insert('end', self.simple_content_db[self.settings.columns])
        simple_disp.pack(side= 'top', fill= 'x')

        q_button = tk.Button(new_window, text= 'Wyjscie', command= new_window.destroy)
        q_button.pack(side= 'bottom', fill= 'x')


    def change_user(self):
        """Funkcja sluzaca do wyswietlania okna zmiany uzytkokwnika"""
        new_window = tk.Toplevel(self)
        new_window.resizable(False, False)

        temp_user_name = tk.StringVar()
        user_list_list = self.user_list['Username'].tolist()
        temp_user_name.set(user_list_list[0])

        user_option = tk.OptionMenu(new_window, temp_user_name, *user_list_list)
        user_option.pack(side= 'top', fill='x')
        ok_button = tk.Button(new_window, text= 'OK')
        q_button = tk.Button(new_window, text= 'Wyjscie', command= new_window.destroy)
        q_button.pack(side= 'bottom', fill='x')
        ok_button['command'] = lambda: self.user_update(temp_user_name.get())
        ok_button.pack(side= 'bottom', fill='x')

    def user_update(self, name):
        """Funkcja do zatwierdzania zmiany uxytkownika"""
        self.user_name = name
        self.user_text.set(f'Witaj {self.user_name}!')

if __name__ == '__main__':
    pr = PhoneRecomender()
    pr.mainloop()