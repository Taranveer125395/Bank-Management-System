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

select * from staff_registeration;

select * from staff_login;