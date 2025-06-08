from sqlalchemy import Column, Integer, String
from src.orm.base import Base

class Country(Base):
    __tablename__ = 'countries'

    country_id = Column('CountryID', Integer, primary_key=True)
    country_name = Column('CountryName', String(100))
    country_code = Column('CountryCode', String(10))