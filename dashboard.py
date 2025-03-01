from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector

def createaccount():
    messagebox.showinfo(title = 'Account Created',
                        message = ' Your Bank Account is successfully created.')

def depositmoney():
    messagebox.showinfo(title = 'Money Deposited', message = 'Your Money is depositted.')

def withdrawmoney():
    messagebox.showinfo(title = 'Money Withdraw', message = 'Your money is withdrawed.')

def loanapplication():
    messagebox.showinfo(title = 'Loan Applied', message = 'Your loan is succefully applied')

def transactionhistory():
    messagebox.showinfo(title = 'Transaction History', message = 'Your transaction history is available.')

root = Tk()
root.title('Bank Management System - Dashboard')
root.geometry('1920x1080')

headerpoint = Frame(root,
                    bg = 'lightpink',
                    width = 50)
headerpoint.pack(fill = 'y',
                 side = 'left')

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

root.mainloop()