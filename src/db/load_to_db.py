import pandas as pd
from sqlalchemy.orm import Session
from db.connection import DBConnection
from orm.base import Base
from orm.customer import Customer
from orm.product import Product
from orm.sale import Sale
from orm.city import City
from orm.country import Country
from orm.employee import Employee
from orm.category import Category
from sqlalchemy import create_engine

# Leer archivos CSV
customers_df = pd.read_csv("data/customers.csv")
products_df = pd.read_csv("data/products.csv")
sales_df = pd.read_csv("data/sales.csv")
cities_df = pd.read_csv("data/cities.csv")
countries_df = pd.read_csv("data/countries.csv")
employees_df = pd.read_csv("data/employees.csv")
categories_df = pd.read_csv("data/categories.csv")

# Inicializar conexión y crear tablas
conn = DBConnection()
engine = conn.engine
Base.metadata.create_all(bind=engine)
session = conn.get_session()

# Cargar datos
def load_data(df, Model):
    objects = [Model(**row.dropna().to_dict()) for _, row in df.iterrows()]
    session.bulk_save_objects(objects)

# Precaución: el orden respeta claves foráneas
load_data(countries_df, Country)
load_data(cities_df, City)
load_data(categories_df, Category)
load_data(customers_df, Customer)
load_data(employees_df, Employee)
load_data(products_df, Product)
load_data(sales_df, Sale)

session.commit()
session.close()
print("Datos cargados exitosamente a la base de datos.")