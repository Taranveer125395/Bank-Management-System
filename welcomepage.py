from tkinter import *
import subprocess

def login():
    root.destroy()
    subprocess.run(['python', 'loginpage.py'])

def registration():
    root.destroy()
    subprocess.run(['python', 'registrationpage.py'])

root = Tk()
root.title('Welcome')
root.geometry('1920x1080')
root.configure(bg = '#f0f0f0')

title = Label(root,
              text = 'Welcome to Our System',
              font = ('Arial', 14, 'bold'),
              bg = '#f0f0f0')
title.pack(pady = 20)

label =Label(root,
             text = 'You have to choose out of Login and Registration to start your work.',
             fg = 'blue',
             font = ('Arial', 13, 'bold'))
label.pack(pady = 10)

loginbutton = Button(root,
                     text = 'Login',
                     font = ('Arial', 12, 'bold'),
                     width = 15,
                     command = login,
                     bg = 'lightgrey',
                     fg = 'black')
loginbutton.pack(pady = 10)

registrationbutton = Button(root,
                            text = 'Registration',
                            font = ('Arial', 12, 'bold'),
                            width = 15,
                            command = registration,
                            bg = 'lightgrey',
                            fg = 'black')
registrationbutton.pack(pady = 10)

root.mainloop()