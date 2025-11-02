from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class SaleItem(BaseModel):
    product_code: str
    qty: float
    price: float

class Sale(BaseModel):
    cashier: str
    items: List[SaleItem]
    total: float
    payment_type: str

@router.post("/")
def create_sale(sale: Sale):
    return {
        "status": "success",
        "message": "Sale processed successfully",
        "data": sale.dict()
    }
