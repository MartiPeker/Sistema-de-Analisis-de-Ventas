class City:
    def __init__(self, city_id, city_name, zipcode, country_id):
        self.city_id = city_id
        self.city_name = city_name
        self.zipcode = zipcode
        self.country_id = country_id

    def __repr__(self):
        return f"<City {self.city_id}: {self.city_name}>"