from sqlalchemy import Column, Integer, Float, String, ForeignKey
from src.orm.base import Base

class Sale(Base):
    __tablename__ = 'sales'

    sale_id = Column('SalesID', Integer, primary_key=True)
    salesperson_id = Column('SalesPersonID', Integer, ForeignKey('employees.EmployeeID'))
    customer_id = Column('CustomerID', Integer, ForeignKey('customers.CustomerID'))
    product_id = Column('ProductID', Integer, ForeignKey('products.ProductID'))
    quantity = Column('Quantity', Integer)
    discount = Column('Discount', Float)
    total_price = Column('TotalPrice', Float)
    sales_date = Column('SalesDate', String(50))  # Puede ajustarse a DateTime
    transaction_number = Column('TransactionNumber', String(255))