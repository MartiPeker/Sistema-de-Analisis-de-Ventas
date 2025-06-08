from sqlalchemy import Column, Integer, String, ForeignKey
from src.orm.base import Base

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column('CustomerID', Integer, primary_key=True)
    first_name = Column('FirstName', String(50))
    middle_initial = Column('MiddleInitial', String(1))
    last_name = Column('LastName', String(50))
    city_id = Column('CityID', Integer, ForeignKey('cities.CityID'))
    address = Column('Address', String(255))