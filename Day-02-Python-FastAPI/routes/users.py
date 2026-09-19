from fastapi import APIRouter, HTTPException
from schemas.user import User
from services.user_service import create_user as create_user_service

router = APIRouter()

@router.get("/users")
def get_users():
    return {"users": ["Rahul", "Ankit", "Priya"]}

@router.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in [1, 2, 3]:
        raise HTTPException(status_code=404, detail="user not found")

    return {"user_id": user_id}

@router.post("/users")
def create_user(user: User):
    return create_user_service(user)