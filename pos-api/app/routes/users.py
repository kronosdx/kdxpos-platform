from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    role: str

@router.get("/", response_model=list[User])
def list_users():
    return [
        {"username": "admin", "role": "manager"},
        {"username": "cashier1", "role": "operator"}
    ]
