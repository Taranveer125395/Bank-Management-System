from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '20Bcs@125395',
    database = 'Banking_Management_System'
)
cursor = conn.cursor()

def forregistration():
    root.destroy()
    subprocess.run(['python', 'registrationpage.py'])

def loginbutton():
    username = entry1.get()
    password = entry2.get()
    
    if username and password:
        try:
            query_check = '''SELECT * FROM staff_registeration
                             WHERE username = %s AND 
                             password = %s'''
            cursor.execute(query_check, (username, password))
            registered_user = cursor.fetchone()

            if not registered_user:
                messagebox.showwarning(title = 'Login Failed',
                                       message = 'Invalid Username or Password. Please register first.')
                cursor.close()
                conn.close()
                entry1.delete(0, END)
                entry2.delete(0, END)
                return

            messagebox.showinfo(title = 'Login Successful',
                                message = f'Welcome {username}!')

            cursor.close()
            conn.close()

            root.destroy()
            subprocess.run(['python', 'dashboard.py'])

        except mysql.connector.Error as err:
            messagebox.showerror(title = 'Database Error',
                                 message = f'Error: {err}')
    else:
        messagebox.showwarning(title = 'Warning',
                               message = 'Enter Your Details')

root = Tk()
root.title('Staff Login')
root.geometry('300x200')

heading = Label(root,
                text = 'Online Banking System',
                font = ('Arial', 16, 'bold'))
heading.grid(row = 0,
             column = 0,
             columnspan = 2,
             pady = 10)

username_type = Label(root,
                      text = 'Username',
                      font = ('Arial', 12, 'bold'))
entry1 = Entry(root,
               font = ('Arial', 12))
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
                      text = 'Password',
                      font = ('Arial', 12, 'bold'))
entry2 = Entry(root,
               show='*',
               font = ('Arial', 12))
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
                      command = loginbutton,
                      font = ('Arial', 12, 'bold'))
login_button.grid(row = 3,
                  column = 0,
                  pady = 10)

registration_button = Button(root,
                             text = 'For Registration',
                             command = forregistration,
                             font = ('Arial', 12, 'bold'))
registration_button.grid(row = 3,
                         column = 1,
                         pady = 10)

root.mainloop()