from collections import defaultdict
from .base_strategy import AnalysisStrategy

class ProductAnalysisStrategy(AnalysisStrategy):
    def analyze(self, sales, products, customers, cities):
        product_sales = defaultdict(int)
        for sale in sales:
            product_sales[sale.product_id] += sale.total_price
        result = [
            (product_id, total)
            for product_id, total in product_sales.items()
        ]
        return sorted(result, key=lambda x: x[1], reverse=True)