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

create table accounts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age int,
    mobilenumber VARCHAR(255),
    dob date,
    aadhaarno bigint,
    pancardno VARCHAR(255),
    fathername varchar(255),
    mothername varchar(255),
    address varchar(255),
    city varchar(255),
    district varchar(255),
    state varchar(255),
    country varchar(255),
    pincode int,
    email varchar(255),
    balance DECIMAL(10,2) NOT NULL
)AUTO_INCREMENT = 1001;

CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) NOT NULL,
    transaction_type ENUM('Deposit', 'Withdraw') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES accounts(id)
);

CREATE TABLE LoanApplication (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    account_number VARCHAR(20) NOT NULL,
    loan_amount DECIMAL(15,2) NOT NULL,
    total_income DECIMAL(15,2) NOT NULL,
    loan_type ENUM('Personal', 'Home', 'Vehicle', 'Business', 'Education') NOT NULL,
    source_income ENUM('Employed', 'Self-Employed', 'Unemployed') NOT NULL,
    guarantor_name VARCHAR(100),
    guarantor_account VARCHAR(20)
);

CREATE TABLE EmploymentDetails (
    employment_id INT PRIMARY KEY AUTO_INCREMENT,
    application_id INT,
    employer_type ENUM('Private Sector', 'Government Sector'),
    position VARCHAR(100),
    department ENUM('Railway', 'Police', 'Revenue', 'Civil Services', 'Banking'),
    office_address TEXT,
    employer_name VARCHAR(100),
    FOREIGN KEY (application_id) REFERENCES LoanApplication(application_id)
);

CREATE TABLE BusinessDetails (
    business_id INT PRIMARY KEY AUTO_INCREMENT,
    application_id INT,
    business_type ENUM('Manufacturing', 'Service Based', 'Retail & E-Commerce', 'Wholesale', 'Agriculture & Farming', 'Technology & IT', 'Finance & Banking', 'Real Estate & Construction', 'Entertainment & Media'),
    product_type VARCHAR(255),
    business_name VARCHAR(255),
    business_address TEXT,
    FOREIGN KEY (application_id) REFERENCES LoanApplication(application_id)
);

select * from staff_registeration;

select * from staff_login;

select * from loans;

select * from transactions;

select * from accounts;