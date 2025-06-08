class Sale:
    def __init__(self, sale_id, salesperson_id, customer_id, product_id, quantity, discount, total_price, sales_date, transaction_number):
        self.sale_id = sale_id
        self.salesperson_id = salesperson_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.discount = discount
        self.total_price = total_price
        self.sales_date = sales_date
        self.transaction_number = transaction_number

    def __repr__(self):
        return f"<Sale {self.sale_id}: Product {self.product_id} to Customer {self.customer_id}>"