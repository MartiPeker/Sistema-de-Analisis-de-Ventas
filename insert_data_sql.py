import pandas as pd

table_order = [
    "countries",
    "categories",
    "cities",
    "customers",
    "employees",
    "products",
    "sales"
]

table_definitions = {
    "countries": """
        CREATE TABLE countries (
            CountryID INT PRIMARY KEY,
            CountryName VARCHAR(255),
            CountryCode VARCHAR(10)
        );
    """,
    "categories": """
        CREATE TABLE categories (
            CategoryID INT PRIMARY KEY,
            CategoryName VARCHAR(255)
        );
    """,
    "cities": """
        CREATE TABLE cities (
            CityID INT PRIMARY KEY,
            CityName VARCHAR(255),
            Zipcode INT,
            CountryID INT,
            FOREIGN KEY (CountryID) REFERENCES countries(CountryID)
        );
    """,
    "customers": """
        CREATE TABLE customers (
            CustomerID INT PRIMARY KEY,
            FirstName VARCHAR(255),
            MiddleInitial VARCHAR(5),
            LastName VARCHAR(255),
            CityID INT,
            Address VARCHAR(255),
            FOREIGN KEY (CityID) REFERENCES cities(CityID)
        );
    """,
    "employees": """
        CREATE TABLE employees (
            EmployeeID INT PRIMARY KEY,
            FirstName VARCHAR(255),
            MiddleInitial VARCHAR(5),
            LastName VARCHAR(255),
            BirthDate DATETIME,
            Gender CHAR(1),
            CityID INT,
            HireDate DATETIME,
            FOREIGN KEY (CityID) REFERENCES cities(CityID)
        );
    """,
    "products": """
        CREATE TABLE products (
            ProductID INT PRIMARY KEY,
            ProductName VARCHAR(255),
            Price FLOAT,
            CategoryID INT,
            Class VARCHAR(50),
            ModifyDate VARCHAR(20),
            Resistant VARCHAR(50),
            IsAllergic VARCHAR(50),
            VitalityDays INT,
            FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID)
        );
    """,
    "sales": """
        CREATE TABLE sales (
            SalesID INT PRIMARY KEY,
            SalesPersonID INT,
            CustomerID INT,
            ProductID INT,
            Quantity INT,
            Discount FLOAT,
            TotalPrice FLOAT,
            SalesDate VARCHAR(20),
            TransactionNumber VARCHAR(50),
            FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
            FOREIGN KEY (ProductID) REFERENCES products(ProductID)
        );
    """
}

def escape(val):
    if pd.isna(val):
        return 'NULL'
    if isinstance(val, str):
        return "'" + val.replace("'", "''") + "'"
    return str(val)

with open("sql/load_data.sql", "w", encoding="utf-8") as f:
    f.write("CREATE DATABASE IF NOT EXISTS analisisventas;\nUSE analisisventas;\n\n")

    for table in table_order:
        f.write(f"-- Table: {table}\n")
        f.write(table_definitions[table] + "\n")

        df = pd.read_csv(f"data/{table}.csv")
        for _, row in df.iterrows():
            values = ", ".join(escape(v) for v in row)
            f.write(f"INSERT INTO {table} VALUES ({values});\n")
        f.write("\n")

print("Archivo SQL generado: load_data.sql")