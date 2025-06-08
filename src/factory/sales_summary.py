class SalesSummary:
    def __init__(self, product_id, total_revenue, total_units):
        self.product_id = product_id
        self.total_revenue = total_revenue
        self.total_units = total_units

    def __repr__(self):
        return f"<SalesSummary product_id={self.product_id}, revenue={self.total_revenue}, units={self.total_units}>"

class SalesSummaryFactory:
    @staticmethod
    def from_series(series):
        return SalesSummary(
            product_id=series['ProductID'],
            total_revenue=series['TotalPrice'],
            total_units=series['Quantity']
        )