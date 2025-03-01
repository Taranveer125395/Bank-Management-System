from tkinter import *
from tkinter import messagebox
import subprocess
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

def depositmoney():
    show_frame(depositframe)

def withdrawmoney():
    show_frame(withdrawfram)

def loanapplication():
    show_frame(loanframe)

def transactionhistory():
    show_frame(transactionframe)

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

main_frame = Frame(root, bg = 'white')
main_frame.pack(expand = True, fill = 'both')

homeframe = Frame(main_frame, bg = 'white')
accountframe = Frame(main_frame, bg = 'skyblue')
depositframe = Frame(main_frame, bg = 'skyblue')
withdrawfram = Frame(main_frame, bg = 'skyblue')
loanframe = Frame(main_frame, bg = 'skyblue')
transactionframe = Frame(main_frame, bg = 'skyblue')

for frame in (homeframe, accountframe, depositframe, withdrawfram, loanframe, transactionframe):
    frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

root.mainloop()