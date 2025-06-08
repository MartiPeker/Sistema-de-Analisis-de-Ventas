class Customer:
    def __init__(self, customer_id, first_name, middle_initial, last_name, city_id, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.city_id = city_id
        self.address = address

    def __repr__(self):
        return f"<Customer {self.customer_id}: {self.first_name} {self.last_name}>"