from fastapi import FastAPI
from .routes import sales, products, users

app = FastAPI(title="kdxPOS API", version="0.1.0")

@app.get("/")
def root():
    return {"message": "Welcome to kdxPOS API"}

# Include routes
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(users.router, prefix="/users", tags=["Users"])
