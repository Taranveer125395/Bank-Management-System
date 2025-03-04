CREATE DATABASE Banking_Management_System;

USE Banking_Management_System;

CREATE TABLE staff_login(
    username varchar(50),
    password varchar (50)
);

CREATE TABLE staff_registeration(
    id int unique not null auto_increment,
    fullname varchar(50),
    username varchar(50),
    mobile_number bigint,
    age int,
    education_qualification varchar(50),
    job_type varchar(50),
    password varchar(50),
    confirm_password varchar(50)
);

CREATE TABLE account_details(
    account_number INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    mobile_number VARCHAR(15) NOT NULL,
    date_of_birth DATE,
    aadhar_number VARCHAR(12),
    pan_card_number VARCHAR(10),
    father_name VARCHAR(255),
    mother_name VARCHAR(255),
    address TEXT,
    city VARCHAR(100),
    district VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    pin_code VARCHAR(10),
    email VARCHAR(255) UNIQUE,
    education_qualification ENUM('Below 12th', '12th Pass', 'Diploma Holder', 'Graduate', 'Post Graduate', 'Doctorate'),
    account_type ENUM('Saving', 'Current'),
    gst_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) AUTO_INCREMENT = 1001;

CREATE TABLE Transactions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number INT NOT NULL,
    balance DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    amount DECIMAL(10,2) NOT NULL,
    transaction_type ENUM('Deposit', 'Withdraw') NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES account_details(account_number) ON DELETE CASCADE
) AUTO_INCREMENT = 1;

CREATE TABLE loanapplication(
    id INT PRIMARY KEY AUTO_INCREMENT,
    account_number INT NOT NULL,
    loan_amount DECIMAL(15,2) NOT NULL,
    income_per_year DECIMAL(15,2) NOT NULL,
    loan_type ENUM('Personal', 'Home', 'Vehicle', 'Business', 'Education') NOT NULL,
    source_of_income ENUM('Employed', 'Self-Employed', 'Unemployed') NOT NULL,
    guarantor_name VARCHAR(100),
    guarantor_account_no INT,
    employer_type ENUM('Private Sector', 'Government Sector', 'None') DEFAULT 'None',
    position VARCHAR(100),
    department ENUM('Railway', 'Police', 'Revenue', 'Civil Services', 'Banking', 'None') DEFAULT 'None',
    office_address VARCHAR(255),
    employer_name VARCHAR(100),
    business_type ENUM('Manufacturing', 'Service Based', 'Retail & E-Commerce', 'Wholesale', 'Agriculture & Farming', 'Technology & IT', 'Finance & Banking', 'Real Estate & Construction', 'Entertainment & Media', 'None') DEFAULT 'None',
    product_type VARCHAR(100),
    business_name VARCHAR(100),
    business_address VARCHAR(255),
    FOREIGN KEY (account_number) REFERENCES account_details(account_number) ON DELETE CASCADE,
    FOREIGN KEY (guarantor_account_no) REFERENCES account_details(account_number) ON DELETE SET NULL
) AUTO_INCREMENT = 10001;


SELECT * FROM staff_registeration;

SELECT * FROM staff_login;

SELECT * FROM LoanApplication;

SELECT * FROM transactions;

SELECT * FROM account_details;