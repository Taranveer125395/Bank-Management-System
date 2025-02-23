from tkinter import *

root = Tk()
root.title('Dashboard')
root.geometry('400x250')

text = Label(root,
             text = '''Welcome to Dashboard!, 
             You are successfully registered and login.''')
text.pack(padx = 5, pady = 50)

root.mainloop()