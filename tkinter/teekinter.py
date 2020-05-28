import tkinter as tk
from tkinter import ttk
from csv import DictWriter

win = tk.Tk()
win.title('win page')

name_label = ttk.Label(win,text = "ENTER NAME HERE :")
name_label.grid(row = 0,column = 0,sticky = tk.W)

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win , width = 16 , textvariable = name_var)
name_entrybox.grid(row = 0,column = 1)
name_entrybox.focus()

email_label = ttk.Label(win,text = 'ENTER EMAIL ADDRESS :')
email_label.grid(row = 1,column = 0,sticky = tk.W)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win , width = 16 , textvariable = email_var)
email_entrybox.grid(row = 1,column = 1)

age_label = ttk.Label(win , text = 'ENTER YOUR AGE :')
age_label.grid(row = 2,column = 0,sticky = tk.W)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win , width = 16 , textvariable = age_var)
age_entrybox.grid(row = 2,column = 1)

gender_label = ttk.Label(win, text = 'CHOOES GENDER :')
gender_label.grid(row = 3,column = 0,sticky = tk.W)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width = 13, textvariable  = gender_var,state = 'readonly')
gender_combobox['values']  =('male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row = 3 , column = 1)

usertype = tk.StringVar()
radio_button = ttk.Radiobutton(win, text = "student",value = "student" , variable = usertype)
radio_button.grid(row = 4 , column = 0)

radio_button = ttk.Radiobutton(win, text = 'teacher', value = 'teacher', variable = usertype)
radio_button.grid(row = 4,column = 1)


checkbutton_var = tk.StringVar()
check_button = ttk.Checkbutton(win,text = 'do you have subscribe it ......???',variable = checkbutton_var)
check_button.grid(row = 5,columnspan = 3,sticky = tk.W)
'''
with open('file.csv','a') as f:
    dict_writer = DictWriter(f, fieldnames = ['username','userage','useremail','gender','choise','subcribed'])
    dict_writer.writeheader()
    dict_writer.writerow()
   ''' 
def action():
    username = name_var.get()
    email = email_var.get()
    userage = age_var.get()
    #print(f"username {username} and age {userage} and email {email}")
    genderbtn = gender_var.get()
    radiobtn = usertype.get()
    if checkbutton_var == 0:
        print('no information here')
    else:
        print(f'{radiobtn} and {genderbtn}  subscribd')


    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)

    """with open('firl.txt','a') as f:
        f.write(f"{username} , {userage} , {email}, {radiobtn} , {genderbtn} , {checkbutton_var} \n")
    
    name_label.configure(foreground = '#b388ff')

    submit_button.configure(foreground = 'Blue')"""
    with open('firl.csv','a') as f:
        dict_writer = DictWriter(f, fieldnames = ['username', 'userage','email','field', 'gender','subscripation'])

        dict_writer.writeheader()
        dict_writer.writerow( {
            'username': username,
            'userage': userage,
            'email' : email,
            'field' : radiobtn,
            'gender' : genderbtn,
            #'subscripation' : checkbutton_var,
        } )
submit_button = tk.Button(win, text = 'submit',command = action)
submit_button.grid(row =7,column = 0)


win.mainloop()  
