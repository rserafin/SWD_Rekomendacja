class Settings():
    
    def __init__(self) -> None:
        #Ustawienia ekranu
        self.weight = 500
        self.height = 400
        self.resize = (False, False)
        self.screensize = f'{self.weight}x{self.height}'
        self.window_title = f'Phone Recomender'
        self.bg_name = f'bg.png'
        #Ustawienia przyciskow
        self.button_weight = 200
        self.button_height = 40
        #Ustawienia baz
        self.columns = ['Brand', 'Phone', 'Price']
        #Ustawienia bazy uzytkownikow
        self.user_list_filename = 'tests.csv'




