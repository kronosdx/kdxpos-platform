from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    barcode = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    stock_qty = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    cashier = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    payment_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
