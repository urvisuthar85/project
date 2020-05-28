import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('win')

name_label = ttk.Label(win,text = 'rtftmvkv;evm,d.mcdf')
name_label.grid(row = 1,column = 0,sticky = tk.W)

labels = ['username :', 'userage :','usergender :','country :','state :','city :']

for i in range(len(labels)):
    current_label = 'label' + str(i)
    current_label = ttk.Label(win,text = labels[i])
    current_label.grid(row = i,column = 0 ,sticky = tk.W)


name_var = tk.StringVar()
user_info = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'country' : tk.StringVar(),
    'state' : tk.StringVar(),
    'city' : tk.StringVar(),
}


counter = 0
for i in user_info:
    cur_entrybox = 'entry'+i
    cur_entrybox = ttk.Entry(win,width = 16,textvariable = user_info[i])
    cur_entrybox.grid(column = 1,row = counter,padx = 2,pady = 2)
    counter+=1


def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())
submit_btn = ttk.Button(win,text = 'submit', command = submit)
submit_btn.grid(row = 6,columnspan = 2)

win.mainloop()

