from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess

def forregistration():
    root.destroy()
    subprocess.run(['python', 'registrationpage.py'])

def loginbutton():
    username = entry1.get()
    password = entry2.get()
    
    if username and password:
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='20Bcs@125395',
                database='Banking_Management_System'
            )

            cursor = conn.cursor()

            query = "SELECT * FROM staff_login WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo(title='Login Successful',
                                    message='Welcome to the Banking Management System!')
            else:
                messagebox.showwarning(title='Login Failed',
                                       message='Invalid Username or Password')

            cursor.close()
            conn.close()
            entry1.delete(0, END)
            entry2.delete(0, END)
            root.destroy()
            subprocess(['python', 'dashboard.py'])

        except mysql.connector.Error as err:
            messagebox.showerror(title='Database Error',
                                 message=f'Error: {err}')
    else:
        messagebox.showwarning(title='Warning',
                               message='Enter Your Details')

root = Tk()
root.title('Staff Login')
root.geometry('300x150')

heading = Label(root,
                text = 'Bank Management System',
                font = ('Arial', 12, 'bold'))
heading.grid(row = 0,
             column = 0,
             columnspan = 2,
             pady = 10)

username_type = Label(root,
                      text = 'Username')
entry1 = Entry(root)
username_type.grid(row = 1,
                   column = 0,
                   padx = 5,
                   pady = 2,
                   sticky = 'e')
entry1.grid(row = 1,
            column = 1,
            padx = 5,
            pady = 2)

password_type = Label(root,
                      text = 'Password')
entry2 = Entry(root,
               show = '*')
password_type.grid(row = 2,
                   column = 0,
                   padx = 5,
                   pady = 2,
                   sticky = 'e')
entry2.grid(row = 2,
            column = 1,
            padx = 5,
            pady = 2)

login_button = Button(root,
                      text = 'Login',
                      command = loginbutton)
login_button.grid(row = 3,
                  column = 0,
                  pady = 10)

registration_button = Button(root,
                             text = 'For Registration',
                             command = forregistration)
registration_button.grid(row = 3,
                         column = 1,
                         pady = 10)

root.mainloop()