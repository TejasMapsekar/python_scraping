create database scraping;

use scraping;

create table jobtypes1(id int auto_increment ,category varchar(255),primary key(id));

create table jobtypes2(id int auto_increment,subcategory varchar(255),primary key(id));

create table categoryandsubcategory(id int auto_increment,category varchar(255),subcategory varchar(255),primary key(id));

create table states(id int auto_increment,company varchar(255),location varchar(255),primary key(id));

create table jobs(id int auto_increment,name varchar(255),location varchar(255),job varchar(255),primary key(id));

create table company_details(id int auto_increment,company varchar(255),description varchar(255),location varchar(255),numberofemp int,primary key(id));
