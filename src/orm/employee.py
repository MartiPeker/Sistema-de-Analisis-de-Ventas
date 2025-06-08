from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.orm.base import Base

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column('EmployeeID', Integer, primary_key=True)
    first_name = Column('FirstName', String(50))
    middle_initial = Column('MiddleInitial', String(1))
    last_name = Column('LastName', String(50))
    birth_date = Column('BirthDate', String(50))  # Puede ajustarse a Date
    gender = Column('Gender', String(1))
    city_id = Column('CityID', Integer, ForeignKey('cities.CityID'))
    hire_date = Column('HireDate', String(50))  # Puede ajustarse a DateTime