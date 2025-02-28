from tkinter import *
from tkinter import messagebox
import subprocess

def login_button():
    root.destroy()
    subprocess.run(['python', 'loginpage.py'])

def registration_button():
    root.destroy()
    subprocess.run(['python', 'registrationpage.py'])

root = Tk()
root.title('Bank Management System - Dashboard')
root.geometry('1920x1080')

headerpoint = Frame(root, bg = 'lightpink', height = 50)
headerpoint.pack(fill = 'x')

loginbutton = Button(headerpoint, text = 'Login', command = login_button)
loginbutton.pack(side = 'right', padx = 5, pady = 5)

registrationbutton = Button(headerpoint, text = 'Registration', command = registration_button)
registrationbutton.pack(side = 'right', padx = 5, pady = 5)

root.mainloop()