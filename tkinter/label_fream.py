import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('LabelFream')

label_frame = ttk.LabelFrame(win,text = 'enter your details below')
label_frame.grid(row = 0,column = 0,padx = 10 )

labels = ['enter your name: ','enter your age: ','enter your gender: ','countery','city: ','state: ']
for i in range(len(labels)):
    current_label = 'label'+str(i)
    current_label = ttk.Label(label_frame,text = labels[i])
    current_label.grid(row = i,column = 0,sticky = tk.W)


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
    cur_entrybox = ttk.Entry(label_frame,width = 16,textvariable = user_info[i])
    cur_entrybox.grid(column = 1,row = counter,padx = 0,pady = 0)
    counter+=1



def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())
submit_btn = ttk.Button(win,text = 'submit', command = submit)
submit_btn.grid(row = 1,columnspan = 2)


for child in label_frame.winfo_children():
    child.grid_configure(padx = 4,pady = 4)

win.mainloop()