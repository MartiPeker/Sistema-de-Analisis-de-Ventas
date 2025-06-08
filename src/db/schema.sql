CREATE DATABASE IF NOT EXISTS sales_company;
USE sales_company;

CREATE TABLE IF NOT EXISTS customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    MiddleInitial CHAR(1),
    LastName VARCHAR(50),
    CityID INT,
    Address VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price FLOAT,
    CategoryID INT,
    Class VARCHAR(50),
    ModifyDate VARCHAR(50),
    Resistant VARCHAR(50),
    IsAllergic VARCHAR(50),
    VitalityDays INT
);