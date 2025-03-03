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

def validate_button():
    datetext = dobentry.get()
    try:
        datetime.strptime(datetext, "%d/%m/%Y")
        messagebox.showinfo(title = 'Success',
                            message = 'Valid Date Format: DD/MM/YYYY')
    except:
        messagebox.showerror(title = 'Error',
                             message = 'Invalid Date! Use Format: DD/MM/YYYY')

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

def sourceincome_entry(event = None):
    if sourceincomeentry.get() == 'Employed':
        employertype.grid(row = 2,
                          column = 4,
                          padx = 10,
                          pady = 10,
                          sticky = 'e')
        employertypeentry.grid(row = 2,
                               column = 5,
                               padx = 10,
                               pady = 10,
                               sticky = 'w')
    else:
        employertype.grid_remove()
        employertypeentry.grid_remove()

def government_sector(event = None):
    if employertypeentry.get() == 'Government Sector':
        position.grid(row = 3,
                      column = 0, 
                      padx = 10, 
                      pady = 10, 
                      sticky = 'e')
        positionentry.grid(row = 3, 
                           column = 1, 
                           padx = 10, 
                           pady = 10, 
                           sticky = 'w')
        department.grid(row = 3, 
                        column = 2, 
                        padx = 10, 
                        pady = 10, 
                        sticky = 'e')
        departmententry.grid(row = 3, 
                             column = 3, 
                             padx = 10, 
                             pady = 10, 
                             sticky = 'w')
        officeaddress.grid(row = 3, 
                           column = 4, 
                           padx = 10, 
                           pady = 10, 
                           sticky = 'e')
        officeaddressentry.grid(row = 3, 
                                column = 5, 
                                padx = 10, 
                                pady = 10, 
                                sticky = 'w')
    else:
        position.grid_remove()
        positionentry.grid_remove()
        department.grid_remove()
        departmententry.grid_remove()
        officeaddress.grid_remove()
        officeaddressentry.grid_remove()

def private_sector(event = None):
    if employertypeentry.get() == 'Private Sector':
        employername.grid(row = 3,
                          column = 0, 
                          padx = 10, 
                          pady = 10, 
                          sticky = 'e')
        employernameentry.grid(row = 3, 
                               column = 1, 
                               padx = 10, 
                               pady = 10, 
                               sticky = 'w')
        position1.grid(row = 3, 
                       column = 2, 
                       padx = 10, 
                       pady = 10, 
                       sticky = 'e')
        positionentry1.grid(row = 3, 
                            column = 3, 
                            padx = 10, 
                            pady = 10, 
                            sticky = 'w')
        officeaddress1.grid(row = 3, 
                            column = 4, 
                            padx = 10, 
                            pady = 10, 
                            sticky = 'e')
        officeaddressentry1.grid(row = 3, 
                                 column = 5, 
                                 padx = 10, 
                                 pady = 10, 
                                 sticky = 'w')
    else:
        employername.grid_remove()
        employernameentry.grid_remove()
        position1.grid_remove()
        positionentry1.grid_remove()
        officeaddress1.grid_remove()
        officeaddressentry1.grid_remove()

def business_type(event = None):
    if sourceincomeentry.get() == 'Self-Employed':
        businesstype.grid(row = 2, column = 4, padx = 10, pady = 10, sticky = 'e')
        businesstypeentry.grid(row = 2, column = 5, padx = 10, pady = 10, sticky = 'w')    
    else:
        businesstype.grid_remove()
        businesstypeentry.grid_remove()

def transactionhistory():
    show_frame(transactionframe)

root = Tk()
root.title('Bank Management System - Dashboard')
root.geometry('1920x1080')

headerpoint = Frame(root,
                    relief = 'solid',
                    bd = 1,
                    width = 20)
headerpoint.pack(fill = 'y',
                 side = 'left')

home = Button(headerpoint,
              text = 'Home',
              bg = 'blue',
              fg = 'white',
              font = ('Arial', 11, 'bold'),
              command = homebutton,
              width = 15)
home.pack(side = 'top',
          padx = 5,
          pady = 5)

create_account = Button(headerpoint,
                        text = 'Create Account',
                        bg = 'blue',
                        fg = 'white',
                        font = ('Arial', 11, 'bold'),
                        command = createaccount,
                        width = 15)
create_account.pack(side = 'top',
                    pady = 5,
                    padx = 5)

deposit_money = Button(headerpoint,
                       text = 'Deposit Money',
                       bg = 'blue',
                       fg = 'white',
                       font = ('Arial', 11, 'bold'),
                       command = depositmoney,
                       width = 15)
deposit_money.pack(side = 'top',
                   pady = 5,
                   padx = 5)

withdraw_money = Button(headerpoint,
                        text = 'Withdraw Money', 
                        bg = 'blue',
                        fg = 'White',
                        font = ('Arial', 11, 'bold'),
                        command = withdrawmoney,
                        width = 15)
withdraw_money.pack(side = 'top', 
                    pady = 5,
                    padx = 5)

apply_for_loan = Button(headerpoint,
                        text = 'Apply For Loan',
                        bg = 'blue',
                        fg = 'white',
                        font = ('Arial', 11, 'bold'),
                        command = loanapplication,
                        width = 15)
apply_for_loan.pack(side = 'top',
                    pady = 5,
                    padx = 5)

transaction_history = Button(headerpoint,
                             text = 'Transaction History',
                             bg = 'blue',
                             fg = 'white',
                             font = ('Arial', 11, 'bold'),
                             command = transactionhistory,
                             width = 15)
transaction_history.pack(side = 'top',
                         pady = 5,
                         padx = 5)

main_frame = Frame(root,
                   bd = 1,
                   relief = 'solid')
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
              font = ('Arial', 11))
name1entry = Entry(accountframe,
                   font = ('Arial', 11))
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
             font = ('Arial', 11))
age1entry = Entry(accountframe,
                  font = ('Arial', 11))
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
                     font = ('Arial', 11))
mobilenumberentry = Entry(accountframe,
                          font = ('Arial', 11),
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
            font = ('Arial', 11))
dobentry = Entry(accountframe,
                 textvariable = 'dd/mm/yyyy',
                 font = ('Arial', 11))
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
                     font = ('Arial', 11))
aadharnumberentry = Entry(accountframe,
                          font = ('Arial', 11))
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
                      font = ('Arial', 11))
pancardnumberentry = Entry(accountframe,
                           font = ('Arial', 11))
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
                   font = ('Arial', 11))
fathernameentry = Entry(accountframe,
                        font = ('Arial', 11))
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
                   font = ('Arial', 11))
mothernameentry = Entry(accountframe,
                        font = ('Arial', 11))
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
                font = ('Arial', 11))
addressentry = Entry(accountframe,
                     font = ('Arial', 11))
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
             font = ('Arial', 11))
cityentry = Entry(accountframe,
                  font = ('Arial', 11))
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
                 font = ('Arial', 11))
districtentry = Entry(accountframe,
                      font = ('Arial', 11))
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
              font = ('Arial', 11))
stateentry = Entry(accountframe,
                   font = ('Arial', 11))
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
                font = ('Arial', 11))
countryentry = Entry(accountframe,
                     font = ('Arial', 11))
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
                font = ('Arial', 11))
pincodeentry = Entry(accountframe,
                     font = ('Arial', 11))
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
              font = ('Arial', 11))
emailentry = Entry(accountframe,
                   font = ('Arial', 11))
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

education = Label(accountframe,
                  text = 'Education Qualification',
                  font  = ('Arial', 11))
educationentry = ttk.Combobox(accountframe,
                              values = ['', 
                                        'Below 12th',
                                        '12th Pass',
                                        'Diploma Holder',
                                        'Graduate',
                                        'Post Graduate',
                                        'Doctrate'],
                              font = ('Arial', 11))
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

accounttype = Label(accountframe,
                    text = 'Account Type',
                    font = ('Arial', 11))
accounttypeentry = ttk.Combobox(accountframe,
                                values = ['',
                                          'Saving',
                                          'Current'],
                                font = ('Arial', 11))
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

gstnumber = Label(accountframe,
                  text = 'GST Number',
                  font = ('Arial', 11))
gstnumberentry = Entry(accountframe,
                       font = ('Arial', 11))

accountbutton = Button(accountframe,
                       text = 'Create Account',
                       font = ('Arial', 11),
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
                      font = ('Arial', 11))
accountnumberentry = Entry(depositframe,
                           font = ('Arial', 11))
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
               font = ('Arial', 11))
amountentry = Entry(depositframe, 
                    font = ('Arial', 11))
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
                       font = ('Arial', 11), 
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
                      font = ('Arial', 11))
accountnumberentry = Entry(withdrawframe,
                           font = ('Arial', 11))
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
               font = ('Arial', 11))
amountentry = Entry(withdrawframe, 
                    font = ('Arial', 11))
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
                        font = ('Arial', 11), 
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
                      font = ('Arial', 11))
accountnumberentry = Entry(loanframe,
                           font = ('Arial', 11))
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
               font = ('Arial', 11))
loanamountentry = Entry(loanframe, 
                    font = ('Arial', 11))
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

totalincome = Label(loanframe,
                    text = 'Income per Year',
                    font = ('Arial', 11))
totalincomeentry = Entry(loanframe,
                         font = ('Arial', 11))
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
                 font = ('Arial', 11))
loantypeentry = ttk.Combobox(loanframe,
                             values = ['',
                                       'Personal',
                                       'Home',
                                       'Vehical',
                                       'Business',
                                       'Education'],
                             font = ('Arial', 11))
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

sourceincome = Label(loanframe,
                     text = 'Source of Income',
                     font = ('Arial', 11))
sourceincomeentry = ttk.Combobox(loanframe,
                                 values = ['',
                                           'Employed',
                                           'Self-Employed',
                                           'Unemployed'],
                                 font = ('Arial', 11))
sourceincomeentry.bind('<<ComboboxSelected>>',
                       sourceincome_entry)
sourceincomeentry.bind('<<ComboboxSelected>>',
                       business_type)
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

employertype = Label(loanframe, 
                     text = 'Employer Type',
                     font = ('Arial', 11))
employertypeentry = ttk.Combobox(loanframe, 
                                 values = ['', 
                                           'Private Sector', 
                                           'Government Sector'], 
                                 font = ('Arial', 11))
employertypeentry.bind('<<ComboboxSelected>>',
                       government_sector)
employertypeentry.bind('<<ComboboxSelected>>',
                       private_sector)

position = Label(loanframe,
                 text = 'Position',
                 font = ('Arial', 11))
positionentry = Entry(loanframe,
                      font = ('Arial', 11))
department = Label(loanframe,
                   text = 'Department',
                   font = ('Arial', 11))
departmententry = ttk.Combobox(loanframe,
                               values = ['',
                                         'Railway', 
                                         'Police', 
                                         'Revenue', 
                                         'Civil Services', 
                                         'Banking'],
                               font = ('Arial', 11))
officeaddress = Label(loanframe, 
                      text = 'Office Address', 
                      font = ('Arial', 11))
officeaddressentry = Entry(loanframe, 
                           font = ('Arial', 11))

employername = Label(loanframe,
                     text = 'Employer Name',
                     font = ('Arial', 11))
employernameentry = Entry(loanframe,
                          font = ('Arial', 11))
position1 = Label(loanframe,
                  text = 'Position',
                  font = ('Arial', 11))
positionentry1 = Entry(loanframe,
                       font = ('Arial', 11))
officeaddress1 = Label(loanframe,
                       text = 'Office Address', 
                       font = ('Arial', 11))
officeaddressentry1 = Entry(loanframe,
                            font = ('Arial', 11))

businesstype = Label(loanframe,
                     text = 'Business Type',
                     font = ('Arial', 11))
businesstypeentry = ttk.Combobox(loanframe,
                                 values = ['',
                                           'Manufacturing',
                                           'Service Based',
                                           'Retail & E-Commerce',
                                           'Wholesale',
                                           'Agriculture & Farming',
                                           'Technology & IT',
                                           'Finance & Banking',
                                           'Real Estate & Construction',
                                           'Entertainment & Media'],
                                 font = ('Arial', 11))
productstype = Label(loanframe,
                     text = 'Product Type',
                     font = ('Arial', 11))
productstypeentry = Entry(loanframe,
                          font = ('Arial', 11))

businessname = Label(loanframe,
                     text = 'Business/Shop Name', 
                     font = ('Arial', 11))
businessnameentry = Entry(loanframe, 
                          font = ('Arial', 11))

loanapplybutton = Button(loanframe,
                         text = 'Apply Loan', 
                         font = ('Arial', 11), 
                         command = loan_apply)
loanapplybutton.grid(row = 11,
                     column = 0, 
                     columnspan = 7,
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
                      font = ('Arial', 11))
accountnumberentry = Entry(transactionframe,
                           font = ('Arial', 11))
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
                            font = ('Arial', 11))
accountdetailbutton.grid(row = 2,
                         column = 0,
                         padx = 10,
                         pady = 10)

balanceenquirybutton = Button(transactionframe,
                              text = 'Balance Enquery',
                              font = ('Arial', 11))
balanceenquirybutton.grid(row = 2,
                          column = 1,
                          padx = 10,
                          pady = 10)

loanenquirybutton = Button(transactionframe,
                           text = 'Loan Enquery',
                           font = ('Arial', 11))
loanenquirybutton.grid(row = 2,
                       column = 2,
                       padx = 10,
                       pady = 10)

root.mainloop()