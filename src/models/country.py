class Country:
    def __init__(self, country_id, country_name, country_code):
        self.country_id = country_id
        self.country_name = country_name
        self.country_code = country_code

    def __repr__(self):
        return f"<Country {self.country_id}: {self.country_name}>"