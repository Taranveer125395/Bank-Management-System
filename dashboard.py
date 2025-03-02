from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

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
                       column = 3,
                       padx = 5,
                       pady = 5,
                       sticky = 'e')
        gstnumberentry.grid(row = 6,
                            column = 4,
                            padx = 5,
                            pady = 5,
                            sticky = 'w')
    else:
        gstnumber.grid_remove()
        gstnumberentry.grid_remove()

def account_button():
    messagebox.showinfo(title = 'Success',
                        message = ' Your account is created successfully.')

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
    messagebox.showinfo(title = 'Success',
                        message = ' Your Money is depositted Successfully.')

def withdrawmoney():
    show_frame(withdrawframe)

def withdraw_button():
    messagebox.showinfo(title = 'Success',
                        message = 'Your Money is Successfully Withdrawed.')

def loanapplication():
    show_frame(loanframe)

def loan_apply():
    messagebox.showinfo(title = 'Success',
                        message = 'Your Loan is Applied.')

def transactionhistory():
    show_frame(transactionframe)

def validate_button():
    datetext = dobentry.get()
    try:
        datetime.strptime(datetext, "%d/%m/%Y")
        messagebox.showinfo(title = 'Success',
                            message = 'Valid Date Format: DD/MM/YYYY')
    except:
        messagebox.showerror(title = 'Error',
                             message = 'Invalid Date! Use Format: DD/MM/YYYY')

root = Tk()
root.title('Bank Management System - Dashboard')
root.geometry('1920x1080')
style = ttk.Style()
style.configure("Custom.TCombobox",
                foreground="blue",
                font=("Arial", 12))

headerpoint = Frame(root,
                    bg = 'lightpink',
                    width = 20)
headerpoint.pack(fill = 'y',
                 side = 'left')

home = Button(headerpoint,
              text = 'Home',
              bg = 'black',
              fg = 'white',
              font = ('Arial', 12, 'bold'),
              command = homebutton,
              width = 15)
home.pack(side = 'top',
          padx = 5,
          pady = 5)

create_account = Button(headerpoint,
                        text = 'Create Account',
                        bg = 'black',
                        fg = 'white',
                        font = ('Arial', 12, 'bold'),
                        command = createaccount,
                        width = 15)
create_account.pack(side = 'top',
                    pady = 5,
                    padx = 5)

deposit_money = Button(headerpoint,
                       text = 'Deposit Money',
                       bg = 'black',
                       fg = 'white',
                       font = ('Arial', 12, 'bold'),
                       command = depositmoney,
                       width = 15)
deposit_money.pack(side = 'top',
                   pady = 5,
                   padx = 5)

withdraw_money = Button(headerpoint,
                        text = 'Withdraw Money', 
                        bg = 'black',
                        fg = 'White',
                        font = ('Arial', 12, 'bold'),
                        command = withdrawmoney,
                        width = 15)
withdraw_money.pack(side = 'top', 
                    pady = 5,
                    padx = 5)

apply_for_loan = Button(headerpoint,
                        text = 'Apply For Loan',
                        bg = 'black',
                        fg = 'white',
                        font = ('Arial', 12, 'bold'),
                        command = loanapplication,
                        width = 15)
apply_for_loan.pack(side = 'top',
                    pady = 5,
                    padx = 5)

transaction_history = Button(headerpoint,
                             text = 'Transaction History',
                             bg = 'black',
                             fg = 'white',
                             font = ('Arial', 12, 'bold'),
                             command = transactionhistory,
                             width = 15)
transaction_history.pack(side = 'top',
                         pady = 5,
                         padx = 5)

main_frame = Frame(root,
                   bg = 'white')
main_frame.pack(expand = True,
                fill = 'both')

homeframe = Frame(main_frame)

accountframe = Frame(main_frame)
vcmd = accountframe.register(mobile_number_validation)

depositframe = Frame(main_frame)
withdrawframe = Frame(main_frame)
loanframe = Frame(main_frame)
transactionframe = Frame(main_frame)

for frame in (homeframe,
              accountframe,
              depositframe,
              withdrawframe,
              loanframe,
              transactionframe):
    frame.place(x = 0,
                y = 0,
                relwidth = 1,
                relheight = 1)

show_frame(homeframe)

heading = Label(accountframe,
                text = 'New Account Application Form',
                font = ('Arial', 14, 'bold'))
heading.grid(row = 0,
             column = 0,
             columnspan = 7,
             pady = 10)

name1 = Label(accountframe,
              text = 'Name',
              font = ('Arial', 12))
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
                sticky = 'w')

age1 = Label(accountframe,
             text = 'Age',
             font = ('Arial', 12))
age1entry = Entry(accountframe,
                  font = ('Arial', 12))
age1.grid(row = 1,
          column = 3,
          padx = 5,
          pady = 10,
          sticky = 'e')
age1entry.grid(row = 1,
               column = 4,
               padx = 5,
               pady = 10,
               sticky = 'w')

mobilenumber = Label(accountframe,
                     text = 'Mobile Number',
                     font = ('Arial', 12))
mobilenumberentry = Entry(accountframe,
                          font = ('Arial', 12),
                          validatecommand = (vcmd, "%M"))
mobilenumber.grid(row = 1,
                  column = 5,
                  padx = 5,
                  pady = 10,
                  sticky = 'e')
mobilenumberentry.grid(row = 1,
                       column = 6,
                       padx = 5,
                       pady = 10,
                       sticky = 'w')

dob = Label(accountframe,
            text = 'Date of Birth',
            font = ('Arial', 12))
dobentry = Entry(accountframe,
                 textvariable = 'dd/mm/yyyy',
                 font = ('Arial', 12))
dob.grid(row = 2,
         column = 0,
         padx = 10,
         pady = 5,
         sticky = 'e')
dobentry.grid(row = 2,
              column = 1,
              padx = 5,
              pady = 5,
              sticky = 'w')
validate = Button(accountframe,
                  text = 'Validate',
                  command = validate_button,
                  font = ('Arial', 10))
validate.grid(row = 2,
              column = 2,
              padx = 5,
              pady = 5)

aadharnumber = Label(accountframe,
                     text = 'Aadhaar No.',
                     font = ('Arial', 12))
aadharnumberentry = Entry(accountframe,
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

pancardnumber = Label(accountframe,
                      text = 'Pan Card Number',
                      font = ('Arial', 12))
pancardnumberentry = Entry(accountframe,
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

fathername = Label(accountframe,
                   text = 'Father Name',
                   font = ('Arial', 12))
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
                     sticky = 'w')

mothername = Label(accountframe,
                   text = 'Mother Name',
                   font = ('Arial', 12))
mothernameentry = Entry(accountframe,
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

address = Label(accountframe,
                text = 'Address',
                font = ('Arial', 12))
addressentry = Entry(accountframe,
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

city = Label(accountframe,
             text = 'City',
             font = ('Arial', 12))
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
               sticky = 'w')

district = Label(accountframe,
                 text = 'District',
                 font = ('Arial', 12))
districtentry = Entry(accountframe,
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

state = Label(accountframe,
              text = 'State',
              font = ('Arial', 12))
stateentry = Entry(accountframe,
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

country = Label(accountframe,
                text = 'Country',
                font = ('Arial', 12))
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
                  sticky = 'w')

pincode = Label(accountframe,
                text = 'Pin Code',
                font = ('Arial', 12))
pincodeentry = Entry(accountframe,
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

email = Label(accountframe,
              text = 'Email Address',
              font = ('Arial', 12))
emailentry = Entry(accountframe,
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

accounttype = Label(accountframe,
                    text = 'Account Type',
                    font = ('Arial', 12))
accounttypeentry = ttk.Combobox(accountframe,
                                values = ['',
                                          'Saving',
                                          'Current'],
                                font = ('Arial', 12))
accounttypeentry.bind('<<ComboboxSelected>>',
                      gst_entry)
accounttype.grid(row = 6,
                 column = 0,
                 padx = 10,
                 pady = 5,
                 sticky = 'e')
accounttypeentry.grid(row = 6,
                      column = 1,
                      padx = 5,
                      pady = 5,
                      sticky = 'w')

gstnumber = Label(accountframe,
                  text = 'GST Number',
                  font = ('Arial', 12))
gstnumberentry = Entry(accountframe,
                       font = ('Arial', 12))

accountbutton = Button(accountframe,
                       text = 'Create Account',
                       font = ('Arial', 12),
                       command = account_button)
accountbutton.grid(row = 7,
                   column = 0,
                   columnspan = 7,
                   pady = 5)

heading1 = Label(depositframe,
                 text = 'Deposit Cash',
                 font = ('Arial', 14, 'bold'))
heading1.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber = Label(depositframe,
                      text = 'Account Number',
                      font = ('Arial', 12))
accountnumberentry = Entry(depositframe,
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

amount = Label(depositframe,
               text = 'Amount',
               font = ('Arial', 12))
amountentry = Entry(depositframe, 
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

depositbutton = Button(depositframe,
                       text = 'Deposit', 
                       font = ('Arial', 12), 
                       command = deposit_button)
depositbutton.grid(row = 2,
                   column = 0, 
                   columnspan = 4,
                   pady = 10)

heading2 = Label(withdrawframe,
                 text = 'Withdraw Cash',
                 font = ('Arial', 14, 'bold'))
heading2.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber = Label(withdrawframe,
                      text = 'Account Number',
                      font = ('Arial', 12))
accountnumberentry = Entry(withdrawframe,
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

amount = Label(withdrawframe,
               text = 'Amount',
               font = ('Arial', 12))
amountentry = Entry(withdrawframe, 
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

withdrawbutton = Button(withdrawframe,
                        text = 'Withraw', 
                        font = ('Arial', 12), 
                        command = withdraw_button)
withdrawbutton.grid(row = 2,
                    column = 0, 
                    columnspan = 4,
                    pady = 10)

heading3 = Label(loanframe,
                 text = 'Loan Application',
                 font = ('Arial', 14, 'bold'))
heading3.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber = Label(loanframe,
                      text = 'Account Number',
                      font = ('Arial', 12))
accountnumberentry = Entry(loanframe,
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

loanamount = Label(loanframe,
               text = 'Amount',
               font = ('Arial', 12))
loanamountentry = Entry(loanframe, 
                    font = ('Arial', 12))
loanamount.grid(row = 1,
                column = 2,
                padx = 10,
                pady = 10,
                sticky = 'e')
loanamountentry.grid(row = 1,
                     column = 3,
                     padx = 10,
                     pady = 10,
                     sticky = 'w')

sourceincome = Label(loanframe,
                     text = 'Source of Income',
                     font = ('Arial', 12))
sourceincomeentry = ttk.Combobox(loanframe,
                                 values = ['',
                                           'Salaried',
                                           'Self-Employed',
                                           'Unemployed'],
                                 font = ('Arial', 12))
sourceincome.grid(row = 1,
                  column = 4,
                  padx = 10,
                  pady = 10,
                  sticky = 'e')
sourceincomeentry.grid(row = 1,
                       column = 5,
                       padx = 10,
                       pady = 10,
                       sticky = 'w')

totalincome = Label(loanframe,
                    text = 'Income per Year',
                    font = ('Arial', 12))
totalincomeentry = Entry(loanframe,
                         font = ('Arial', 12))
totalincome.grid(row = 2,
                 column = 0,
                 padx = 10,
                 pady = 5,
                 sticky = 'e')
totalincomeentry.grid(row = 2,
                      column = 1,
                      padx = 10,
                      pady = 5,
                      sticky = 'w')

loantype = Label(loanframe,
                 text = 'Loan Type',
                 font = ('Arial', 12))
loantypeentry = ttk.Combobox(loanframe,
                             values = ['',
                                       'Personal',
                                       'Home',
                                       'Vehical',
                                       'Business',
                                       'Education'],
                             font = ('Arial', 12))
loantype.grid(row = 2,
              column = 2,
              padx = 10,
              pady = 5,
              sticky = 'e')
loantypeentry.grid(row = 2,
                   column = 3,
                   padx = 10,
                   pady = 5,
                   sticky = 'w')

loanapplybutton = Button(loanframe,
                         text = 'Apply Loan', 
                         font = ('Arial', 12), 
                         command = loan_apply)
loanapplybutton.grid(row = 3,
                     column = 0, 
                     columnspan = 4,
                     pady = 10)

heading4 = Label(transactionframe,
                 text = 'Account History',
                 font = ('Arial', 14, 'bold'))
heading4.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber = Label(transactionframe,
                      text = 'Account Number',
                      font = ('Arial', 12))
accountnumberentry = Entry(transactionframe,
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

accountdetailbutton = Button(transactionframe,
                            text = 'Account Detail',
                            font = ('Arial', 12))
accountdetailbutton.grid(row = 2,
                         column = 0,
                         padx = 10,
                         pady = 10)

balanceenquirybutton = Button(transactionframe,
                              text = 'Balance Enquery',
                              font = ('Arial', 12))
balanceenquirybutton.grid(row = 2,
                          column = 1,
                          padx = 10,
                          pady = 10)

loanenquirybutton = Button(transactionframe,
                           text = 'Loan Enquery',
                           font = ('Arial', 12))
loanenquirybutton.grid(row = 2,
                       column = 2,
                       padx = 10,
                       pady = 10)

root.mainloop()