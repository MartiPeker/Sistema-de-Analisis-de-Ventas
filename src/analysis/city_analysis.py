from collections import defaultdict
from .base_strategy import AnalysisStrategy

class CityAnalysisStrategy(AnalysisStrategy):
    def analyze(self, sales, products, customers, cities):
        customer_map = {c.customer_id: c.city_id for c in customers}
        city_map = {city.city_id: city.city_name for city in cities}
        city_sales = defaultdict(float)
        for sale in sales:
            city_id = customer_map.get(sale.customer_id)
            if city_id:
                city_name = city_map.get(city_id, "Unknown")
                city_sales[city_name] += sale.total_price
        return sorted(city_sales.items(), key=lambda x: x[1], reverse=True)