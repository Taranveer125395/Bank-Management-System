import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

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

def validate_button():
    datetext = dobentry.get()
    try:
        datetime.strptime(datetext, '%Y-%m-%d')
        messagebox.showinfo(title = 'Success',
                            message = 'Valid Date Format: YYYY-MM-DD')
    except ValueError:
        messagebox.showerror(title = 'Error',
                             message = 'Invalid Date! Use Format: YYYY-MM-DD')

def on_entry_focus_in(event):
    if dobentry.get() == 'yyyy-mm-dd':
        dobentry.delete(0, tk.END)
        dobentry.config(fg = 'black')

def on_entry_focus_out(event):
    if dobentry.get() == '':
        dobentry.insert(0, 'yyyy-mm-dd')
        dobentry.config(fg = 'grey')

def gst_entry(event = None):
    if accounttypeentry.get() == 'Current':
        gstnumber.grid(row = 6,
                       column = 5,
                       padx = 5,
                       pady = 5,
                       sticky = 'e')
        gstnumberentry.grid(row = 6,
                            column = 6,
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
        date_of_birth = dobentry.get()
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
                 VALUES (%s, %s, %s, %s,
                 %s, %s, %s, %s, %s, %s,
                 %s, %s, %s, %s, %s, %s,
                 %s, %s)'''

        values = (name, age, mobile_number, date_of_birth, aadhar_number, 
                  pan_card_number, father_name, mother_name, address, city, 
                  district, state, country, pin_code, email, 
                  education_qualification, account_type, gst_number)

        cursor.execute(sql, values)
        conn.commit()
        
        messagebox.showinfo(title = 'Success',
                            message = 'Your account has been created successfully.')

        name1entry.delete(0, tk.END)
        age2entry.delete(0, tk.END)
        mobilenumber1entry.delete(0, tk.END)
        dobentry.delete(0, tk.END)
        aadharnumberentry.delete(0, tk.END)
        pancardnumberentry.delete(0, tk.END)
        fathernameentry.delete(0, tk.END)
        mothernameentry.delete(0, tk.END)
        addressentry.delete(0, tk.END)
        cityentry.delete(0, tk.END)
        districtentry.delete(0, tk.END)
        stateentry.delete(0, tk.END)
        countryentry.delete(0, tk.END)
        pincodeentry.delete(0, tk.END)
        emailentry.delete(0, tk.END)
        educationentry.set('')
        accounttypeentry.set('')
        gstnumberentry.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror(title = 'Error',
                             message = f'Error: {err}')
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def mobile_number_validation(M):
    if M.isdigit() and len(M) <= 10:
        return True
    elif M == ' ':
        return True
    else:
        messagebox.showerror(title = 'Error',
                             message = 'Mobile number shoul be equal to 10 digits')

def depositmoney():
    show_frame(depositframe)

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
            accountnumberentry.delete(0, tk.END)
            amountentry.delete(0, tk.END)
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
        accountnumberentry.delete(0, tk.END)
        amountentry.delete(0, tk.END)

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
            accountnumberentry.delete(0, tk.END)
            amountentry.delete(0, tk.END)
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
        accountnumberentry.delete(0, tk.END)
        amountentry.delete(0, tk.END)

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

def transactionhistory():
    show_frame(transactionframe)

def fetch_account_detail(account_number):
    try:
        query = '''
            SELECT * FROM account_details 
            WHERE account_number = %s
        '''
        cursor.execute(query, (account_number,))
        account_data = cursor.fetchone()
        return account_data
    except mysql.connector.Error as e:
        messagebox.showerror(title = 'Database Error', 
                             message = f'Error fetching account details: {str(e)}')
        return None

def display_account_detail(account_data):
    for widget in transactionframe.winfo_children():
        if isinstance(widget, tk.Label) and widget not in [accountnumber2, accountnumber2entry]:
            widget.destroy()
    
    if not account_data:
        messagebox.showerror(title = 'Error',
                             message = 'No account detail found!')
        return
    
    accountnumber2entry.config(state = 'disabled')
    
    labels = ['Account Number', 'Name', 'Age', 'Mobile Number', 'Date of Birth',
              'Aadhar Number', 'Pan Card Number', 'Father Name', 'Mother Name',
              'Address', 'City', 'District', 'State', 'Country', 'Pin Code',
              'Email', 'Education Qualification', 'Account Type', 'GST Number',
              'Created At']
    
    canvas = tk.Canvas(transactionframe)
    scrollbar = tk.Scrollbar(transactionframe,
                             orient = 'vertical',
                             command = canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion = canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0),
                         window = scrollable_frame,
                         anchor = 'nw')
    canvas.configure(yscrollcommand = scrollbar.set)
    
    for i, label in enumerate(labels):
        tk.Label(scrollable_frame,
                 text = f"{label}:",
                 font = ('Arial', 12, 'bold')).grid(row = i,
                                                    column = 0,
                                                    sticky = 'w',
                                                    padx = 10,
                                                    pady = 2)
        tk.Label(scrollable_frame,
                 text = f"{account_data[i]}",
                 font = ('Arial', 12, 'italic')).grid(row = i,
                                                      column = 1,
                                                      sticky = 'w',
                                                      padx = 10,
                                                      pady = 2)
    
    canvas.grid(row = 3,
                column = 0,
                columnspan = 2,
                sticky = 'nsew')
    scrollbar.grid(row = 3,
                   column = 2,
                   sticky = 'ns')
    
    remove_button = tk.Button(transactionframe,
                              text = 'Remove Details',
                              font = ('Arial', 12, 'bold'),
                              command = lambda: remove_account_details(canvas,
                                                                       scrollbar,
                                                                       remove_button),
                              bg = 'red',
                              fg = 'white')
    remove_button.grid(row = 4,
                       column = 0,
                       columnspan = 2,
                       padx = 10,
                       pady = 10)

def remove_account_details(canvas, scrollbar, remove_button):
    canvas.destroy()
    scrollbar.destroy()
    remove_button.destroy()
    accountnumber2entry.config(state = 'normal')
    accountnumber2entry.delete(0, tk.END)

def account_detail():
    account_number = accountnumber2entry.get()
    
    if not account_number.isdigit():
        messagebox.showerror(title = 'Invalid Input',
                             message = 'Please enter a valid Account Number.')
        return
    
    account_data = fetch_account_detail(account_number)
    
    if not account_data:
        messagebox.showerror(title = 'Error',
                             message = 'No account found with this number.')
        return
    
    if isinstance(account_data, dict):
        account_data = tuple(account_data.values())

    elif isinstance(account_data, list) and isinstance(account_data[0], (list, tuple)):
        account_data = account_data[0]

    elif not isinstance(account_data, (list, tuple)):
        messagebox.showerror(title = 'Error',
                             message = 'Invalid account data format.')
        return
    
    display_account_detail(account_data)

def generate_balance_pdf(account_number):
    try:
        cursor = conn.cursor(dictionary = True)

        cursor.execute(
            '''SELECT account_number, name 
            FROM account_details 
            WHERE account_number = %s''',
            (account_number,)
        )
        account = cursor.fetchone()

        if not account:
            messagebox.showerror(title = 'Error',
                                 message = 'Account not found!')
            return

        account_num, account_name = account['account_number'], account['name']

        query = '''SELECT id, transaction_date,
                CASE
                    WHEN transaction_type = 'Deposit' 
                    THEN amount 
                    ELSE NULL 
                    END AS deposit,
                CASE
                    WHEN transaction_type = 'Withdraw' 
                    THEN amount
                    ELSE NULL 
                    END AS withdraw,
                balance
                FROM Transactions
                WHERE account_number = %s
                ORDER BY id ASC'''
        
        cursor.execute(query, (account_number,))
        transactions = cursor.fetchall()

        cursor.close()

        pdf_filename = f'Balance_Enquiry_{account_number}.pdf'
        doc = SimpleDocTemplate(pdf_filename,
                                pagesize = A4)

        elements = []
        styles = getSampleStyleSheet()

        styles['Normal'].alignment = TA_CENTER
        elements.append(Paragraph('<b>Online Banking System</b>',
                                  styles['Normal']))
        elements.append(Paragraph(f'<b>Account Number:</b> {account_num}',
                                  styles['Normal']))
        elements.append(Paragraph(f'<b>Name:</b> {account_name}',
                                  styles['Normal']))
        elements.append(Spacer(1, 15))

        table_data = [['ID', 'Date', 'Time',
                       'Deposit', 'Withdraw', 'Balance']]

        for row in transactions:
            transaction_date = row['transaction_date']
            date_str = transaction_date.strftime('%Y-%m-%d')
            time_str = transaction_date.strftime('%H:%M:%S')

            table_data.append([row['id'], date_str, time_str,
                               row['deposit'] if row['deposit'] else '-',
                               row['withdraw'] if row['withdraw'] else '-',
                               row['balance']])

        table = Table(table_data, colWidths = [50, 80, 80, 80, 80, 80])

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ]))

        elements.append(table)
        doc.build(elements)

        messagebox.showinfo(title = 'Success',
                            message = f'PDF generated: {pdf_filename}')

        accountnumber2entry.delete(0, tk.END)

    except mysql.connector.Error as db_error:
        messagebox.showerror(title = 'Database Error',
                             message = f'Error: {db_error}')
    except Exception as e:
        messagebox.showerror(title = 'Error',
                             message = str(e))

def on_generate_pdf():
    account_number = accountnumber2entry.get()
    if account_number.isdigit():
        generate_balance_pdf(account_number)
    else:
        messagebox.showerror(title = 'Error',
                             message = 'Please enter a valid account number')

if len(sys.argv) > 1:
    logged_in_username = sys.argv[1]
else:
    logged_in_username = None

root = tk.Tk()
root.title('Online Banking System - Dashboard')
root.geometry('1920x1080')

headerpoint = tk.Frame(root,
                       width = 20,
                       relief = tk.SOLID,
                       bd = 1)
headerpoint.pack(fill = 'x',
                 side = 'top',
                 padx = 5,
                 pady = 5)

home = tk.Button(headerpoint,
              text = 'Home',
              bg = 'lightgrey',
              fg = 'black',
              font = ('Arial', 12, 'bold'),
              command = homebutton,
              width = 15)
home.pack(side = 'left',
          padx = 70,
          pady = 15)

create_account = tk.Button(headerpoint,
                           text = 'Create Account',
                           bg = 'lightgrey',
                           fg = 'black',
                           font = ('Arial', 12, 'bold'),
                           command = createaccount,
                           width = 15)
create_account.pack(side = 'left',
                    pady = 15,
                    padx = 70)

transaction_history = tk.Button(headerpoint,
                                text = 'Transaction History',
                                bg = 'lightgrey',
                                fg = 'black',
                                font = ('Arial', 12, 'bold'),
                                command = transactionhistory,
                                width = 15)
transaction_history.pack(side = 'right',
                         pady = 15,
                         padx = 70)

deposit_money = tk.Button(headerpoint,
                          text = 'Deposit and Withdraw Cash',
                          bg = 'lightgrey',
                          fg = 'black',
                          font = ('Arial', 12, 'bold'),
                          command = depositmoney,
                          width = 25)
deposit_money.pack(side = 'right',
                   pady = 15,
                   padx = 70)

main_frame = tk.Frame(root,
                      bd = 1,
                      relief = tk.SOLID)
main_frame.pack(expand = True,
                fill = 'both',
                padx = 5,
                pady = 5)

homeframe = tk.Frame(main_frame)

accountframe = tk.Frame(main_frame)
vcmd = accountframe.register(mobile_number_validation)

depositframe = tk.Frame(main_frame)
transactionframe = tk.Frame(main_frame)

for frame in (homeframe,
              accountframe,
              depositframe,
              transactionframe):
    frame.place(x = 0,
                y = 0,
                relwidth = 1,
                relheight = 1)

show_frame(homeframe)

welcome = tk.Label(homeframe,
                   text = 'Welcome to System & Start Your Work',
                   font = ('Arial', 18, 'bold'))
welcome.pack(pady = 100)

heading = tk.Label(accountframe,
                   text = 'New Account Application Form',
                   font = ('Arial', 14, 'bold'))
heading.grid(row = 0,
             column = 0,
             columnspan = 7,
             pady = 10)

name1 = tk.Label(accountframe,
                 text = 'Name',
                 font = ('Arial', 12, 'bold'))
name1entry = tk.Entry(accountframe,
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
                sticky = 'w')

age2 = tk.Label(accountframe,
                text = 'Age',
                font = ('Arial', 12, 'bold'))
age2entry = tk.Entry(accountframe,
                     font = ('Arial', 12))
age2.grid(row = 1,
          column = 3,
          padx = 5,
          pady = 10,
          sticky = 'e')
age2entry.grid(row = 1,
               column = 4,
               padx = 5,
               pady = 10,
               sticky = 'w')

mobilenumber1 = tk.Label(accountframe,
                         text = 'Mobile Number',
                         font = ('Arial', 12, 'bold'))
mobilenumber1entry = tk.Entry(accountframe,
                              font = ('Arial', 12),
                              validatecommand = (vcmd, '%M'))
mobilenumber1.grid(row = 1,
                   column = 5,
                   padx = 5,
                   pady = 10,
                   sticky = 'e')
mobilenumber1entry.grid(row = 1,
                       column = 6,
                       padx = 5,
                       pady = 10,
                       sticky = 'w')

dob = tk.Label(accountframe,
               text = 'Date of Birth',
               font = ('Arial', 12, 'bold'))
dob.grid(row = 2,
         column = 0,
         padx = 10,
         pady = 5,
         sticky = 'e')

dobentry = tk.Entry(accountframe,
                    font = ('Arial', 12),
                    fg = 'grey')
dobentry.insert(0,
                'yyyy-mm-dd')
dobentry.bind('<FocusIn>',
              on_entry_focus_in)
dobentry.bind('<FocusOut>',
              on_entry_focus_out)
dobentry.grid(row = 2,
              column = 1,
              padx = 5,
              pady = 5,
              sticky = 'w')

validate = tk.Button(accountframe,
                     text = 'Validate',
                     command = validate_button, 
                     font = ('Arial', 12, 'bold'),
                     bg = 'lightgrey')
validate.grid(row = 2,
              column = 2)

aadharnumber = tk.Label(accountframe,
                        text = 'Aadhaar No.',
                        font = ('Arial', 12, 'bold'))
aadharnumberentry = tk.Entry(accountframe,
                             font = ('Arial', 12))
aadharnumber.grid(row = 2,
                  column = 3,
                  padx = 10,
                  pady = 5,
                  sticky = 'e')
aadharnumberentry.grid(row = 2,
                       column = 4,
                       padx = 5,
                       pady = 5,
                       sticky = 'w')

pancardnumber = tk.Label(accountframe,
                         text = 'Pan Card Number',
                         font = ('Arial', 12, 'bold'))
pancardnumberentry = tk.Entry(accountframe,
                              font = ('Arial', 12))
pancardnumber.grid(row = 2,
                   column = 5,
                   padx = 5,
                   pady = 5,
                   sticky = 'e')
pancardnumberentry.grid(row = 2,
                        column = 6,
                        padx = 5,
                        pady = 5,
                        sticky = 'w')

fathername = tk.Label(accountframe,
                      text = 'Father Name',
                      font = ('Arial', 12, 'bold'))
fathernameentry = tk.Entry(accountframe,
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
                     sticky = 'w')

mothername = tk.Label(accountframe,
                      text = 'Mother Name',
                      font = ('Arial', 12, 'bold'))
mothernameentry = tk.Entry(accountframe,
                           font = ('Arial', 12))
mothername.grid(row = 3,
                column = 3,
                padx = 5,
                pady = 5,
                sticky = 'e')
mothernameentry.grid(row = 3,
                     column = 4,
                     padx = 5,
                     pady = 5,
                     sticky = 'w')

address = tk.Label(accountframe,
                   text = 'Address',
                   font = ('Arial', 12, 'bold'))
addressentry = tk.Entry(accountframe,
                        font = ('Arial', 12))
address.grid(row = 3,
             column = 5,
             padx = 5,
             pady = 5,
             sticky = 'e')
addressentry.grid(row = 3,
                  column = 6,
                  padx = 5,
                  pady = 5,
                  sticky = 'w')

city = tk.Label(accountframe,
                text = 'City',
                font = ('Arial', 12, 'bold'))
cityentry = tk.Entry(accountframe,
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
               sticky = 'w')

district = tk.Label(accountframe,
                    text = 'District',
                    font = ('Arial', 12, 'bold'))
districtentry = tk.Entry(accountframe,
                         font = ('Arial', 12))
district.grid(row = 4,
              column = 3,
              padx = 5,
              pady = 5,
              sticky = 'e')
districtentry.grid(row = 4,
                   column = 4,
                   padx = 5,
                   pady = 5,
                   sticky = 'w')

state = tk.Label(accountframe,
                 text = 'State',
                 font = ('Arial', 12, 'bold'))
stateentry = tk.Entry(accountframe,
                      font = ('Arial', 12))
state.grid(row = 4,
           column = 5,
           padx = 5,
           pady = 5,
           sticky = 'e')
stateentry.grid(row = 4,
                column = 6,
                padx = 5,
                pady = 5,
                sticky = 'w')

country = tk.Label(accountframe,
                   text = 'Country',
                   font = ('Arial', 12, 'bold'))
countryentry = tk.Entry(accountframe,
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
                  sticky = 'w')

pincode = tk.Label(accountframe,
                   text = 'Pin Code',
                   font = ('Arial', 12, 'bold'))
pincodeentry = tk.Entry(accountframe,
                        font = ('Arial', 12))
pincode.grid(row = 5,
           column = 3,
           padx = 5,
           pady = 5,
           sticky = 'e')
pincodeentry.grid(row = 5,
                  column = 4,
                  padx = 5,
                  pady = 5,
                  sticky = 'w')

email = tk.Label(accountframe,
                 text = 'Email Address',
                 font = ('Arial', 12, 'bold'))
emailentry = tk.Entry(accountframe,
                      font = ('Arial', 12))
email.grid(row = 5,
           column = 5,
           padx = 5,
           pady = 5,
           sticky = 'e')
emailentry.grid(row = 5,
                column = 6,
                padx = 5,
                pady = 5,
                sticky = 'w')

education = tk.Label(accountframe,
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
                    sticky = 'w')

accounttype = tk.Label(accountframe,
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
                 column = 3,
                 padx = 5,
                 pady = 5,
                 sticky = 'e')
accounttypeentry.grid(row = 6,
                      column = 4,
                      padx = 5,
                      pady = 5,
                      sticky = 'w')

gstnumber = tk.Label(accountframe,
                     text = 'GST Number',
                     font = ('Arial', 12, 'bold'))
gstnumberentry = tk.Entry(accountframe,
                          font = ('Arial', 12))

accountbutton = tk.Button(accountframe,
                          text = 'Create Account',
                          font = ('Arial', 12, 'bold'),
                          command = account_button)
accountbutton.grid(row = 7,
                   column = 0,
                   columnspan = 7,
                   pady = 5)

heading1 = tk.Label(depositframe,
                    text = 'Deposit and Withdraw Cash',
                    font = ('Arial', 14, 'bold'))
heading1.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber = tk.Label(depositframe,
                         text = 'Account Number',
                         font = ('Arial', 12, 'bold'))
accountnumberentry = tk.Entry(depositframe,
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

amount = tk.Label(depositframe,
                  text = 'Amount',
                  font = ('Arial', 12, 'bold'))
amountentry = tk.Entry(depositframe, 
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

depositbutton = tk.Button(depositframe,
                          text = 'Deposit', 
                          font = ('Arial', 12, 'bold'), 
                          command = deposit_button,
                          bg = 'lightgrey')
depositbutton.grid(row = 2,
                   column = 0, 
                   columnspan = 2,
                   pady = 10)

withdrawbutton = tk.Button(depositframe,
                           text = 'Withdraw',
                           font = ('Arial', 12, 'bold'),
                           command = withdraw_button,
                           bg = 'lightgrey')
withdrawbutton.grid(row = 2,
                    column = 2,
                    columnspan = 2,
                    pady = 10)

heading4 = tk.Label(transactionframe,
                    text = 'Account History',
                    font = ('Arial', 14, 'bold'))
heading4.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber2 = tk.Label(transactionframe,
                          text = 'Account Number',
                          font = ('Arial', 12, 'bold'))
accountnumber2entry = tk.Entry(transactionframe,
                               font = ('Arial', 12))
accountnumber2.grid(row = 1,
                   column = 0,
                   padx = 10,
                   pady = 10,
                   sticky = 'w')
accountnumber2entry.grid(row = 1,
                        column = 1,
                        padx = 10,
                        pady = 10,
                        sticky = 'e')

accountdetailbutton = tk.Button(transactionframe,
                                text = 'Account Detail',
                                font = ('Arial', 12, 'bold'),
                                command = account_detail,
                                bg = 'lightgrey')
accountdetailbutton.grid(row = 2,
                         column = 0,
                         padx = 10,
                         pady = 10)

balanceenquirybutton = tk.Button(transactionframe,
                                 text = 'Balance Enquery',
                                 font = ('Arial', 12, 'bold'),
                                 command = on_generate_pdf,
                                 bg = 'lightgrey')
balanceenquirybutton.grid(row = 2,
                          column = 1,
                          padx = 10,
                          pady = 10)

root.mainloop()