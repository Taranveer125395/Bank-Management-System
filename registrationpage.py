from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import subprocess

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '20Bcs@125395',
    database = 'Banking_Management_System'
)
cursor = conn.cursor()

def register_button():
    fullname = full_name_entry.get()
    username = username_entry.get()
    mobilenumber = mobile_number_entry.get()
    age1 = age_entry.get()
    qualification = qualification_entry.get()
    job = job_type_entry.get()
    password = password_type_entry.get()
    confirmpassword = confirm_password_type_entry.get()

    if not (fullname and 
            username and 
            mobilenumber and 
            age1 and 
            qualification and 
            job and 
            password and 
            confirmpassword):
        messagebox.showwarning(title = 'Error',
                               message = 'Enter Your Data Properly.')
        return

    if password != confirmpassword:
        messagebox.showwarning(title = 'Error',
                               message = 'Password and Confirm Password do not match.')
        return

    try:
        cursor.execute('''SELECT username FROM staff_registeration
                       WHERE username = %s''',
                       (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror(title = 'Error',
                                 message = 'Username already exists! Choose a different one.')
            cursor.close()
            conn.close()
            return

        insert_query = '''
        INSERT INTO staff_registeration (
            fullname, username, mobile_number, age, 
            education_qualification, job_type, password, 
            confirm_password
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''

        values = (fullname, username, mobilenumber,
                  age1, qualification, job, password,
                  confirmpassword)
        cursor.execute(insert_query, values)
        conn.commit()

        messagebox.showinfo(title = 'Success',
                            message = 'Data Successfully saved to Database!')

        full_name_entry.delete(0, END)
        username_entry.delete(0, END)
        mobile_number_entry.delete(0, END)
        age_entry.delete(0, END)
        qualification_entry.set('')
        job_type_entry.set('')
        password_type_entry.delete(0, END)
        confirm_password_type_entry.delete(0, END)

        cursor.close()
        conn.close()

        root.destroy()
        subprocess.run(['python', 'loginpage.py'])

    except pymysql.Error as err:
        messagebox.showerror(title = 'Database Error',
                             message = f'Error: {err}')

def backbutton():
    root.destroy()
    subprocess.run(['python', 'welcomepage.py'])

def mobile_number_validation(P):
    if P.isdigit() and len(P) <= 10:
        return True
    elif P == '':
        return True
    else:
        messagebox.showwarning(title = 'Error', 
                               message = 'Mobile number should be less than equal to 10')

def loginbutton():
    root.destroy()
    subprocess.run(['python', 'loginpage.py'])

root = Tk()
root.title('Staff Registration')

vcmd = root.register(mobile_number_validation)

heading = Label(root, 
                text = 'Online Banking System', 
                font = ('Arial', 16, 'bold'))
heading.grid(row = 0, 
             column = 0, 
             columnspan = 4, 
             pady = 10)

full_name = Label(root, 
                  text = 'Full Name',
                  font = ('Arial', 12, 'bold'))
full_name_entry = Entry(root,
                        font = ('Arial', 12))
full_name.grid(row = 1, 
               column = 0, 
               padx = 5, 
               pady = 2,
               sticky = 'e')
full_name_entry.grid(row = 1, 
                     column = 1, 
                     padx = 5, 
                     pady = 2,
                     sticky = 'w')

user_name = Label(root, 
                  text = 'Username',
                  font = ('Arial', 12, 'bold'))
username_entry = Entry(root,
                       font = ('Arial', 12))
user_name.grid(row = 1, 
               column = 2, 
               padx = 5, 
               pady = 2,
               sticky = 'e')
username_entry.grid(row = 1, 
                    column = 3, 
                    padx = 5, 
                    pady = 2,
                    sticky = 'w')

mobile_number = Label(root,
                      text = 'Mobile Number',
                      font = ('Arial', 12, 'bold'))
mobile_number_entry = Entry(root,
                            validate = 'key', 
                            validatecommand = (vcmd, '%P'),
                            font = ('Arial', 12))
mobile_number.grid(row = 2,
                   column = 0,
                   padx = 5,
                   pady = 2,
                   sticky = 'e')
mobile_number_entry.grid(row = 2,
                         column = 1,
                         padx = 5,
                         pady = 2,
                         sticky = 'w')

age = Label(root, 
            text = 'Age',
            font = ('Arial', 12, 'bold'))
age_entry = Spinbox(root, 
                    from_ = 18, 
                    to = 100,
                    font = ('Arial', 12))
age.grid(row = 2, 
         column = 2, 
         padx = 5, 
         pady = 2,
         sticky = 'e')
age_entry.grid(row = 2, 
               column = 3, 
               padx = 5, 
               pady = 2,
               sticky = 'w')

qualification_type = Label(root, 
                      text = 'Education Qualification',
                      font = ('Arial', 12, 'bold'))
qualification_entry = ttk.Combobox(root, 
                                   values = ['12th Pass', 
                                             'Diploma', 
                                             'Graduate', 
                                             'PG Diploma', 
                                             'PostGraduate'],
                                   font = ('Arial', 12))
qualification_type.grid(row = 3, 
                        column = 0, 
                        padx = 5, 
                        pady = 2,
                        sticky = 'e')
qualification_entry.grid(row = 3, 
                         column = 1, 
                         padx = 5, 
                         pady = 2,
                         sticky = 'w')

job_type = Label(root, 
                 text = 'Job Type',
                 font = ('Arial', 12, 'bold'))
job_type_entry = ttk.Combobox(root,
                              values = ['Customer Service Officer(CSO)',
                                        'Relationship Manager',
                                        'Teller',
                                        'Cashier',
                                        'Loan Officer',
                                        'Assistant Manager',
                                        'Bank Manager',],
                              font = ('Arial', 12))
job_type.grid(row = 3, 
              column = 2, 
              padx = 5, 
              pady = 2,
              sticky = 'e')
job_type_entry.grid(row = 3, 
                    column = 3, 
                    padx = 5, 
                    pady = 2,
                    sticky = 'w')

password_type = Label(root,
                      text = 'Password',
                      font = ('Arial', 12, 'bold'))
password_type_entry = Entry(root,
                            show = '*',
                            font = ('Arial', 12))
password_type.grid(row = 4,
                   column = 0,
                   padx = 5,
                   pady = 2,
                   sticky = 'e')
password_type_entry.grid(row = 4,
                         column = 1,
                         padx = 5,
                         pady = 2,
                         sticky = 'w')

confirm_password_type = Label(root,
                              text = 'Confirm Password',
                              font = ('Arial', 12, 'bold'))
confirm_password_type_entry = Entry(root,
                                    show = '*',
                                    font = ('Arial', 12))
confirm_password_type.grid(row = 4,
                           column = 2,
                           padx = 5,
                           pady = 2,
                           sticky = 'e')
confirm_password_type_entry.grid(row = 4,
                                 column = 3,
                                 padx = 5,
                                 pady = 2,
                                 sticky = 'w')

registration_button = Button(root, 
                             text = 'Register',
                             command = register_button,
                             font = ('Arial', 12, 'bold'))
registration_button.grid(row = 5, 
                         column = 0, 
                         columnspan = 2, 
                         pady = 10)

login_button = Button(root,
                      text = 'Login Here!',
                      font = ('Arial', 12, 'bold'),
                      command = loginbutton)
login_button.grid(row = 5,
                  column = 2,
                  pady = 10)

back_button = Button(root,
                     text = 'Go Back!',
                     font = ('Arial', 12, 'bold'),
                     command = backbutton)
back_button.grid(row = 5,
                 column = 3,
                 pady = 10,
                 padx = 20,
                 columnspan = 2)

root.mainloop()