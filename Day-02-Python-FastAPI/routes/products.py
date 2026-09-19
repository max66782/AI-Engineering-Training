from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
def get_products(category: str):
    return {"category": category}