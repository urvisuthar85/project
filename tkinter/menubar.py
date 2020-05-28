import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title('menubar')

def func():
    print('hello save')
'''
menubar = tk.Menu(win)

menubar.add_command(label = 'save',command = func)
menubar.add_command(label = 'saveas',command = func)
menubar.add_command(label = 'edit',command = func)
menubar.add_command(label = 'view',command = func)
menubar.add_command(label = 'help',command = func)
'''

main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu)

main_menu.add_cascade(label ='file',menu = file_menu)
file_menu.add_command(label ='sjlfd',command = func)
file_menu.add_command(label ='sjlfd',command = func)
file_menu.add_command(label ='sjlfd',command = func)
file_menu.add_command(label ='sjlfd',command = func)
win.config(menu = main_menu)


win.mainloop() 
