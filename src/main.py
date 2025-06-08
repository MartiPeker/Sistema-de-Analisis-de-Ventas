from load_data import (
    load_customers, load_employees, load_products, load_sales,
    load_categories, load_cities, load_countries
)

from analysis.context import AnalysisContext
from analysis.product_analysis import ProductAnalysisStrategy
from analysis.city_analysis import CityAnalysisStrategy

# Rutas a los archivos CSV
CUSTOMERS_CSV = 'data/customers.csv'
EMPLOYEES_CSV = 'data/employees.csv'
PRODUCTS_CSV = 'data/products.csv'
SALES_CSV = 'data/sales.csv'
CATEGORIES_CSV = 'data/categories.csv'
CITIES_CSV = 'data/cities.csv'
COUNTRIES_CSV = 'data/countries.csv'

def run_analysis(sales, products, customers, cities):
    print("\n🔍 Top 5 productos por ingresos:")
    context = AnalysisContext(ProductAnalysisStrategy())
    top_products = context.execute_analysis(sales, products, customers, cities)
    for pid, total in top_products[:5]:
        print(f"Producto ID {pid}: ${total:.2f}")

    print("\n🏙️ Top 5 ciudades por ingresos:")
    context.set_strategy(CityAnalysisStrategy())
    top_cities = context.execute_analysis(sales, products, customers, cities)
    for city, total in top_cities[:5]:
        print(f"{city}: ${total:.2f}")

def main():
    customers = load_customers(CUSTOMERS_CSV)
    employees = load_employees(EMPLOYEES_CSV)
    products = load_products(PRODUCTS_CSV)
    sales = load_sales(SALES_CSV)
    categories = load_categories(CATEGORIES_CSV)
    cities = load_cities(CITIES_CSV)
    countries = load_countries(COUNTRIES_CSV)

    print(f"Loaded {len(customers)} customers")
    print(f"Loaded {len(employees)} employees")
    print(f"Loaded {len(products)} products")
    print(f"Loaded {len(sales)} sales")
    print(f"Loaded {len(categories)} categories")
    print(f"Loaded {len(cities)} cities")
    print(f"Loaded {len(countries)} countries")

    run_analysis(sales, products, customers, cities)

if __name__ == '__main__':
    main()