from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '20Bcs@125395',
    database = 'Banking_Management_System'
)
cursor = conn.cursor()

def show_frame(frame):
    frame.tkraise()

def homebutton():
    show_frame(homeframe)

def createaccount():
    show_frame(accountframe)

def gst_entry(event = None):
    if accounttypeentry.get() == 'Current':
        gstnumber.grid(row = 6,
                       column = 6,
                       padx = 5,
                       pady = 5,
                       sticky = 'e')
        gstnumberentry.grid(row = 6,
                            column = 7,
                            padx = 5,
                            pady = 5,
                            sticky = 'w')
    else:
        gstnumber.grid_remove()
        gstnumberentry.grid_remove()

def account_button():
    try:
        name = name1entry.get()
        age = age2entry.get()
        mobile_number = mobilenumber1entry.get()
        day = selected_day.get()
        month = selected_month.get()
        year = selected_year.get()
        if day == 'Day' or month == 'Month' or year == 'Year':
            date_of_birth = None
        else:
            date_of_birth = f'{year}-{months.index(month) + 1:02d}-{int(day):02d}'

        aadhar_number = aadharnumberentry.get()
        pan_card_number = pancardnumberentry.get()
        father_name = fathernameentry.get()
        mother_name = mothernameentry.get()
        address = addressentry.get()
        city = cityentry.get()
        district = districtentry.get()
        state = stateentry.get()
        country = countryentry.get()
        pin_code = pincodeentry.get()
        email = emailentry.get()
        education_qualification = educationentry.get()
        account_type = accounttypeentry.get()
        gst_number = gstnumberentry.get()

        sql = '''INSERT INTO account_details 
                 (name, age, mobile_number, date_of_birth, aadhar_number, 
                  pan_card_number, father_name, mother_name, address, city, 
                  district, state, country, pin_code, email, education_qualification, 
                  account_type, gst_number)
                 VALUES
                 (%s, %s, %s, %s,
                 %s, %s, %s, %s,
                 %s, %s, %s, %s,
                 %s, %s, %s, %s,
                 %s, %s)'''
        values = (name, age, mobile_number, date_of_birth, aadhar_number, 
                  pan_card_number, father_name, mother_name, address, city, 
                  district, state, country, pin_code, email, 
                  education_qualification, account_type, gst_number)

        cursor.execute(sql, values)
        conn.commit()

        cursor.execute('SELECT LAST_INSERT_ID()')
        account_number = cursor.fetchone()[0]

        messagebox.showinfo(title = 'Success',
                            message = f'''Your account has been created successfully.
                                          \nAccount Number: {account_number}''')

        global account_label, remove_button
        account_label = Label(root,
                              text = f'Account Number: {account_number}',
                              font = ('Arial', 12, 'bold'))
        account_label.pack()

        remove_button = Button(root,
                               text = 'Remove',
                               command = remove_account_display,
                               bg = 'red',
                               fg = 'white')
        remove_button.pack()

        name1entry.delete(0, END)
        age2entry.delete(0, END)
        mobilenumber1entry.delete(0, END)
        selected_day.set('Day')
        selected_month.set('Month')
        selected_year.set('Year')
        aadharnumberentry.delete(0, END)
        pancardnumberentry.delete(0, END)
        fathernameentry.delete(0, END)
        mothernameentry.delete(0, END)
        addressentry.delete(0, END)
        cityentry.delete(0, END)
        districtentry.delete(0, END)
        stateentry.delete(0, END)
        countryentry.delete(0, END)
        pincodeentry.delete(0, END)
        emailentry.delete(0, END)
        educationentry.set('')
        accounttypeentry.set('')
        gstnumberentry.delete(0, END)

    except mysql.connector.Error as err:
        messagebox.showerror(title = 'Error',
                             message = f'Error: {err}')
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def remove_account_display():
    '''Removes the displayed account number and the remove button'''
    account_label.destroy()
    remove_button.destroy()

def depositmoney():
    show_frame(depositandwithdrawframe)

def deposit_button():
    account_number = accountnumberentry.get().strip()
    deposit_amount = amountentry.get().strip()

    if not account_number or not deposit_amount:
        messagebox.showwarning(title = 'Error', 
                               message = 'Please enter account number and amount.')
        return

    if not account_number.isdigit():
        messagebox.showwarning(title = 'Error', 
                               message = 'Account number must be numeric.')
        return

    try:
        deposit_amount = float(deposit_amount)
        if deposit_amount <= 0:
            messagebox.showwarning(title = 'Error', 
                                   message = 'Enter a valid deposit amount.')
            return

        cursor = conn.cursor()

        cursor.execute(
            '''SELECT account_number 
            FROM account_details 
            WHERE account_number = %s''', 
            (account_number,)
        )
        if not cursor.fetchone():
            messagebox.showwarning(title = 'Error', 
                                   message = 'Invalid Account Number')
            accountnumberentry.delete(0, END)
            amountentry.delete(0, END)
            cursor.close()
            return

        cursor.execute(
            '''SELECT balance 
            FROM Transactions 
            WHERE account_number = %s 
            ORDER BY transaction_date 
            DESC LIMIT 1''',
            (account_number,))
        current_balance = cursor.fetchone()
        last_balance = current_balance[0] if current_balance else 0
        new_balance = float(last_balance) + deposit_amount

        cursor.execute(
            '''INSERT INTO Transactions
            (account_number, balance, amount, transaction_type)
            VALUES (%s, %s, %s, 'Deposit')''',
            (account_number, new_balance, deposit_amount)
        )
        conn.commit()

        messagebox.showinfo(title = 'Success',
                            message = 'Deposit Successful')
        accountnumberentry.delete(0, END)
        amountentry.delete(0, END)

    except ValueError:
        messagebox.showwarning(title = 'Error',
                               message = 'Enter a valid numeric amount.')

    except mysql.connector.Error as db_error:
        messagebox.showerror(title = 'Database Error', 
                             message = f'Database error: {db_error}')
        conn.rollback()

    finally:
        cursor.close()

def withdraw_button():
    account_number = accountnumberentry.get().strip()
    withdraw_amount = amountentry.get().strip()

    if not account_number or not withdraw_amount:
        messagebox.showwarning(title = 'Error',
                               message = 'Please enter account number and amount.')
        return

    if not account_number.isdigit():
        messagebox.showwarning(title = 'Error',
                               message = 'Account number must be numeric.')
        return

    try:
        withdraw_amount = float(withdraw_amount)
        if withdraw_amount <= 0:
            messagebox.showwarning(title = 'Error',
                                   message = 'Enter a valid withdrawal amount.')
            return

        if conn is None:
            messagebox.showerror(title = 'Database Error',
                                 message = 'Database connection is not established.')
            return
        
        cursor = conn.cursor(buffered = True)

        cursor.execute(
            '''SELECT account_number 
            FROM account_details 
            WHERE account_number = %s''', 
            (account_number,)
        )
        if not cursor.fetchone():
            messagebox.showwarning(title = 'Error', 
                                   message = 'Invalid Account Number')
            accountnumberentry.delete(0, END)
            amountentry.delete(0, END)
            cursor.close()
            return

        cursor.execute(
            '''SELECT balance FROM Transactions 
            WHERE account_number = %s 
            ORDER BY transaction_date 
            DESC LIMIT 1''',
            (account_number,)
        )
        current_balance = cursor.fetchone()
        last_balance = current_balance[0] if current_balance else 0

        if last_balance < withdraw_amount:
            messagebox.showwarning(title = 'Error',
                                   message = 'Insufficient balance.')
            cursor.close()
            return

        new_balance = float(last_balance) - withdraw_amount

        cursor.execute(
            '''INSERT INTO Transactions
            (account_number, balance, amount, transaction_type) 
            VALUES (%s, %s, %s, 'Withdraw')''',
            (account_number, new_balance, withdraw_amount)
        )
        conn.commit()

        messagebox.showinfo(title = 'Success',
                            message = 'Withdrawal Successful')
        accountnumberentry.delete(0, END)
        amountentry.delete(0, END)

    except ValueError:
        messagebox.showwarning(title = 'Error',
                               message = 'Enter a valid numeric amount.')

    except mysql.connector.Error as db_error:
        messagebox.showerror(title = 'Database Error',
                             message = f'Database error: {db_error}')
        conn.rollback()

    finally:
        if cursor:
            cursor.close()

root = Tk()
root.title('Online Banking System - Dashboard')
root.geometry('1920x1080')

headerpoint = Frame(root,
                    width = 20,
                    relief = SOLID,
                    bd = 1)
headerpoint.pack(fill = 'x',
                 side = 'top',
                 padx = 5,
                 pady = 5)

home = Button(headerpoint,
              text = 'Home',
              bg = 'lightgrey',
              fg = 'black',
              font = ('Arial', 12, 'bold'),
              command = homebutton,
              width = 15)
home.pack(side = 'left',
          padx = 70,
          pady = 15)

create_account = Button(headerpoint,
                        text = 'Create Account',
                        bg = 'lightgrey',
                        fg = 'black',
                        font = ('Arial', 12, 'bold'),
                        command = createaccount,
                        width = 15)
create_account.pack(side = 'left',
                    pady = 15,
                    padx = 200)

depositandwithdraw_money = Button(headerpoint,
                                  text = 'Deposit and Withdraw Cash',
                                  bg = 'lightgrey',
                                  fg = 'black',
                                  font = ('Arial', 12, 'bold'),
                                  command = depositmoney,
                                  width = 25)
depositandwithdraw_money.pack(side = 'right',
                              pady = 15,
                              padx = 70)

main_frame = Frame(root,
                   bd = 1,
                   relief = SOLID)
main_frame.pack(expand = True,
                fill = 'both',
                padx = 5,
                pady = 5)

homeframe = Frame(main_frame)
accountframe = Frame(main_frame)
depositandwithdrawframe = Frame(main_frame)

for frame in (homeframe,
              accountframe,
              depositandwithdrawframe):
    frame.place(x = 0,
                y = 0,
                relwidth = 1,
                relheight = 1)

show_frame(homeframe)

welcome = Label(homeframe,
                text = 'Welcome to System & Start Your Work',
                font = ('Arial', 18, 'bold'))
welcome.pack(pady = 100)

heading = Label(accountframe,
                text = 'New Account Application Form',
                font = ('Arial', 14, 'bold'))
heading.grid(row = 0,
             column = 0,
             columnspan = 7,
             pady = 10)

name1 = Label(accountframe,
              text = 'Name',
              font = ('Arial', 12, 'bold'))
name1entry = Entry(accountframe,
                   font = ('Arial', 12))
name1.grid(row = 1,
           column = 0,
           padx = 10,
           pady = 10,
           sticky = 'e')
name1entry.grid(row = 1,
                column = 1,
                padx = 5,
                pady = 10,
                sticky = 'w',
                columnspan = 3)

age2 = Label(accountframe,
             text = 'Age',
             font = ('Arial', 12, 'bold'))
age2entry = Entry(accountframe,
                  font = ('Arial', 12))
age2.grid(row = 1,
          column = 4,
          padx = 5,
          pady = 10,
          sticky = 'e')
age2entry.grid(row = 1,
               column = 5,
               padx = 5,
               pady = 10,
               sticky = 'w')

mobilenumber1 = Label(accountframe,
                      text = 'Mobile Number',
                      font = ('Arial', 12, 'bold'))
mobilenumber1entry = Entry(accountframe,
                           font = ('Arial', 12))
mobilenumber1.grid(row = 1,
                   column = 6,
                   padx = 5,
                   pady = 10,
                   sticky = 'e')
mobilenumber1entry.grid(row = 1,
                       column = 7,
                       padx = 5,
                       pady = 10,
                       sticky = 'w')

dob = Label(accountframe,
            text = 'Date of Birth',
            font = ('Arial', 12, 'bold'))
dob.grid(row = 2,
         column = 0,
         padx = 10,
         pady = 5,
         sticky = 'e')

days = [str(i) for i in range(1, 32)]
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
years = [str(i) for i in range(1925, 2026)]

selected_day = StringVar()
selected_month = StringVar()
selected_year = StringVar()

selected_day.set('Day')
selected_month.set('Month')
selected_year.set('Year')

day_dropdown = ttk.Combobox(accountframe,
                            textvariable = selected_day,
                            values = days,
                            width = 5,
                            state = 'readonly')
month_dropdown = ttk.Combobox(accountframe,
                              textvariable = selected_month,
                              values = months,
                              width = 10,
                              state = 'readonly')
year_dropdown = ttk.Combobox(accountframe,
                             textvariable = selected_year,
                             values = years,
                             width = 7,
                             state='readonly')

day_dropdown.grid(row = 2,
                  column = 1,
                  padx = 5,
                  pady = 5,
                  sticky = 'w')
month_dropdown.grid(row = 2,
                    column = 2,
                    padx = 5,
                    pady = 5,
                    sticky = 'w')
year_dropdown.grid(row = 2,
                   column = 3,
                   padx = 5,
                   pady = 5,
                   sticky = 'w')

aadharnumber = Label(accountframe,
                     text = 'Aadhaar No.',
                     font = ('Arial', 12, 'bold'))
aadharnumberentry = Entry(accountframe,
                          font = ('Arial', 12))
aadharnumber.grid(row = 2,
                  column = 4,
                  padx = 10,
                  pady = 5,
                  sticky = 'e')
aadharnumberentry.grid(row = 2,
                       column = 5,
                       padx = 5,
                       pady = 5,
                       sticky = 'w')

pancardnumber = Label(accountframe,
                      text = 'Pan Card Number',
                      font = ('Arial', 12, 'bold'))
pancardnumberentry = Entry(accountframe,
                           font = ('Arial', 12))
pancardnumber.grid(row = 2,
                   column = 6,
                   padx = 5,
                   pady = 5,
                   sticky = 'e')
pancardnumberentry.grid(row = 2,
                        column = 7,
                        padx = 5,
                        pady = 5,
                        sticky = 'w')

fathername = Label(accountframe,
                   text = 'Father Name',
                   font = ('Arial', 12, 'bold'))
fathernameentry = Entry(accountframe,
                        font = ('Arial', 12))
fathername.grid(row = 3,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'e')
fathernameentry.grid(row = 3,
                     column = 1,
                     padx = 5,
                     pady = 5,
                     sticky = 'w',
                     columnspan = 3)

mothername = Label(accountframe,
                   text = 'Mother Name',
                   font = ('Arial', 12, 'bold'))
mothernameentry = Entry(accountframe,
                        font = ('Arial', 12))
mothername.grid(row = 3,
                column = 4,
                padx = 5,
                pady = 5,
                sticky = 'e')
mothernameentry.grid(row = 3,
                     column = 5,
                     padx = 5,
                     pady = 5,
                     sticky = 'w')

address = Label(accountframe,
                text = 'Address',
                font = ('Arial', 12, 'bold'))
addressentry = Entry(accountframe,
                     font = ('Arial', 12))
address.grid(row = 3,
             column = 6,
             padx = 5,
             pady = 5,
             sticky = 'e')
addressentry.grid(row = 3,
                  column = 7,
                  padx = 5,
                  pady = 5,
                  sticky = 'w')

city = Label(accountframe,
             text = 'City',
             font = ('Arial', 12, 'bold'))
cityentry = Entry(accountframe,
                  font = ('Arial', 12))
city.grid(row = 4,
          column = 0,
          padx = 10,
          pady = 5,
          sticky = 'e')
cityentry.grid(row = 4,
               column = 1,
               padx = 5,
               pady = 5,
               sticky = 'w',
               columnspan = 3)

district = Label(accountframe,
                 text = 'District',
                 font = ('Arial', 12, 'bold'))
districtentry = Entry(accountframe,
                      font = ('Arial', 12))
district.grid(row = 4,
              column = 4,
              padx = 5,
              pady = 5,
              sticky = 'e')
districtentry.grid(row = 4,
                   column = 5,
                   padx = 5,
                   pady = 5,
                   sticky = 'w')

state = Label(accountframe,
              text = 'State',
              font = ('Arial', 12, 'bold'))
stateentry = Entry(accountframe,
                   font = ('Arial', 12))
state.grid(row = 4,
           column = 6,
           padx = 5,
           pady = 5,
           sticky = 'e')
stateentry.grid(row = 4,
                column = 7,
                padx = 5,
                pady = 5,
                sticky = 'w')

country = Label(accountframe,
                text = 'Country',
                font = ('Arial', 12, 'bold'))
countryentry = Entry(accountframe,
                     font = ('Arial', 12))
country.grid(row = 5,
             column = 0,
             padx = 10,
             pady = 5,
             sticky = 'e')
countryentry.grid(row = 5,
                  column = 1,
                  padx = 5,
                  pady = 5,
                  sticky = 'w',
                  columnspan = 3)

pincode = Label(accountframe,
                text = 'Pin Code',
                font = ('Arial', 12, 'bold'))
pincodeentry = Entry(accountframe,
                     font = ('Arial', 12))
pincode.grid(row = 5,
             column = 4,
             padx = 5,
             pady = 5,
             sticky = 'e')
pincodeentry.grid(row = 5,
                  column = 5,
                  padx = 5,
                  pady = 5,
                  sticky = 'w')

email = Label(accountframe,
              text = 'Email Address',
              font = ('Arial', 12, 'bold'))
emailentry = Entry(accountframe,
                   font = ('Arial', 12))
email.grid(row = 5,
           column = 6,
           padx = 5,
           pady = 5,
           sticky = 'e')
emailentry.grid(row = 5,
                column = 7,
                padx = 5,
                pady = 5,
                sticky = 'w')

education = Label(accountframe,
                  text = 'Education Qualification',
                  font  = ('Arial', 12, 'bold'))
educationentry = ttk.Combobox(accountframe,
                              values = ['', 
                                        'Below 12th',
                                        '12th Pass',
                                        'Diploma Holder',
                                        'Graduate',
                                        'Post Graduate',
                                        'Doctrate'],
                              font = ('Arial', 12))
education.grid(row = 6,
               column = 0,
               padx = 10,
               pady = 5,
               sticky = 'e')
educationentry.grid(row = 6,
                    column = 1,
                    padx = 10,
                    pady = 5,
                    sticky = 'w',
                    columnspan = 3)

accounttype = Label(accountframe,
                    text = 'Account Type',
                    font = ('Arial', 12, 'bold'))
accounttypeentry = ttk.Combobox(accountframe,
                                values = ['',
                                          'Saving',
                                          'Current'],
                                font = ('Arial', 12))
accounttypeentry.bind('<<ComboboxSelected>>',
                      gst_entry)
accounttype.grid(row = 6,
                 column = 4,
                 padx = 5,
                 pady = 5,
                 sticky = 'e')
accounttypeentry.grid(row = 6,
                      column = 5,
                      padx = 5,
                      pady = 5,
                      sticky = 'w')

gstnumber = Label(accountframe,
                  text = 'GST Number',
                  font = ('Arial', 12, 'bold'))
gstnumberentry = Entry(accountframe,
                       font = ('Arial', 12))

accountbutton = Button(accountframe,
                       text = 'Create Account',
                       font = ('Arial', 12, 'bold'),
                       command = account_button)
accountbutton.grid(row = 7,
                   column = 0,
                   columnspan = 8,
                   pady = 5)

heading1 = Label(depositandwithdrawframe,
                 text = 'Deposit and Withdraw Cash',
                 font = ('Arial', 14, 'bold'))
heading1.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber = Label(depositandwithdrawframe,
                      text = 'Account Number',
                      font = ('Arial', 12, 'bold'))
accountnumberentry = Entry(depositandwithdrawframe,
                           font = ('Arial', 12))
accountnumber.grid(row = 1,
                   column = 0,
                   padx = 10,
                   pady = 10,
                   sticky = 'e')
accountnumberentry.grid(row = 1,
                        column = 1,
                        padx = 10,
                        pady = 10,
                        sticky = 'w')

amount = Label(depositandwithdrawframe,
               text = 'Amount',
               font = ('Arial', 12, 'bold'))
amountentry = Entry(depositandwithdrawframe,
                    font = ('Arial', 12))
amount.grid(row = 1,
            column = 2,
            padx = 10,
            pady = 10,
            sticky = 'e')
amountentry.grid(row = 1,
                 column = 3,
                 padx = 10,
                 pady = 10,
                 sticky = 'w')

depositbutton = Button(depositandwithdrawframe,
                       text = 'Deposit', 
                       font = ('Arial', 12, 'bold'), 
                       command = deposit_button,
                       bg = 'lightgrey')
depositbutton.grid(row = 2,
                   column = 0, 
                   columnspan = 2,
                   pady = 10)

withdrawbutton = Button(depositandwithdrawframe,
                        text = 'Withdraw',
                        font = ('Arial', 12, 'bold'),
                        command = withdraw_button,
                        bg = 'lightgrey')
withdrawbutton.grid(row = 2,
                    column = 2,
                    columnspan = 2,
                    pady = 10)

root.mainloop()