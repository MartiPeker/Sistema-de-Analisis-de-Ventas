import csv
from models.customer import Customer
from models.employee import Employee
from models.product import Product
from models.sale import Sale
from models.category import Category
from models.city import City
from models.country import Country

def load_customers(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Customer(
            int(row['CustomerID']),
            row['FirstName'],
            row['MiddleInitial'],
            row['LastName'],
            int(row['CityID']),
            row['Address']
        ) for row in reader]

def load_employees(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Employee(
            int(row['EmployeeID']),
            row['FirstName'],
            row['MiddleInitial'],
            row['LastName'],
            row['BirthDate'],
            row['Gender'],
            int(row['CityID']),
            row['HireDate']
        ) for row in reader]

def load_products(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Product(
            int(row['ProductID']),
            row['ProductName'],
            float(row['Price']),
            int(row['CategoryID']),
            row['Class'],
            row['ModifyDate'],
            row['Resistant'],
            row['IsAllergic'],
            int(row['VitalityDays'])
        ) for row in reader]

def load_sales(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Sale(
            int(row['SalesID']),
            int(row['SalesPersonID']),
            int(row['CustomerID']),
            int(row['ProductID']),
            int(row['Quantity']),
            float(row['Discount']),
            float(row['TotalPrice']),
            row['SalesDate'],
            row['TransactionNumber']
        ) for row in reader]

def load_categories(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Category(
            int(row['CategoryID']),
            row['CategoryName']
        ) for row in reader]

def load_cities(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [City(
            int(row['CityID']),
            row['CityName'],
            row['Zipcode'],
            int(row['CountryID'])
        ) for row in reader]

def load_countries(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Country(
            int(row['CountryID']),
            row['CountryName'],
            row['CountryCode']
        ) for row in reader]