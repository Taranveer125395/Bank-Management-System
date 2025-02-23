from tkinter import *
import subprocess

def login():
    root.destroy()
    subprocess.run(['python', 'loginpage.py'])

def registration():
    root.destroy()
    subprocess.run(['python', 'registrationpage.py'])

root = Tk()
root.title("Welcome")
root.geometry("400x250")
root.configure(bg = "#f0f0f0")

title = Label(root,
              text = 'Welcome to Our System',
              font = ('Arial', 14, 'bold'),
              bg = "#f0f0f0")
title.pack(pady = 20)

loginbutton = Button(root,
                     text = 'Login',
                     font = ('Arial', 12),
                     width = 15,
                     command = login,
                     bg="#4CAF50",
                     fg="white")
loginbutton.pack(pady = 10)

registrationbutton = Button(root,
                            text = 'Registration',
                            font = ('Arial', 12),
                            width = 15,
                            command = registration,
                            bg="#008CBA",
                            fg="white")
registrationbutton.pack(pady = 10)

root.mainloop()