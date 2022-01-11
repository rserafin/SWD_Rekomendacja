import tkinter as tk
import pandas as pd
import random
from PIL import Image,ImageTk

screen_size = '500x400'
window = tk.Tk()
window.geometry(screen_size)
window.resizable(False, False)


#TESTY
data_base = pd.read_csv("mobile.csv", low_memory = False, encoding="ISO-8859-1")
pd.set_option('max_columns', None)
#print(len(data_base[5:172]))
test_reko = pd.DataFrame(columns= ['Brand', 'Phone'])
nr = []
for i in range(3):
    nr.append(random.randint(5, 172))
    test_reko2 = data_base[nr[i]:nr[i]+1][['Brand', 'Phone']]
    test_reko = pd.concat([test_reko, test_reko2], ignore_index = True, axis = 0)
    #print(nr)
    #print(data_base[nr:nr+1][['Brand', 'Phone']])
print(test_reko)


def reko_random():
    new_window = tk.Toplevel(window)
    new_window.geometry(screen_size)
    new_window.resizable(False, False)
    q_button = tk.Button(new_window, text= 'Wyjscie', command= new_window.destroy)
    q_button.pack(side= 'bottom')
    test_text = tk.Text(new_window)
    test_text.pack()
    test_text.insert('end', test_reko)

def reko_content():
    new_window = tk.Toplevel(window)
    new_window.geometry(screen_size)
    new_window.resizable(False, False)
    q_button = tk.Button(new_window, text= 'Wyjscie', command= new_window.destroy)
    q_button.pack(side= 'bottom')

def reko_collab():
    new_window = tk.Toplevel(window)
    new_window.geometry(screen_size)
    new_window.resizable(False, False)
    q_button = tk.Button(new_window, text= 'Wyjscie', command= new_window.destroy)
    q_button.pack(side= 'bottom')

def rekomenduj():
    wybor = var.get()
    if wybor == 'random':
        reko_random()
    if wybor == 'content':
        reko_content()
    if wybor == 'collaborative':
        reko_collab()

users = pd.read_csv('user.csv')
users_list = users['Username'].to_list()
image_file = Image.open('tlo.png')
bg_image = ImageTk.PhotoImage(image_file)
bg_label = tk.Label(window, image= bg_image)
bg_label.place(x = 0, y= 0)
name = tk.Label(window, text='System rekomendacji')
q_button = tk.Button(window, text= 'Wyjscie', command= quit)
load_button = tk.Button(window, text= 'Wczytaj', command= None)
reco_button = tk.Button(window, text= 'Rekomenduj!', command= rekomenduj)
user_button = tk.Button(window, text= 'Zmien uzytkownika', command= None)

option = ['content', 'collaborative', 'random']
var = tk.StringVar()
var.set(option[0])
b_option = tk.OptionMenu(window, var, *option)
name.pack()

reco_button.place(x = 125, y = 55, width = 250, height = 75)
b_option.place(x = 175, y = 135, width = 150, height = 50)
user_button.place(x = 175, y = 190, width = 150, height = 50)
load_button.place(x = 175, y = 245, width = 150, height = 50)
q_button.place(x = 175, y = 300, width = 150, height = 50)



window.mainloop()