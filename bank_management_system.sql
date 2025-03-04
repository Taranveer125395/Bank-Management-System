Create database Banking_Management_System;

Use Banking_Management_System;

create table staff_login(
    username varchar(50),
    password varchar (50)
);

create table staff_registeration(
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

CREATE TABLE account_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
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
)AUTO_INCREMENT = 1001;

CREATE TABLE Transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) NOT NULL,
    balance DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    amount DECIMAL(10,2) NOT NULL,
    transaction_type ENUM('deposit', 'withdraw') NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)AUTO_INCREMENT = 1;

CREATE TABLE LoanApplication (
    id INT PRIMARY KEY AUTO_INCREMENT,
    account_number VARCHAR(20) NOT NULL,
    loan_amount DECIMAL(15,2) NOT NULL,
    income_per_year DECIMAL(15,2) NOT NULL,
    loan_type ENUM('Personal', 'Home', 'Vehicle', 'Business', 'Education') NOT NULL,
    source_of_income ENUM('Employed', 'Self-Employed', 'Unemployed') NOT NULL,
    guarantor_name VARCHAR(100),
    guarantor_account_no VARCHAR(20),
    employer_type ENUM('Private Sector', 'Government Sector'),
    position VARCHAR(100),
    department ENUM('Railway', 'Police', 'Revenue', 'Civil Services', 'Banking'),
    office_address VARCHAR(255),
    employer_name VARCHAR(100),
    business_type ENUM('Manufacturing', 'Service Based', 'Retail & E-Commerce', 'Wholesale', 'Agriculture & Farming', 'Technology & IT', 'Finance & Banking', 'Real Estate & Construction', 'Entertainment & Media'),
    product_type VARCHAR(100),
    business_name VARCHAR(100),
    business_address VARCHAR(255)
)AUTO_INCREMENT = 10001;

select * from staff_registeration;

select * from staff_login;

select * from loans;

select * from transactions;

select * from accounts;