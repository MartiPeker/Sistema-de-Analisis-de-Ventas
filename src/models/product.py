class Product:
    def __init__(self, product_id, product_name, price, category_id, prod_class, modify_date, resistant, is_allergic, vitality_days):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category_id = category_id
        self.prod_class = prod_class
        self.modify_date = modify_date
        self.resistant = resistant
        self.is_allergic = is_allergic
        self.vitality_days = vitality_days

    def __repr__(self):
        return f"<Product {self.product_id}: {self.product_name}>"