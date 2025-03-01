from tkinter import *
from tkinter import messagebox
import subprocess

def createaccount():
    messagebox.showinfo(title = 'Account Created',
                        message = ' Your Bank Account is successfully created.')

def depositmoney():
    messagebox.showinfo(title = 'Money Deposited', message = 'Your Money is depositted.')

root = Tk()
root.title('Bank Management System - Dashboard')
root.geometry('1920x1080')

headerpoint = Frame(root, bg = 'lightpink', width = 50)
headerpoint.pack(fill = 'y', side = 'left')

create_account = Button(headerpoint,
                        text = 'Create Account',
                        bg = '#87CEFA',
                        fg = 'white',
                        font = ('Arial', 12, 'bold'),
                        command = createaccount)
create_account.pack(side = 'top',
                    pady = 5,
                    padx = 5)

deposit_money = Button(headerpoint,
                       text =  'Deposit Money',
                       bg = '#90EE90',
                       fg = 'white',
                       font = ('Arial', 12, 'bold'),
                       command = depositmoney)
deposit_money.pack(side = 'top',
                   pady = 5,
                   padx = 5)

withdraw_money = Button(headerpoint, text = 'Withdraw Money', bg = '#90EE90', fg = 'White', font = ('Arial', 12, 'bold'))
withdraw_money.pack(side = 'top', pady = 5, padx = 5)

root.mainloop()