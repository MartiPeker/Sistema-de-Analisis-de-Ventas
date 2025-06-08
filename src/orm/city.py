from sqlalchemy import Column, Integer, String, ForeignKey
from src.orm.base import Base

class City(Base):
    __tablename__ = 'cities'

    city_id = Column('CityID', Integer, primary_key=True)
    city_name = Column('CityName', String(100))
    zipcode = Column('Zipcode', String(20))
    country_id = Column('CountryID', Integer, ForeignKey('countries.CountryID'))