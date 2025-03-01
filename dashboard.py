from tkinter import *
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

def withdrawmoney():
    show_frame(withdrawfram)

def loanapplication():
    show_frame(loanframe)

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

headerpoint = Frame(root,
                    bg = 'lightpink',
                    width = 50)
headerpoint.pack(fill = 'y',
                 side = 'left')

home = Button(headerpoint,
              text = 'Home',
              bg = 'black',
              fg = 'white',
              font = ('Arial', 12, 'bold'),
              command = homebutton)
home.pack(side = 'top',
          padx = 5,
          pady = 5)

create_account = Button(headerpoint,
                        text = 'Create Account',
                        bg = 'black',
                        fg = 'white',
                        font = ('Arial', 12, 'bold'),
                        command = createaccount)
create_account.pack(side = 'top',
                    pady = 5,
                    padx = 5)

deposit_money = Button(headerpoint,
                       text = 'Deposit Money',
                       bg = 'black',
                       fg = 'white',
                       font = ('Arial', 12, 'bold'),
                       command = depositmoney)
deposit_money.pack(side = 'top',
                   pady = 5,
                   padx = 5)

withdraw_money = Button(headerpoint,
                        text = 'Withdraw Money', 
                        bg = 'black',
                        fg = 'White',
                        font = ('Arial', 12, 'bold'),
                        command = withdrawmoney)
withdraw_money.pack(side = 'top', 
                    pady = 5,
                    padx = 5)

apply_for_loan = Button(headerpoint,
                        text = 'Apply For Loan',
                        bg = 'black',
                        fg = 'white',
                        font = ('Arial', 12, 'bold'),
                        command = loanapplication)
apply_for_loan.pack(side = 'top',
                    pady = 5,
                    padx = 5)

transaction_history = Button(headerpoint,
                             text = 'Transaction History',
                             bg = 'black',
                             fg = 'white',
                             font = ('Arial', 12, 'bold'),
                             command = transactionhistory)
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
withdrawfram = Frame(main_frame)
loanframe = Frame(main_frame)
transactionframe = Frame(main_frame)

for frame in (homeframe,
              accountframe,
              depositframe,
              withdrawfram,
              loanframe,
              transactionframe):
    frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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
                   font = ('Arial', 12),
                   fg = 'blue')
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
                  font = ('Arial', 12),
                  fg = 'blue')
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
                          fg = 'blue',
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
                 font = ('Arial', 12), fg = 'blue')
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
                          font = ('Arial', 12),
                          fg = 'blue')
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
                           font = ('Arial', 12),
                           fg = 'blue')
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
                        font = ('Arial', 12),
                        fg = 'blue')
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
                        font = ('Arial', 12),
                        fg = 'blue')
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
                     font = ('Arial', 12),
                     fg = 'blue')
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
                  font = ('Arial', 12),
                  fg = 'blue')
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
                      font = ('Arial', 12),
                      fg = 'blue')
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
                   font = ('Arial', 12),
                   fg = 'blue')
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
                     font = ('Arial', 12),
                     fg = 'blue')
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
                     font = ('Arial', 12),
                     fg = 'blue')
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
                   font = ('Arial', 12),
                   fg = 'blue')
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

accountbutton = Button(accountframe,
                       text = 'Create Account',
                       font = ('Arial', 12),
                       command = account_button)
accountbutton.grid(row = 6,
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
                      font = ('Arial', 12, 'bold'))
accountnumberentry = Entry(depositframe,
                           font = ('Arial', 12, 'bold'),
                           fg= 'blue')
accountnumber.grid(row = 1,
                   column = 0,
                   padx = 10,
                   pady = 10,
                   sticky = 'e')
accountnumberentry.grid(row = 1,
                        column = 1,
                        padx = 10,
                        pady = 5,
                        sticky = 'w')

root.mainloop()