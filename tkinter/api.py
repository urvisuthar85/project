import tkinter as tk
from tkinter import ttk
import requests
import json
from pprint import pprint
win = tk.Tk()
win.title('winpage')


name_label = ttk.Label(win,text = "ENTER MOVIE NAME HERE :")
name_label.grid(row = 0,column = 0,sticky = tk.W)

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win , width = 16 , textvariable = name_var)
name_entrybox.grid(row = 0,column = 1)

def action():
    u_name = name_var.get()
    url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query="
    s = "&api-key="
    key = "xSic6aps1SkzhqBL06rQLbCNVDdGGW7v"
    act_urls = url+u_name+s+key
    #print(act_urls)
    data = requests.get(act_urls)
    data = data.json()
    pprint(data)



name_entrybox.delete(0,tk.END)
"""with open('firl1.txt','a') as f:
    f.write()"""

submit_button = tk.Button(win, text = 'submit',command = action)
submit_button.grid(row =7,column = 0)
win.mainloop()