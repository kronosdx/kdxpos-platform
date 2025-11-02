from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    barcode: str
    price: float
    stock_qty: float = 0

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class SaleItem(BaseModel):
    product_id: int
    qty: float
    price: float

class SaleBase(BaseModel):
    cashier: str
    total: float
    payment_type: str

class SaleCreate(SaleBase):
    items: List[SaleItem]

class Sale(SaleBase):
    id: int
    class Config:
        orm_mode = True
