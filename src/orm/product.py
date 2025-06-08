from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.orm.base import Base

class Product(Base):
    __tablename__ = 'products'

    product_id = Column('ProductID', Integer, primary_key=True)
    product_name = Column('ProductName', String(255))
    price = Column('Price', Float)
    category_id = Column('CategoryID', Integer, ForeignKey('categories.CategoryID'))
    prod_class = Column('Class', String(50))
    modify_date = Column('ModifyDate', String(50))
    resistant = Column('Resistant', String(50))
    is_allergic = Column('IsAllergic', String(50))
    vitality_days = Column('VitalityDays', Integer)