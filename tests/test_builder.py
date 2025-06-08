import unittest
import pandas as pd
from src.analysis.product_analysis import ProductAnalysisStrategy
from src.analysis.city_analysis import CityAnalysisStrategy
from src.orm.sale import Sale
from src.orm.customer import Customer
from src.orm.product import Product
from src.orm.city import City
from src.analysis.builder import ReportBuilder

class TestReportBuilder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sales_df = pd.read_csv("data/sales.csv")
        sales_df.columns = ["sale_id", "salesperson_id", "customer_id", "product_id", "quantity", "discount", "total_price", "sales_date", "transaction_number"]
        cls.sales = [Sale(**row) for _, row in sales_df.iterrows()]

        customers_df = pd.read_csv("data/customers.csv")
        customers_df.columns = ["customer_id", "first_name", "middle_initial", "last_name", "city_id", "address"]
        cls.customers = [Customer(**row) for _, row in customers_df.iterrows()]

        products_df = pd.read_csv("data/products.csv")
        products_df.columns = ["product_id", "product_name", "price", "category_id", "prod_class", "modify_date", "resistant", "is_allergic", "vitality_days"]
        cls.products = [Product(**row) for _, row in products_df.iterrows()]

        cities_df = pd.read_csv("data/cities.csv")
        cities_df.columns = ["city_id", "city_name", "zipcode", "country_id"]
        cls.cities = [City(**row) for _, row in cities_df.iterrows()]

    def test_builder(self):
        builder = (
            ReportBuilder()
            .with_strategy(ProductAnalysisStrategy())
            .with_strategy(CityAnalysisStrategy())
            .build()
        )
        results = builder.execute_all(self.sales, self.products, self.customers, self.cities)
        self.assertIn("ProductAnalysis", results)
        self.assertIn("CityAnalysis", results)
        self.assertTrue(len(results["ProductAnalysis"]) > 0)
        self.assertTrue(len(results["CityAnalysis"]) > 0)

if __name__ == "__main__":
    unittest.main()