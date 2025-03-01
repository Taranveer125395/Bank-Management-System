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

create table transactions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    type ENUM('Deposit', 'Withdraw') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

create table loans(
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

select * from staff_registeration;

select * from staff_login;

select * from loans;

select * from transactions;

select * from accounts;