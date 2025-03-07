from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

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

def get_user_details(username):
    try:
        query = '''SELECT fullname, username, mobile_number,
                age, education_qualification, job_type FROM 
                staff_registeration WHERE username = %s'''
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return user_data
    
    except mysql.connector.Error as err:
        messagebox.showerror(title='Database Error', message=f'Error: {err}')
        return None

def createaccount():
    show_frame(accountframe)

def validate_button():
    datetext = dobentry.get()
    try:
        datetime.strptime(datetext, "%Y-%m-%d")
        messagebox.showinfo(title = 'Success',
                            message = 'Valid Date Format: YYYY-MM-DD')
    except ValueError:
        messagebox.showerror(title = 'Error',
                             message = 'Invalid Date! Use Format: YYYY-MM-DD')

def on_entry_focus_in(event):
    if dobentry.get() == "yyyy-mm-dd":
        dobentry.delete(0, END)
        dobentry.config(fg = "black")

def on_entry_focus_out(event):
    if dobentry.get() == "":
        dobentry.insert(0, "yyyy-mm-dd")
        dobentry.config(fg = "grey")

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

def get_next_account_number():
    cursor.execute("SELECT MAX(account_number) FROM account_details")
    last_account = cursor.fetchone()[0]
    
    if last_account is None:
        return 1001
    else:
        return last_account + 1

def generate_pdf(account_data):
    account_number = account_data[0]
    pdf_filename = f"Account_{account_number}.pdf"
    
    c = canvas.Canvas(pdf_filename, pagesize = A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Account Details")
    c.drawString(100, 730, f"Account Number: {account_number}")
    
    labels = ["Name", "Age", "Mobile Number", "Date of Birth", "Aadhar Number",
              "PAN Card Number", "Father's Name", "Mother's Name", "Address",
              "City", "District", "State", "Country", "Pin Code", "Email",
              "Education Qualification", "Account Type", "GST Number"]
    
    y_position = 710
    for i, label in enumerate(labels):
        c.drawString(100, y_position, f"{label}: {account_data[i+1]}")
        y_position -= 20
    
    c.save()
    messagebox.showinfo(title = "PDF Generated", 
                        message = f"Account details saved as {pdf_filename}")

def account_button():
    account_number = get_next_account_number()
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

    sql = """
    INSERT INTO account_details (
        account_number, name, age, mobile_number, date_of_birth,
        aadhar_number, pan_card_number, father_name, mother_name,
        address, city, district, state, country, pin_code, email,
        education_qualification, account_type, gst_number
    ) VALUES (
        %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s
    )
    """

    values = (account_number, name, age, mobile_number, date_of_birth, aadhar_number,
              pan_card_number, father_name, mother_name, address, city, district, state,
              country, pin_code, email, education_qualification, account_type, gst_number)

    try:
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo(title = "Success",
                            message = "Your account has been created successfully!")

        generate_pdf((account_number, name, age, mobile_number, date_of_birth,
                      aadhar_number, pan_card_number, father_name, mother_name,
                      address, city, district, state, country, pin_code, email,
                      education_qualification, account_type, gst_number))

        name1entry.delete(0, END)
        age2entry.delete(0, END)
        mobilenumber1entry.delete(0, END)
        dobentry.delete(0, END)
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
        messagebox.showerror(title = "Error",
                             message = f"Error: {err}")
    
    finally:
        cursor.close()
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
        
        cursor = conn.cursor(buffered=True)

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
        businesstype.grid(row = 2,
                          column = 4, 
                          padx = 10, 
                          pady = 10, 
                          sticky = 'e')
        businesstypeentry.grid(row = 2, 
                               column = 5, 
                               padx = 10, 
                               pady = 10, 
                               sticky = 'w')
        productstype.grid(row = 3,
                          column = 0, 
                          padx = 10, 
                          pady = 10, 
                          sticky = 'e')
        productstypeentry.grid(row = 3, 
                               column = 1, 
                               padx = 10, 
                               pady = 10, 
                               sticky = 'w')
        businessname.grid(row = 3, 
                          column = 2, 
                          padx = 10, 
                          pady = 10, 
                          sticky = 'e')
        businessnameentry.grid(row = 3,
                               column = 3, 
                               padx = 10, 
                               pady = 10, 
                               sticky = 'w')
        address1.grid(row = 3,
                      column = 4, 
                      padx = 10, 
                      pady = 10, 
                      sticky = 'e')
        address1entry.grid(row = 3,
                           column = 5, 
                           padx = 10, 
                           pady = 10, 
                           sticky = 'w')
    else:
        businesstype.grid_remove()
        businesstypeentry.grid_remove()
        productstype.grid_remove()
        productstypeentry.grid_remove()
        businessname.grid_remove()
        businessnameentry.grid_remove()
        address1.grid_remove()
        address1entry.grid_remove()

def unemployed(event = None):
    if loantypeentry.get() != 'Education' and sourceincomeentry.get() == 'Unemployed':
        guarantorname.grid(row = 2,
                           column = 4,
                           padx = 10,
                           pady = 10,
                           sticky = 'e')
        guarantornameentry.grid(row = 2,
                                column = 5,
                                padx = 10,
                                pady = 10,
                                sticky = 'w')
        guarantoraccount.grid(row = 3,
                              column = 0,
                              padx = 10,
                              pady = 10,
                              sticky = 'e')
        guarantoraccountentry.grid(row = 3,
                                   column = 1,
                                   padx = 10,
                                   pady = 10,
                                   sticky = 'w')
    else:
        guarantorname.grid_remove()
        guarantornameentry.grid_remove()
        guarantoraccount.grid_remove()
        guarantoraccountentry.grid_remove()

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

def generate_pdf(account_data):
    if not account_data:
        messagebox.showerror(title = 'Error',
                             message = 'No account detail found!')
        return
    
    pdf_file = f'AccountDetail_{account_data[0]}.pdf'
    doc = SimpleDocTemplate(pdf_file,
                            pagesize = A4)
    elements = []
    styles = getSampleStyleSheet()
    bold_style = ParagraphStyle(name = "BoldStyle",
                                parent = styles["Normal"], 
                                fontName = "Helvetica-Bold",
                                fontSize = 10)
    
    data = [['Field', 'Data']]
    labels = [
        'Account Number',
        'Name',
        'Age',
        'Mobile Number',
        'Date of Birth',
        'Aadhar Number',
        'Pan Card Number',
        'Father Name',
        'Mother Name',
        'Address',
        'City',
        'District',
        'State',
        'Country',
        'Pin Code',
        'Email',
        'Education Qualification',
        'Account Type',
        'GST Number',
        'Created At'
    ]
    
    for i, label in enumerate(labels):
        data.append([Paragraph(label, bold_style),
                     str(account_data[i])])

    
    table = Table(data,
                  colWidths = [150, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)
    doc.build(elements)
    messagebox.showinfo(title = 'PDF Generated',
                        message = f'PDF saved as {pdf_file}')

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
    
    generate_pdf(account_data)
    accountnumber2entry.delete(0, 'end')

def generate_balance_pdf(account_number):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                '''SELECT account_number, name 
                FROM account_details 
                WHERE account_number = %s''',
                (account_number,)
            )
            account = cursor.fetchone()

            if not account:
                messagebox.showerror(title = "Error",
                                     message = "Account not found!")
                return

            account_num, account_name = account

            query = """
            SELECT id, transaction_date, 
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
            ORDER BY id ASC
            """
            cursor.execute(query, (account_number,))
            transactions = cursor.fetchall()

        conn.close()

        pdf_filename = f"Balance_Enquiry_{account_number}.pdf"
        doc = SimpleDocTemplate(pdf_filename,
                                pagesize = A4)
        
        elements = []
        styles = getSampleStyleSheet()
        
        elements.append(Paragraph(f"<b>Account Number:</b> {account_num}", styles["Normal"]))
        elements.append(Paragraph(f"<b>Name:</b> {account_name}", styles["Normal"]))
        elements.append(Spacer(1, 15))

        table_data = [["ID", 
                       "Transaction Date",
                       "Deposit",
                       "Withdraw",
                       "Balance"]]
        
        for row in transactions:
            table_data.append([row[0],
                               row[1],
                               row[2] or "",
                               row[3] or "",
                               row[4]])

        table = Table(table_data,
                      colWidths = [50, 
                                   120, 
                                   80, 
                                   80, 
                                   80])
        
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
        messagebox.showinfo(title = "Success",
                            message = f"PDF generated: {pdf_filename}")

        accountnumber2entry.delete(0, END)

    except mysql.connector.Error as db_error:
        messagebox.showerror(title = "Database Error",
                             message = f"Error: {db_error}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_generate_pdf():
    account_number = accountnumber2entry.get()
    if account_number.isdigit():
        generate_balance_pdf(account_number)
    else:
        messagebox.showerror(title = "Error",
                             message = "Please enter a valid account number")

def loan():
    messagebox.showwarning(title = 'Loan',
                           message = 'Your Loan is Pending.')

if len(sys.argv) > 1:
    logged_in_username = sys.argv[1]
else:
    logged_in_username = None

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
              bg = 'lightgrey',
              fg = 'black',
              font = ('Arial', 11, 'bold'),
              command = homebutton,
              width = 15)
home.pack(side = 'top',
          padx = 5,
          pady = 5)

create_account = Button(headerpoint,
                        text = 'Create Account',
                        bg = 'lightgrey',
                        fg = 'black',
                        font = ('Arial', 11, 'bold'),
                        command = createaccount,
                        width = 15)
create_account.pack(side = 'top',
                    pady = 5,
                    padx = 5)

deposit_money = Button(headerpoint,
                       text = 'D and W Cash',
                       bg = 'lightgrey',
                       fg = 'black',
                       font = ('Arial', 11, 'bold'),
                       command = depositmoney,
                       width = 15)
deposit_money.pack(side = 'top',
                   pady = 5,
                   padx = 5)

apply_for_loan = Button(headerpoint,
                        text = 'Apply For Loan',
                        bg = 'lightgrey',
                        fg = 'black',
                        font = ('Arial', 11, 'bold'),
                        command = loanapplication,
                        width = 15)
apply_for_loan.pack(side = 'top',
                    pady = 5,
                    padx = 5)

transaction_history = Button(headerpoint,
                             text = 'Transaction History',
                             bg = 'lightgrey',
                             fg = 'black',
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
loanframe = Frame(main_frame)
transactionframe = Frame(main_frame)

for frame in (homeframe,
              accountframe,
              depositframe,
              loanframe,
              transactionframe):
    frame.place(x = 0,
                y = 0,
                relwidth = 1,
                relheight = 1)

show_frame(homeframe)

if logged_in_username:
    user_details = get_user_details(logged_in_username)
    if user_details:
        fullname, username, mobile, age, qualification, job = user_details
        name = Label(homeframe,
                     text = f"Full Name: {fullname}",
                     font = ('Arial', 12))
        name.pack(pady = 5)
        uname = Label(homeframe,
                      text = f"Username: {username}",
                      font = ('Arial', 12))
        uname.pack(pady = 5)
        mno = Label(homeframe,
                    text = f"Mobile Number: {mobile}",
                    font = ('Arial', 12))
        mno.pack(pady = 5)
        ag = Label(homeframe,
                   text = f"Age: {age}",
                   font = ('Arial', 12))
        ag.pack(pady = 5)
        eq = Label(homeframe,
                   text = f"Qualification: {qualification}",
                   font = ('Arial', 12))
        eq.pack(pady = 5)
        jt = Label(homeframe,
                   text = f"Job Type: {job}",
                   font = ('Arial', 12))
        jt.pack(pady = 5)
    else:
        ud  = Label(homeframe,
                    text = "User details not found!",
                    font = ('Arial', 12, 'bold'))
        ud.pack(pady = 10)
else:
    nu = Label(homeframe,
               text = "No username provided!",
               font = ('Arial', 12, 'bold'))
    nu.pack(pady = 10)

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

age2 = Label(accountframe,
             text = 'Age',
             font = ('Arial', 11))
age2entry = Entry(accountframe,
                  font = ('Arial', 11))
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

mobilenumber1 = Label(accountframe,
                     text = 'Mobile Number',
                     font = ('Arial', 11))
mobilenumber1entry = Entry(accountframe,
                          font = ('Arial', 11),
                          validatecommand = (vcmd, "%M"))
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

dob = Label(accountframe,
            text = "Date of Birth",
            font = ("Arial", 11))
dob.grid(row = 2,
         column = 0,
         padx = 10,
         pady = 5,
         sticky = "e")

dobentry = Entry(accountframe,
                 font = ("Arial", 11),
                 fg = "grey")
dobentry.insert(0,
                "yyyy-mm-dd")
dobentry.bind("<FocusIn>",
              on_entry_focus_in)
dobentry.bind("<FocusOut>",
              on_entry_focus_out)
dobentry.grid(row = 2,
              column = 1,
              padx = 5,
              pady = 5,
              sticky = "w")

validate = Button(accountframe,
                  text = "Validate",
                  command = validate_button, 
                  font = ("Arial", 10))
validate.grid(row = 2,
              column = 2)

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
                 text = 'Deposit and Withdraw Cash',
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
                   columnspan = 2,
                   pady = 10)

withdrawbutton = Button(depositframe,
                        text = 'Withdraw',
                        font = ('Arial', 11),
                        command = withdraw_button)
withdrawbutton.grid(row = 2,
                    column = 2,
                    columnspan = 2,
                    pady = 10)

heading3 = Label(loanframe,
                 text = 'Loan Application',
                 font = ('Arial', 14, 'bold'))
heading3.grid(row = 0,
              column = 0,
              columnspan = 7,
              pady = 20)

accountnumber1 = Label(loanframe,
                      text = 'Account Number',
                      font = ('Arial', 11))
accountnumber1entry = Entry(loanframe,
                           font = ('Arial', 11))
accountnumber1.grid(row = 1,
                   column = 0,
                   padx = 10,
                   pady = 10,
                   sticky = 'e')
accountnumber1entry.grid(row = 1,
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
loantype.grid(row = 1,
              column = 4,
              padx = 10,
              pady = 5,
              sticky = 'e')
loantypeentry.grid(row = 1,
                   column = 5,
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
sourceincomeentry.bind('<<ComboboxSelected>>',
                       unemployed)
sourceincome.grid(row = 2,
                  column = 2,
                  padx = 10,
                  pady = 10,
                  sticky = 'e')
sourceincomeentry.grid(row = 2,
                       column = 3,
                       padx = 10,
                       pady = 10,
                       sticky = 'w')

guarantorname = Label(loanframe,
                      text = 'Guarantor Name', 
                      font = ('Arial', 11))
guarantornameentry = Entry(loanframe, 
                           font = ('Arial', 11))
guarantoraccount = Label(loanframe,
                         text = 'Guarantor Account No.', 
                         font = ('Arial', 11))
guarantoraccountentry = Entry(loanframe, 
                              font = ('Arial', 11))

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

address1 = Label(loanframe,
                 text = 'Business Address',
                 font = ('Arial', 11))
address1entry = Entry(loanframe,
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

accountnumber2 = Label(transactionframe,
                      text = 'Account Number',
                      font = ('Arial', 11))
accountnumber2entry = Entry(transactionframe,
                           font = ('Arial', 11))
accountnumber2.grid(row = 1,
                   column = 0,
                   padx = 10,
                   pady = 10,
                   sticky = 'w')
accountnumber2entry.grid(row = 1,
                        column = 1,
                        padx = 10,
                        pady = 10,
                        sticky = 'w')

accountdetailbutton = Button(transactionframe,
                            text = 'Account Detail',
                            font = ('Arial', 11),
                            command = account_detail)
accountdetailbutton.grid(row = 2,
                         column = 0,
                         padx = 10,
                         pady = 10,
                         sticky = 'w')

balanceenquirybutton = Button(transactionframe,
                              text = 'Balance Enquery',
                              font = ('Arial', 11),
                              command = on_generate_pdf)
balanceenquirybutton.grid(row = 2,
                          column = 1,
                          padx = 10,
                          pady = 10,
                          sticky = 'w')

loanenquirybutton = Button(transactionframe,
                           text = 'Loan Enquery',
                           font = ('Arial', 11),
                           command = loan)
loanenquirybutton.grid(row = 2,
                       column = 2,
                       padx = 10,
                       pady = 10,
                       sticky = 'w')

root.mainloop()